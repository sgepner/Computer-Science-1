#!/usr/bin/env python3
"""W2.12: focused notebook audit and complete C11 example regression.

Requires Python 3, GCC and Linux x86-64 reference assumptions for golden output.
Leaves no binaries or saved notebook outputs in the repository.
"""
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
NOTEBOOK = HERE / "Wykład 2.ipynb"

EXPECTED = {
    2: ["a+b=11"],
    9: ["sizeof(int) = 4 B"],
    12: ["CHAR_BIT = 8 bits per byte", "sizeof(char) = 1 B",
         "sizeof(int) = 4 B", "sizeof(long long int) = 8 B",
         "sizeof(float) = 4 B", "sizeof(double) = 8 B",
         "sizeof liczba = 4 B"],
    16: ["a=90, b=10", "after assignment: a=91, b=10"],
    19: ["16 16 16"],
    21: ["20 = 20", "020 = 16", "0x20 = 32"],
    24: ["decimal: 16", "octal:   20", "hex:     10", "HEX:     10"],
    28: ["a=90, b=10, c=40"],
    31: ["INT_MIN = -2147483648", "INT_MAX = 2147483647",
         "UINT_MAX = 4294967295"],
    40: ["przed=4294967295", "po=0"],
    45: ["a=5, b=4", "a+b=9", "a-b=1", "a*b=20"],
    48: ["a/b=0", "b/a=1", "a%b=5", "b%a=1"],
    51: ["-7/3=-2", "-7%3=-1", "7/-3=-2", "7%-3=1"],
    54: ["int:    0", "float:  0.833333", "double: 0.833333"],
    57: ["sizeof(float)  = 4 B", "sizeof(double) = 8 B", "FLT_RADIX = 2",
         "FLT_MANT_DIG = 24", "DBL_MANT_DIG = 53", "FLT_DIG = 6",
         "DBL_DIG = 15"],
    66: ["float:  0.100000001", "double: 0.10000000000000001"],
    69: ["float:  16777216 -> 16777216",
         "double: 16777216 -> 16777217"],
    72: ["a+b=6.00", "a-b=3.00", "a*b=6.75", "a/b=3.00",
         "scientific: 6.022141e+23"],
    75: ["int: 0", "double literal: 0.50", "cast operand: 0.50",
         "cast result: 0.00"],
    78: ["start: a=2, x=6.28", "after double to int: a=6",
         "after int to double: x=6.00"],
    81: ["original: 6.28", "cast to int: 6", "back to double: 6.00"],
    84: ["int: 16777217", "float: 16777216", "double: 16777217"],
    90: ["sizeof(char)=1 B", "CHAR_BIT=8", "symbol=A", "code=65",
         "'B' code=66"],
    93: ["character: 0, code: 48", "numeric zero: 0", "string: 0",
         "string bytes: 2", "NUL code: 0", "newline code: 10"],
    96: ["CHAR_MIN=-128 CHAR_MAX=127", "SCHAR_MIN=-128 SCHAR_MAX=127",
         "UCHAR_MAX=255", "signed char: -1", "unsigned char: 255"],
    100: ["sizeof(bool)=1 B", "gotowe=1", "po zmianie=0"],
    103: ["0 -> 0", "42 -> 1", "-3 -> 1"],
    105: ["a<b=1", "a==b=0", "a!=b=1"],
    108: ["main: poczatek", "Witaj z funkcji przywitaj", "main: koniec"],
    111: ["void: 11", "int: 11"],
    117: ["a+b*c=14", "(a+b)*c=20", "20/5*2=8", "20/(5*2)=2",
          "a+b*c==14: 1"],
    120: ["z nawiasami=2.666667", "bez nawiasow=16.000000"],
    123: ["a++: 3", "++a: 4", "a--: 3", "--a: 2"],
    126: ["prefix: a=2 b=2", "postfix: a=2 b=1"],
    129: ["a+=b: 13", "a-=b: 10", "a*=b: 30", "a/=b: 10", "a%=b: 1"],
}


def run(command, **kwargs):
    return subprocess.run(command, text=True, capture_output=True, timeout=15, **kwargs)


