#!/usr/bin/env python3
"""Structure/resources/provenance and W1 C11 diagnostics; optional actual C kernel.

python3 check_w1_w5.py
python3 check_w1_w5.py --kernel --kernel-python /path/to/venv/bin/python

Run focused numerical/output suites separately:
python3 2/check_w2.py; python3 3/check_w3.py
python3 4/check_w4.py; python3 5/check_w5.py
The kernel test compares safe complete programs with independent GCC executions.
Intentional UB is NEVER executed. Terminal-only Markdown programs are checked by
the focused suites, not submitted to a blocking notebook kernel.
"""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import nbformat

ROOT=Path(__file__).resolve().parent
BASE="9a42b0348e74c25795dad19a1bafc25f349a9d92"
EN=["","Lecture 1 examples.ipynb","Lecture 2 Examples.ipynb",
    "Lecture 3 Examples.ipynb","Lecture 4 examples.ipynb","Lecture 5 examples.ipynb"]
W1_FRAGMENTS={31,42,47,54,60}
W1_ERRORS={25:"main",26:"implicit declaration",28:"expected",34:"two or more",
           40:"invalid suffix",51:"redefinition",58:"main",65:"implicit declaration"}
W1_GOLDEN={
10:"Hello students, this is a piece of code!!\n",
36:"Hello students this is a piece of code!!\n",
38:"Hello students, this is a piece of code!!\n",
45:"Hello students, this is a piece of code!!\n",
56:"3\n",
67:"This is a printf from function sum()\n",
70:"This is a printf from function sum()\n",
72:"a+b=11\n",
75:"Hello CS1 students!!\n",
77:"Hello CS1 students!!\na+b=14\n",
79:"Hello CS1 students!!\na+b=11\n",
}

def run(cmd,**kw):
 return subprocess.run(cmd,capture_output=True,timeout=10,
                       env={**os.environ,"LC_ALL":"C"},**kw)

def stripped(text):
 return re.sub(r"//[^\n]*|/\*.*?\*/","",text,flags=re.S)

def compile_source(text,temp,opt="-O0",strict=True,fragment=False):
 source=temp/"p.c";exe=temp/"p";source.write_text(text)
 cmd=["gcc","-std=c11",opt,"-Wall","-Wextra","-pedantic"]
 if strict:cmd+=["-pedantic-errors"]
 cmd += [str(source),"-o",str(exe)]
 cmd += ["-c"] if fragment else ["-lm"]
 return run(cmd),exe

def structural():
 docs={}
 refs=0
 for n in range(1,6):
  p=ROOT/str(n)/f"Wykład {n}.ipynb";raw=json.loads(p.read_text())
  nbformat.validate(nbformat.from_dict(raw))
  assert raw["metadata"]["kernelspec"]["name"]=="c"
  docs[n]=raw
  for i,c in enumerate(raw["cells"]):
   s="".join(c["source"])
   assert s.strip(),(n,i,"empty cell")
   if c["cell_type"]=="code":
    assert c["execution_count"] is None and not c["outputs"],(n,i,"stale outputs")
    assert not re.search(r"\b(?:scanf|fgets|gets)\s*\(",stripped(s)),(n,i,"interactive or unsafe")
   if c["cell_type"]!="markdown":continue
   for token in ("W4-INT","historyczny wykład","Odzyskany eksperyment","wersji pokazywanej kiedyś"):
    assert token not in s,(n,i,token)
   paths=re.findall(r'<img\b[^>]*\bsrc=["\']([^"\']+)',s)
   paths+=re.findall(r'!\[[^\]]*\]\(([^)]+)\)',s)
   for link in paths:
    if link.startswith(("http:","https:","data:")):continue
    if link.startswith("attachment:"):
     assert link.split(":",1)[1] in c.get("attachments",{}),(n,i,link)
    else:
     assert (p.parent/link).is_file(),(n,i,link)
    refs+=1
 # Byte provenance for ALL protected legacy documents, not target Polish files.
 for n in range(1,6):
  for name in (EN[n],f"lec{n}.pdf",f"lec{n}.tex"):
   rel=f"{n}/{name}"
   actual=run(["git","hash-object",str(ROOT/rel)]).stdout.strip()
   expected=run(["git","rev-parse",f"{BASE}:{rel}"],cwd=ROOT).stdout.strip()
   assert actual==expected,(rel,actual,expected)
 print(f"PASS 5 nbformat notebooks, kernel c, {refs} local image references, clean code outputs; 15 legacy file hashes match base")
 return docs

def check_w1(raw,temp):
 codeindices={i for i,c in enumerate(raw["cells"]) if c["cell_type"]=="code"}
 assert codeindices==W1_FRAGMENTS|set(W1_ERRORS)|set(W1_GOLDEN)
 for i in sorted(codeindices):
  text="".join(raw["cells"][i]["source"])
  if i in W1_FRAGMENTS:
   built,_=compile_source(text+"\nint fragment_context;\n",temp,fragment=True)
   assert built.returncode==0,(i,built.stderr)
  elif i in W1_ERRORS:
   built,_=compile_source(text,temp)
   assert built.returncode!=0 and W1_ERRORS[i].encode() in built.stderr,(i,built.stderr)
  else:
   for opt in ("-O0","-O2"):
    built,exe=compile_source(text,temp,opt)
    assert built.returncode==0,(i,built.stderr)
    result=run([str(exe)])
    assert (result.returncode,result.stdout.decode(),result.stderr)==(0,W1_GOLDEN[i],b""),(i,result)
 print("PASS W1: 11 valid programs x O0/O2; 5 object-only fragments; 8 expected compile/link diagnostics")
 print("W1 pre-existing identifier examples have intentional unused-variable warnings; no warnings suppressed")

