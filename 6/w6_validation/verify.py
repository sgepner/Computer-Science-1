#!/usr/bin/env python3
"""Local W6 gate; branch-only verification, not a student dependency."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import nbformat

ROOT = Path(__file__).resolve().parents[2]
NOTEBOOK = ROOT / '6/Wykład 6.ipynb'
parser = argparse.ArgumentParser()
parser.add_argument('--through', type=int, default=13)
parser.add_argument('--kernel', action='store_true')
args = parser.parse_args()
out = Path(__file__).parent / 'results'
out.mkdir(exist_ok=True)
nb = nbformat.read(NOTEBOOK, as_version=4)
nbformat.validate(nb)
assert nb.metadata.kernelspec.name == 'c'
sections = [int(x) for c in nb.cells if c.cell_type == 'markdown'
            for x in re.findall(r'^## W6\.(\d+)\b', c.source, re.M)]
assert sections == list(range(1, 14)), sections
for c in nb.cells:
    assert c.source.strip(), 'Empty cell'
    if c.cell_type == 'code':
        assert not c.outputs and c.execution_count is None
    for name, data in c.get('attachments', {}).items():
        assert data and f'attachment:{name}' in c.source
    for target in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', c.source):
        if target.startswith('attachment:'):
            assert target[11:] in c.get('attachments', {})
        else:
            assert not target.startswith(('http:', 'https:'))
            assert (NOTEBOOK.parent / target).is_file(), target

report = {'notebook_sha256': hashlib.sha256(NOTEBOOK.read_bytes()).hexdigest(),
          'base_or_head': subprocess.check_output(['git','rev-parse','HEAD'], cwd=ROOT, text=True).strip(),
          'gcc': subprocess.check_output(['gcc','--version'], text=True).splitlines()[0],
          'through': args.through, 'runs': []}
selected = []
section = 0
for i,c in enumerate(nb.cells):
    if c.cell_type == 'markdown':
        m = re.search(r'^## W6\.(\d+)\b', c.source, re.M)
        if m: section = int(m.group(1))
    if c.cell_type == 'code' and section <= args.through:
        selected.append((i,section,c))
assert selected, 'No executable examples'

def check_semantics(section, source, stdout):
    if section == 1:
        assert stdout == 'a = 100, rozmiar = 4 B\nd = 3.5, rozmiar = 8 B\nc = A, rozmiar = 1 B\n', stdout
    elif section == 2:
        m = re.fullmatch(r'Przed: a = 100, &a = (0x[0-9a-fA-F]+)\nPo:    a = 200, &a = (0x[0-9a-fA-F]+)\n', stdout)
        assert m and m[1] == m[2], stdout
    elif section == 3:
        m = re.fullmatch(r'&a = (0x[0-9a-fA-F]+)\np  = (0x[0-9a-fA-F]+)\n&p = (0x[0-9a-fA-F]+)\np == &a: 1\nRozmiar a = 4 B, p = 8 B\nRozmiar d = 8 B, pd = 8 B\n',stdout)
        assert m and m[1] == m[2] and m[1] != m[3], stdout
    elif section == 4:
        assert stdout.startswith('a = 100, *p = 100\n') and stdout.endswith('Po a = 20: a = 20, *p = 20\n'), stdout
        a, p, pp = re.search(r'&a = (0x[0-9a-f]+), p = (0x[0-9a-f]+), &p = (0x[0-9a-f]+)', stdout).groups()
        assert a == p and a != pp
    elif section == 5:
        assert stdout == ('Start:      a=100 b=200 *p=100 *q=100\n'
            '*p = 20:    a=20 b=200 *p=20 *q=20\n'
            'p = &b:     a=20 b=200 *p=200 *q=20\n'
            '*p = 30:    a=20 b=30 *p=30 *q=20\n'
            'p == &b: 1, q == &a: 1\n'), stdout
    elif section == 6:
        lines=stdout.splitlines()
        a,b=re.findall(r'0x[0-9a-f]+',lines[0]); c,d=re.findall(r'0x[0-9a-f]+',lines[1])
        assert a==b and c==d and a!=c, stdout
        assert '\n'.join(lines[2:]) == ('Start:       a=100 b=200 **pp=100\n'
            '**pp = 20:   a=20 b=200 **pp=20\n'
            '*pp = &b:    a=20 b=200 **pp=200\n'
            '**pp = 30:   a=20 b=30 **pp=30\n'
            'p == &b: 1, pp == &p: 1'), stdout
    elif section == 7:
        assert stdout == ('Brak celu: nie odczytujemy *p.\n'
            'Po p = &a: *p = 10\nPo zapisie: a = 20\n'), stdout
    elif section == 8:
        assert stdout == ('W zmien_kopie: a=500\nPo zmien_kopie: a=9\n'
            'W zmien_cel: *p=500\nPo zmien_cel: a=500\n'
            'W przepnij_kopie: *p=300\nPo przepnij_kopie: a=500 *p=500 p==&a: 1\n'), stdout
    elif section == 9:
        if 'suma_roznica' in source:
            assert stdout == 'suma=11 roznica=5\n', stdout
        elif 'void swap' in source:
            assert stdout == 'Przed: a=3 b=8\nPo:    a=8 b=3\n', stdout
        else: raise AssertionError('Unexpected W6.9 program')
    elif section == 10:
        lines=stdout.splitlines()
        for line,label,size in zip(lines[:3],['char','int','double'],[1,4,8]):
            m=re.fullmatch(r'(char|int|double): +p=(0x[0-9a-f]+), p\+1=(0x[0-9a-f]+), krok=(\d+) B',line)
            assert m and m[1]==label and int(m[3],16)-int(m[2],16)==size and int(m[4])==size, line
        assert len(lines)==4 and lines[3]=='Wartosci bez zmian: c=A a=10 d=3.5',stdout
    elif section == 11:
        a,p=re.findall(r'0x[0-9a-f]+',stdout.splitlines()[0])
        assert a==p,stdout
        assert '\n'.join(stdout.splitlines()[1:])=='a = 4449, odczyt przez p = 4449\nPo zapisie: a = 20',stdout
    elif section == 12:
        assert stdout == ('int: 4 B, double: 8 B, dwie reprezentacje int: 8 B\n'
            'Przed kopiowaniem: x=5 y=8 d=9.0\n'
            'Skopiowano 8 B do d; nie odczytujemy wartosci double.\n'
            'Odzyskane: x=5 y=8\nZgodnosc: 1\n'),stdout
    else:
        raise AssertionError(f'No semantic oracle for W6.{section}')

def normalized(s):
    return re.sub(r'0x[0-9a-fA-F]+', '<address>', s)

with tempfile.TemporaryDirectory(prefix='w6-check-') as tmp:
    tmp = Path(tmp)
    for i,section,c in selected:
        src = tmp/f'cell_{i}.c'
        src.write_text(c.source)
        row = {'cell':i,'section':section,'modes':{}}
        reference = None
        for mode, flags in [('O0',['-O0']),('O2',['-O2']),
                            ('san',['-O1','-g','-fsanitize=address,undefined','-fno-omit-frame-pointer','-fno-pie','-no-pie'])]:
            exe = tmp/f'cell_{i}_{mode}'
            command = ['gcc','-std=c11','-Wall','-Wextra','-Wpedantic','-Werror',*flags,str(src),'-o',str(exe)]
            built = subprocess.run(command, capture_output=True,text=True,timeout=30)
            assert built.returncode == 0 and not built.stderr, (command,built.stdout,built.stderr)
            env = dict(os.environ, ASAN_OPTIONS='detect_leaks=1:halt_on_error=1', UBSAN_OPTIONS='halt_on_error=1:print_stacktrace=1')
            run = subprocess.run([str(exe)],capture_output=True,text=True,timeout=10,env=env)
            (out/f'cell_{i}_{mode}.txt').write_text(run.stdout+run.stderr)
            assert run.returncode == 0 and not run.stderr, (i,mode,run.returncode,run.stderr)
            check_semantics(section, c.source, run.stdout)
            norm = normalized(run.stdout)
            # Only addresses may vary. Byte representation demonstrations must stay stable on this host.
            if reference is None: reference = norm
            else: assert norm == reference, (i,mode,reference,norm)
            row['modes'][mode] = {'command':command,'exit':run.returncode,'stdout':run.stdout}
        report['runs'].append(row)

if args.kernel:
    # Existing kernel package lives in the user's established Jupyter environment.
    venv = '/home/sgepner/Virtualenv/jupyter/bin/python'
    with tempfile.TemporaryDirectory(prefix='w6-jupyter-') as td:
        td = Path(td)
        spec = td/'data/kernels/c'
        spec.mkdir(parents=True)
        (spec/'kernel.json').write_text(json.dumps({'argv':[venv,'-m','jupyter_c_kernel','-f','{connection_file}'],'display_name':'C','language':'c'}))
        code_nb = nbformat.v4.new_notebook(cells=[nbformat.v4.new_code_cell(c.source) for _,_,c in selected],metadata=nb.metadata)
        inp = td/'input.ipynb'
        nbformat.write(code_nb,inp)
        program = '''import sys,nbformat\nfrom nbclient import NotebookClient\nn=nbformat.read(sys.argv[1],as_version=4)\nNotebookClient(n,timeout=60,kernel_name="c",allow_errors=False,resources={"metadata":{"path":sys.argv[3]}}).execute()\nnbformat.write(n,sys.argv[2])\n'''
        executed = out/'kernel-executed.ipynb'
        env = dict(os.environ, JUPYTER_PATH=str(td/'data'), JUPYTER_RUNTIME_DIR=str(td/'runtime'), IPYTHONDIR=str(td/'ipython'))
        proc = subprocess.run([venv,'-c',program,str(inp),str(executed),str(ROOT/'6')],env=env,capture_output=True,text=True,timeout=180)
        (out/'kernel.log').write_text(proc.stdout+proc.stderr)
        assert proc.returncode == 0, proc.stderr
        ran = nbformat.read(executed,as_version=4)
        for (i,_,_),actual,expected in zip(selected,ran.cells,report['runs']):
            # C kernel reports compilation/runtime failures on stderr with status ok!
            assert not any(o.output_type=='error' or (o.output_type=='stream' and o.name=='stderr') for o in actual.outputs), (i,actual.outputs)
            stdout = ''.join(o.text for o in actual.outputs if o.output_type=='stream' and o.name=='stdout')
            assert normalized(stdout)==normalized(expected['modes']['O0']['stdout']), (i,stdout,expected)
        report['kernel'] = {'cells':len(ran.cells),'result':'PASS','python':venv}

(out/f'report-through-{args.through}.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print(f'PASS: structure; {len(selected)} C11 examples × O0/O2/ASan+UBSan; through W6.{args.through}; kernel={args.kernel}')
print(f'Evidence: {out}')
