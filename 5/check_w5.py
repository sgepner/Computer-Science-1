#!/usr/bin/env python3
"""C11 regression for exact W5 examples, terminal game, binary32 and Fourier.
Run from any directory: python3 5/check_w5.py. GCC/Linux reference environment.
"""
import json
import math
import os
from pathlib import Path
import re
import struct
import subprocess
import tempfile
import nbformat

NB=Path(__file__).resolve().parent/"Wykład 5.ipynb"
EXPECTED = {
 0: "".join(f"{i}\n" for i in range(101)),
 1: "| limit=0 i=0\n0 | limit=1 i=1\n0 1 2 3 4 5 6 7 8 9 | limit=10 i=10\n",
 2: "while=100 do=101\n",
 3: "init\ntest 0\nbody 0\nupdate\ntest 1\nbody 1\nupdate\ntest 2\nkoniec 2\n",
 4: "0 1 2 \n",
 5: "< : n=10 i=10\n<=: n=11 i=11\n10 8 6 4 2 0 | i=-2\n",
 6: "0 1 2 \n1 2 3 \n",
 7: "wewnatrz=0 wewnatrz=1 po=7 globalna=20\nj=3\n",
 8: "".join(f"{i} {i/10:.3f}\n" for i in range(11)),
 9: "0 2 4 6 8 10 | krok: i=12\n0 2 4 6 8 10 | filtr: i=11\n",
 10: "1 3 5 7 9 \n1 3 5 7 9 \n",
 12: "0 1 2 3 4\n1 2 3 4 5\n2 3 4 5 6\n3 4 5 6 7\nelementow=20\n",
 13: "0 1 2 3 4 | break i=5\n0 1 2 3 4 6 7 8 9 | continue i=10\n",
 14: "0 1 2 3 4 6 7 8 9 | i=10\n",
 15: "(0,1) wiersz\n(1,0) wiersz\n",
 16: "proby=3\n",
 17: "0 1 1 2 3 5 8 13 21 34\n",
 18: "2 3 5 7 11 13 17 19 23 29 \n",
}

def run(argv,data=""):
 return subprocess.run(argv,input=data,capture_output=True,text=True,timeout=5,
                       env={**os.environ,"LC_ALL":"C"})

def build(text,temp,opt):
 source=temp/"p.c";exe=temp/"p";source.write_text(text)
 result=run(["gcc","-std=c11",opt,"-Wall","-Wextra","-Werror","-pedantic",str(source),"-o",str(exe),"-lm"])
 assert result.returncode==0 and not result.stderr,result.stderr
 return exe

def f32(x):
 return struct.unpack("f",struct.pack("f",x))[0]

def check_float(output):
 rows=[line.split() for line in output.splitlines()]
 assert len(rows)==11
 x=0.0;h=f32(0.1)
 for i,row in enumerate(rows):
  index=int(row[0]);acc,direct,eacc,edir=map(float,row[1:])
  assert index==i
  ref_direct=f32(i*h)
  assert math.isclose(acc,x,rel_tol=0,abs_tol=5.1e-10),(i,acc,x)
  assert math.isclose(direct,ref_direct,rel_tol=0,abs_tol=5.1e-10),(i,direct,ref_direct)
  # Errors printed to 4 significant digits; independent binary32 recurrence oracle.
  assert math.isclose(eacc,x-i/10,rel_tol=5.1e-4,abs_tol=1e-15),(i,eacc)
  assert math.isclose(edir,ref_direct-i/10,rel_tol=5.1e-4,abs_tol=1e-15),(i,edir)
  x=f32(x+h)
 last=rows[-1]
 assert float(last[1])>1 and float(last[2])==1
 print(f"  binary32 final: accumulated={last[1]}, indexed={last[2]}, errors={last[3:]}")

