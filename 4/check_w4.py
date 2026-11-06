#!/usr/bin/env python3
"""Compile exact W4 notebook programs and check semantics; no notebook mutation.
Run: python3 4/check_w4.py --if-only (CP3), or without flag after CP4.
GCC C11 tests do not replace the separate actual Jupyter C kernel check.
"""
import argparse
import json
import math
import os
from pathlib import Path
import re
import subprocess
import tempfile
import nbformat

HERE = Path(__file__).resolve().parent
NB = HERE / "Wykład 4.ipynb"
EXPECTED = {
    "61d45c4a": "Przed warunkiem\nx jest ujemne\nPo warunku\n",
    "w4-if-single": "B\nKoniec\n",
    "w4-if-block": "Koniec\n",
    "w4-if-empty": "Blok wykonany\n",
    "w4-scope-block": "w bloku a=30 b=20\npo bloku a=10\n",
    "4bfe372e": "x=7, w_przedziale=1\n",
    "2e32f995": "p q AND OR NOT_p\n0 0  0   0   1\n0 1  0   1   1\n1 0  0   1   0\n1 1  1   1   0\n-2 && 7 = 1, -2 || 0 = 1, !(-2) = 0\n",
    "ae30e57f": "x=11, w=0, !w=1, poza=1\n",
    "1a2c80e2": "p || (q && r) = 1\n(p || q) && r = 0\n",
    "ebedf0a8": "0 && P: 0\nObliczam prawy operand\n1 && P: 1\n1 || P: 1\nObliczam prawy operand\n0 || P: 0\n",
    "7c7e8639": "mianownik=0, wynik=0\n",
    "w4-branch-blocks": "dodatni\nwewnatrz bloku\npo decyzji\n",
    "w4-branch-independent-chain": "A\nB\nC\n---\ndodatnie\n",
    "w4-branch-nested-else": "else nalezy do wewnetrznego if\n",
    "w4-branch-assignment": "warunek prawdziwy\na=7\n",
    "dd027695-8bf4-47cb-85da-bf44f5163516": "17\n",
    "373cbd16-59af-4dde-93fd-4d423a66de4c": "17\n",
    "44960722-9222-433e-8af8-0b53ec184a3b": "This is the second case\n",
    "b19c4849-ad7f-41c8-b464-181c394837b7": "This is the first case\n",
    "w4-functions-value-scope": "lokalna=5\npo wywolaniu=4\n",
    "w4-int3-global-shadow": "funkcja: x=15\nmain: x=100\n",
    # Removed when the terminal A/B versions replace this legacy parser in CP4.
    "w4-quadratic-decision-tree": "dwa x1=2.0 x2=1.0\n",
}

def run(argv, data=""):
    return subprocess.run(argv, input=data, capture_output=True, text=True,
                          timeout=5, env={**os.environ, "LC_ALL": "C"})

def build(text, temp, opt="-O0", warnings=False, expected_error=None):
    source = temp / "p.c"; exe = temp / "p"
    source.write_text(text)
    flags = ["gcc", "-std=c11", opt, "-Wall", "-Wextra", "-pedantic"]
    if not warnings: flags += ["-Werror"]
    result = run(flags + [str(source), "-o", str(exe), "-lm"])
    if expected_error is not None:
        assert result.returncode != 0 and expected_error in result.stderr, result.stderr
        return None
    assert result.returncode == 0, result.stderr
    if warnings: assert "empty body" in result.stderr, result.stderr
    else: assert result.stderr == "", result.stderr
    return exe

def fences(cell):
    return re.findall(r"```c\n(.*?)```", "".join(cell["source"]), re.S)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--if-only", action="store_true")
    args = parser.parse_args()
    raw = json.loads(NB.read_text())
    nbformat.validate(nbformat.from_dict(raw))
    assert raw["metadata"]["kernelspec"]["name"] == "c"
    cells = {c["id"]: c for c in raw["cells"]}
    count = 0
    with tempfile.TemporaryDirectory(prefix="w4_check_") as td:
        temp = Path(td)
        for id, cell in cells.items():
            if cell["cell_type"] != "code": continue
            assert id in EXPECTED, f"Missing independent expected result for {id}"
            assert cell["outputs"] == [] and cell["execution_count"] is None
            for opt in ("-O0", "-O2"):
                exe = build("".join(cell["source"]), temp, opt, warnings=id=="w4-if-empty")
                result = run([str(exe)])
                assert (result.returncode, result.stdout, result.stderr)==(0,EXPECTED[id],""),(id,opt,result)
                count += 1
        # Controlled pairs: exactly the sign of x changes in the same program.
        for id in ("w4-if-single", "w4-if-block", "w4-if-empty"):
            for opt in ("-O0", "-O2"):
                text = "".join(cells[id]["source"]).replace("x = -3","x = 3")
                exe = build(text,temp,opt,warnings=id=="w4-if-empty")
                result = run([str(exe)])
                expected = "Blok wykonany\n" if id=="w4-if-empty" else "A\nB\nKoniec\n"
                assert (result.returncode,result.stdout)==(0,expected),(id,result)
                count += 1
        bad = fences(cells["w4-scope-expected-fail"])
        assert len(bad)==1
        build(bad[0],temp,expected_error="undeclared")
        # Same dangling-else source as printed, all a/b combinations.
        dangling = fences(cells["w4-dangling-else-note"])[0]
        for a,b,expected in ((0,0,""),(0,1,""),(1,0,"a prawdziwe, b falszywe\n"),(1,1,"oba prawdziwe\n")):
            text = '#include <stdio.h>\nint main(void) {\nint a=%d,b=%d;\n'%(a,b)+dangling+'\nreturn 0;}\n'
            source=temp/"dangling.c";exe=temp/"dangling";source.write_text(text)
            comp=run(["gcc","-std=c11","-Wall","-Wextra","-pedantic",str(source),"-o",str(exe)])
            assert comp.returncode==0 and "dangling-else" in comp.stderr,comp.stderr
            assert run([str(exe)]).stdout==expected
            count+=1
        # De Morgan and short-circuit safeguards on multiple boundary values.
        for x in (-1,0,10,11):
            text=''.join(cells["ae30e57f"]["source"]).replace("x = 11",f"x = {x}")
            expected=int(0<=x<=10)
            assert run([str(build(text,temp))]).stdout==f"x={x}, w={expected}, !w={1-expected}, poza={1-expected}\n"
        for den,value in ((0,0),(2,1),(5,0)):
            text=''.join(cells["7c7e8639"]["source"]).replace("mianownik = 0",f"mianownik = {den}")
            assert run([str(build(text,temp))]).stdout==f"mianownik={den}, wynik={value}\n"
        print(f"PASS W4 IF: {count} golden/controlled runs + 7 logical boundary runs; scope EXPECTED-FAIL; warnings explicit")
        if not args.if_only:
            raise AssertionError("CP4 A/B verification not implemented yet")
    print("PASS W4 structure, no saved outputs, C11 -Wall -Wextra -pedantic, O0/O2")

if __name__ == "__main__":
    main()
