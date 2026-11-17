#!/usr/bin/env python3
"""Boundary cases for the notebook's public function contracts; branch-only."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import nbformat

root=Path(__file__).resolve().parents[2]
path=root/'6/Wykład 6.ipynb'
nb=nbformat.read(path,as_version=4)
codes=[c.source for c in nb.cells if c.cell_type=='code']
swap=next(c for c in codes if 'void swap(' in c).split('int main(void)')[0]
sumdiff=next(c for c in codes if 'void suma_roznica(' in c).split('int main(void)')[0]
checks=[]
for a,b in [(3,8),(8,3),(5,5),(-2,-7),(0,0),(-2147483648,2147483647)]:
 checks.append(f'{{ int a={a}, b={b}; swap(&a,&b); assert(a=={b} && b=={a}); swap(&a,&b); assert(a=={a} && b=={b}); }}')
checks.append('{ int a=-7; swap(&a,&a); assert(a==-7); }')
tests={'swap':swap+'\n#include <assert.h>\nint main(void) {\n'+'\n'.join(checks)+'\nreturn 0;\n}\n'}
checks=[]
for a,b in [(8,3),(3,8),(0,0),(-3,-8),(-8,-3),(-10,7)]:
 checks.append(f'{{ int s=99, r=99; suma_roznica({a},{b},&s,&r); assert(s=={a+b} && r=={a-b}); }}')
tests['suma_roznica']=sumdiff+'\n#include <assert.h>\nint main(void) {\n'+'\n'.join(checks)+'\nreturn 0;\n}\n'
memcpy=next(c for c in codes if 'unsigned char bufor[' in c)
tests['memcpy-negative-roundtrip']=memcpy.replace('int x = 5;', 'int x = -3;').replace('int y = 8;', 'int y = 42;')
report={'notebook_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'result':'PASS','tests':[]}
with tempfile.TemporaryDirectory(prefix='w6-regression-') as tmp:
 for name,source in tests.items():
  src=Path(tmp)/(name+'.c');src.write_text(source)
  for mode,flags in [('O0',['-O0']),('O2',['-O2']),('san',['-O1','-g','-fsanitize=address,undefined','-fno-pie','-no-pie'])]:
   exe=Path(tmp)/(name+'-'+mode)
   command=['gcc','-std=c11','-Wall','-Wextra','-Wpedantic','-Werror',*flags,str(src),'-o',str(exe)]
   compiled=subprocess.run(command,capture_output=True,text=True,timeout=30)
   assert compiled.returncode==0 and not compiled.stderr,(command,compiled.stderr)
   run=subprocess.run([str(exe)],capture_output=True,text=True,timeout=10,env=dict(os.environ,ASAN_OPTIONS='detect_leaks=1:halt_on_error=1',UBSAN_OPTIONS='halt_on_error=1:print_stacktrace=1'))
   assert run.returncode==0 and not run.stderr,(name,mode,run.stderr)
   if name=='memcpy-negative-roundtrip': assert run.stdout.endswith('Odzyskane: x=-3 y=42\nZgodnosc: 1\n'),run.stdout
   report['tests'].append({'name':name,'mode':mode,'command':command,'source':source,'exit':run.returncode,'stdout':run.stdout})
out=Path(__file__).parent/'results/regression.json';out.write_text(json.dumps(report,indent=2)+'\n')
print('PASS: swap 7 cases (including identity, negative values, int extrema, double swap); sum/difference 6 cases; negative memcpy roundtrip; all O0/O2/ASan+UBSan')