def check_fourier(output,N=5,m=9):
 rows=[list(map(float,line.split())) for line in output.splitlines()]
 assert len(rows)==m
 for i,(x,y) in enumerate(rows):
  target_x=-1+2*i/(m-1)
  assert abs(x-target_x)<5.1e-3
  # Independent formula and analytic checkpoints, including jumps and oddness.
  expected=4/math.pi*sum(math.sin((2*k+1)*math.pi*target_x)/(2*k+1) for k in range(N))
  assert abs(y-expected)<5.1e-7,(N,x,y,expected)
  assert abs(y+rows[m-1-i][1])<1e-6
  if i in (0,m//2,m-1):assert abs(y)<1e-6
 if m==9:
  quarter=rows[6][1]
  if N==1:assert abs(quarter-4/math.pi)<5.1e-7
  if N==2:assert abs(quarter-(4/math.pi)*(1-1/3))<5.1e-7
 return rows

def main():
 raw=json.loads(NB.read_text());nbformat.validate(nbformat.from_dict(raw))
 assert raw["metadata"]["kernelspec"]["name"]=="c"
 codes=[c for c in raw["cells"] if c["cell_type"]=="code"]
 assert len(codes)==20
 assert set(EXPECTED)==set(range(20))-{11,19}
 assert all(c["outputs"]==[] and c["execution_count"] is None for c in codes)
 assert not any(re.search(r"\b(?:scanf|sscanf|gets)\s*\(","".join(c["source"])) for c in codes)
 count=0
 with tempfile.TemporaryDirectory(prefix="w5_check_") as td:
  temp=Path(td)
  for opt in ("-O0","-O2"):
   for i,c in enumerate(codes):
    result=run([str(build("".join(c["source"]),temp,opt))])
    assert result.returncode==0 and result.stderr=="",(i,result)
    if i==11:check_float(result.stdout)
    elif i==19:check_fourier(result.stdout)
    else:assert result.stdout==EXPECTED[i],(i,opt,repr(result.stdout),repr(EXPECTED[i]))
    count+=1
   # Same while code, changed initial condition: zero bodies when limit=0;
   # same do-while code with both initial counters 9: both execute once.
   text="".join(codes[2]["source"]).replace("a = 100, b = 100","a = 9, b = 9")
   assert run([str(build(text,temp,opt))]).stdout=="while=10 do=10\n"
   for N in (1,2,5):
    for m in (9,17):
     text="".join(codes[19]["source"]).replace("m = 9, N = 5",f"m = {m}, N = {N}")
     check_fourier(run([str(build(text,temp,opt))]).stdout,N,m)
   # Preserve the stated 1e-12 invariant using raw function results, not a
   # six-decimal display. The original szereg implementation is unmodified.
   unit="".join(codes[19]["source"]).replace("int main(void)","int notebook_main(void)",1)+r"""
int main(void)
{
    int ns[] = {1, 2, 5};
    double xs[] = {-1, -0.5, -0.125, 0, 0.125, 0.5, 1};
    for (int i=0; i<3; ++i)
        for (int j=0; j<7; ++j)
            printf("%d %.17g %.17g\n", ns[i], xs[j], szereg(xs[j],1.0,ns[i]));
    return 0;
}
"""
   result=run([str(build(unit,temp,opt))])
   assert result.returncode==0 and result.stderr==""
   rawrows=[line.split() for line in result.stdout.splitlines()]
   assert len(rawrows)==21
   values={(int(n),float(x)):float(y) for n,x,y in rawrows}
   for (N,x),y in values.items():
    assert abs(y+values[N,-x])<1e-12,(opt,N,x,"oddness")
    if x in (-1,0,1):assert abs(y)<1e-12,(opt,N,x,"jump")
    if N==1 and x==0.5:assert abs(y-4/math.pi)<1e-12
    if N==2 and x==0.5:assert abs(y-(4/math.pi)*(1-1/3))<1e-12
   print(f"  Fourier raw {opt}: 21 values, oddness/jump zeros/analytic N=1,2 at 1e-12")
   # Exact terminal game is compiled from Markdown, never from another wrapper.
   gamecell=next(c for c in raw["cells"] if "while (tura < 5)" in "".join(c["source"]))
   game=re.findall(r"```c\n(.*?)```","".join(gamecell["source"]),re.S)
   assert len(game)==1 and "sscanf" not in game[0]
   exe=build(game[0],temp,opt)
   prompt="Podaj liczbe nie wieksza niz 10:\n"
   cases=[
    ("7\n11\n",0,prompt+"My is greater I win!! 7 8\n"+prompt+"You cheat, I win!!\n"),
    ("kot\n",1,prompt+"Blad danych\n"),
    ("",0,prompt+"Koniec wejscia\n"),
    ("7\n",0,prompt+"My is greater I win!! 7 8\n"+prompt+"Koniec wejscia\n"),
    ("11\n",0,prompt+"You cheat, I win!!\n"),
    ("0\n1\n2\n3\n4\n",0,"".join(prompt+f"My is greater I win!! {i} {i+1}\n" for i in range(5))+"Koniec 5 tur\n"),
    ("7\nkot\n",1,prompt+"My is greater I win!! 7 8\n"+prompt+"Blad danych\n"),
    ("-2147483648\n11\n",0,prompt+"My is greater I win!! -2147483648 -2147483647\n"+prompt+"You cheat, I win!!\n"),
   ]
   for data,status,expected in cases:
    result=run([str(exe)],data)
    assert (result.returncode,result.stdout,result.stderr)==(status,expected,""),(opt,data,result)
   count+=len(cases)
   # Scope failure is tested from the exact displayed complete C fragment.
   scope=next(c for c in raw["cells"] if "obie nazwy poza zasięgiem" in "".join(c["source"]))
   text=re.findall(r"```c\n(.*?)```","".join(scope["source"]),re.S)[0]
   source=temp/"bad.c";source.write_text(text)
   bad=run(["gcc","-std=c11","-Wall","-Wextra","-pedantic-errors","-fsyntax-only",str(source)])
   assert bad.returncode!=0 and "undeclared" in bad.stderr,bad.stderr
 print(f"PASS W5: {count} golden/game runs; 12 Fourier N/m variants + 42 raw Fourier values at 1e-12; 2 do-while boundary runs; 11-point float oracle at both optimizations; scope EXPECTED-FAIL")
 print("PASS structure, C11 -Wall -Wextra -Werror -pedantic, no interactive code cells")

if __name__=="__main__":main()