def main():
    assert shutil.which("gcc"), "W2.12 requires GCC"
    nb = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    assert nb["nbformat"] == 4 and nb["metadata"]["kernelspec"]["name"] == "c"
    assert len(nb["cells"]) == 134, len(nb["cells"])
    cs = [(i, c) for i, c in enumerate(nb["cells"]) if c["cell_type"] == "code"]
    assert len(cs) == 37, len(cs)
    assert all(c["execution_count"] is None and c["outputs"] == [] for _, c in cs)
    assert all("".join(c["source"]).strip() for _, c in cs)
    assert nb["cells"][37]["metadata"].get("tags") == ["expected-undefined-behavior"]
    assert nb["cells"][114]["metadata"].get("tags") == ["expected-compile-error"]

    all_good = {i for i, _ in cs} - {37, 114}
    assert len(all_good) == 35
    assert set(EXPECTED) == all_good, (sorted(set(EXPECTED) - all_good),
                                       sorted(all_good - set(EXPECTED)))

    markdown = "\n".join("".join(c["source"]) for c in nb["cells"]
                         if c["cell_type"] == "markdown")
    assert "`dodo`" not in markdown and "```text" not in markdown
    for part in range(1, 12):
        assert f"## W2.{part} —" in markdown, f"Missing section W2.{part}"
    for phrase in ("Co dziś zrobiliśmy?", "Pytania kontrolne", "Co dalej?"):
        assert phrase in markdown, phrase
    chart = "".join(nb["cells"][89]["source"])
    section = chart[chart.index("| Zakres kodów |"):chart.index("**Skróty")]
    assert [int(x) for x in re.findall(r"`(\d{3}) [^`]+`", section)] == list(range(128))
    sub = "".join(nb["cells"][62]["source"])
    assert all(bits in sub for bits in ("00000000000000000000001", "00000000000000000000010"))
    assert "Linux na architekturze x86-64" in "".join(nb["cells"][6]["source"])
    w1 = json.loads((ROOT / "1" / "Wykład 1.ipynb").read_text(encoding="utf-8"))
    assert w1["metadata"]["kernelspec"]["name"] == "c"
    assert all(c["outputs"] == [] and c["execution_count"] is None
               for c in w1["cells"] if c["cell_type"] == "code")

    # Historical teaching materials must not be silently modified.
    for path, sha in (
        ("2/Lecture 2 Examples.ipynb", "a33d1194f814dcf0e74286f908542910c58e74da"),
        ("2/lec2.tex", "a3320348bd4ec4b8279fa453eb1f12413364d6b6"),
        ("1/Wykład 1.ipynb", "38c5b8e4ad0424807d636635162b1d757ed3eb6b"),
    ):
        result = run(["git", "rev-parse", f"HEAD:{path}"], cwd=ROOT)
        assert result.returncode == 0 and result.stdout.strip() == sha, (path, result.stderr)
    print("PASS: structure, metadata, ASCII, W1 consistency and legacy provenance")

    with tempfile.TemporaryDirectory(prefix="check_w2_") as tmp:
        for i, c in cs:
            source = Path(tmp) / f"cell_{i}.c"
            exe = Path(tmp) / f"cell_{i}"
            source.write_text("".join(c["source"]), encoding="utf-8")
            if i == 37:
                # A deliberate signed overflow is undefined behavior: do NOT execute.
                cmd = ["gcc", "-std=c11", "-pedantic", "-fsyntax-only", str(source)]
                p = run(cmd)
                assert p.returncode == 0, (i, p.stderr)
                print("PASS: cell 37 — intentional UB identified, syntax only")
                continue
            if i == 114:
                # Invalid void object: rejection is the expected outcome.
                cmd = ["gcc", "-std=c11", "-pedantic-errors", "-fsyntax-only", str(source)]
                p = run(cmd)
                assert p.returncode != 0 and "declared void" in p.stderr, (i, p.stderr)
                print("PASS: cell 114 — intentional diagnostic")
                continue
            for opt in ("-O0", "-O2"):
                cmd = ["gcc", "-std=c11", opt, "-Wall", "-Wextra", "-pedantic",
                       "-Werror", str(source), "-o", str(exe)]
                built = run(cmd)
                assert built.returncode == 0, (i, opt, built.stderr)
                p = run([str(exe)])
                assert p.returncode == 0, (i, opt, p.stderr)
                lines = p.stdout.strip().splitlines()
                assert lines == EXPECTED[i], (i, opt, lines, EXPECTED[i])
            print(f"PASS: cell {i} — -O0 and -O2")

    print("PASS: W2.12 — 35 valid C programs x 2 = 70 runs; "
          "1 expected UB syntax-only; 1 intentional compile error")


if __name__ == "__main__":
    main()