def kernel_check(docs,temp,python,join_output_threads=False):
 from jupyter_client import KernelManager
 from jupyter_client.kernelspec import KernelSpecManager
 # A temporary spec selects the existing interpreter, without editing user configuration.
 spec=temp/"kernels"/"c";spec.mkdir(parents=True)
 argv=[python,"-m","jupyter_c_kernel","-f","{connection_file}"]
 if join_output_threads:
  # Repair only the installed kernel's subprocess-output transport race.
  # Compilation, execution, assertions and the kernel's do_execute are unchanged.
  driver=temp/"kernel_driver.py"
  driver.write_text(
   "from jupyter_c_kernel.kernel import CKernel, RealTimeSubprocess\n"
   "from ipykernel.kernelapp import IPKernelApp\n"
   "original = RealTimeSubprocess.write_contents\n"
   "def drain(self):\n"
   "    if self.poll() is not None:\n"
   "        self._stdout_thread.join(timeout=2)\n"
   "        self._stderr_thread.join(timeout=2)\n"
   "        if self._stdout_thread.is_alive() or self._stderr_thread.is_alive():\n"
   "            raise RuntimeError('kernel output reader did not finish')\n"
   "    return original(self)\n"
   "RealTimeSubprocess.write_contents = drain\n"
   "IPKernelApp.launch_instance(kernel_class=CKernel)\n")
  argv=[python,str(driver),"-f","{connection_file}"]
  print("Kernel transport workaround ON: join completed-process reader threads before final drain; no compiler/output assertions changed",flush=True)
 (spec/"kernel.json").write_text(json.dumps({"argv":argv,"display_name":"C","language":"c"}))
 manager=KernelSpecManager(kernel_dirs=[str(temp/"kernels")])
 evidence=[]
 for n,raw in docs.items():
  km=KernelManager(kernel_name="c",kernel_spec_manager=manager,connection_file=str(temp/f"connection-{n}.json"))
  km.start_kernel(cwd=str(ROOT/str(n)),env={**os.environ,"IPYTHONDIR":str(temp/"ipython")})
  kc=km.client();kc.start_channels();kc.wait_for_ready(timeout=30);count=0
  try:
   for i,c in enumerate(raw["cells"]):
    if c["cell_type"]!="code":continue
    tags=c.get("metadata",{}).get("tags",[])
    if "expected-undefined-behavior" in tags or "expected-compile-error" in tags:continue
    if n==1 and i not in W1_GOLDEN:continue
    text="".join(c["source"])
    assert not re.search(r"\b(?:scanf|fgets|gets)\s*\(",stripped(text)),(n,i)
    built,exe=compile_source(text,temp,strict=False)
    assert built.returncode==0,(n,i,built.stderr)
    standalone=run([str(exe)])
    assert standalone.returncode==0,(n,i,standalone.stderr)
    msgid=kc.execute(text,allow_stdin=False)
    stdout="";stderr="";errors=[]
    while True:
     msg=kc.get_iopub_msg(timeout=30)
     if msg.get("parent_header",{}).get("msg_id")!=msgid:continue
     content=msg["content"]
     if msg["msg_type"]=="stream":
      if content["name"]=="stdout":stdout+=content["text"]
      else:stderr+=content["text"]
     if msg["msg_type"]=="error":errors.append(content)
     if msg["msg_type"]=="status" and content["execution_state"]=="idle":break
    # This kernel returns status ok even on GCC errors; inspect stderr as well.
    assert not errors and not stderr,(n,i,errors,stderr)
    assert stdout==standalone.stdout.decode(),(n,i,repr(stdout),repr(standalone.stdout))
    evidence.append({"lecture":n,"cell":i,"id":c.get("id"),"status":"PASS","stdout":stdout});count+=1
   print(f"PASS actual Jupyter C W{n}: {count} safe complete programs",flush=True)
  finally:
   kc.stop_channels();km.shutdown_kernel(now=True);del kc;del km
 print(f"PASS actual Jupyter C total: {len(evidence)}; stdout parity with GCC; no error messages")
 return evidence

def main():
 parser=argparse.ArgumentParser()
 parser.add_argument("--kernel",action="store_true")
 parser.add_argument("--kernel-python",default=sys.executable)
 parser.add_argument("--kernel-evidence",type=Path)
 parser.add_argument("--join-output-threads",action="store_true",
                     help="explicit workaround for the installed jupyter-c-kernel output-reader race")
 parser.add_argument("--lectures",nargs="+",type=int,choices=range(1,6),default=list(range(1,6)))
 args=parser.parse_args()
 docs=structural()
 with tempfile.TemporaryDirectory(prefix="w1_w5_check_") as td:
  temp=Path(td);check_w1(docs[1],temp)
  if args.kernel:
   evidence=kernel_check({n:docs[n] for n in args.lectures},temp,args.kernel_python,args.join_output_threads)
   if args.kernel_evidence:args.kernel_evidence.write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+"\n")

if __name__=="__main__":main()
