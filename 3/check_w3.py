#!/usr/bin/env python3
"""W3: verify notebook structure and compile/run all C examples (GCC C11).

Run from repository root: python3 3/check_w3.py
Golden outputs are specified for Linux/x86-64 with GCC and C locale. This
checks compiled C, not the actual Jupyter C kernel (instructor smoke test).
No repository files are modified; executables go into a temporary directory.
"""
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
NB = HERE / "Wykład 3.ipynb"
SAMPLES = HERE / "samples"

# Code-cell ordinal among C cells, independent of Markdown insertions.
EXPECTED_CELLS = [
    "ABC\nPierwszy printf zapisal 4 znaki.\n",
    "int=-3, double=2.50, char=A\nunsigned=12, hex=c, oct=14\n",
    "|    12|12    |\n|1234567|1234567|\n|+12|-12|\n",
    "|     12.35|\n|1.23e+01|\n|12.35|\n|007|\n",
    "naukowo = 1.001e+03\nduze E  = 1.001E+03\n"
    "15 cyfr = 1.000888800000000e+03\nogolny  = 1000.9\n",
    "numer=00007\nujemny=-0007\nwypelniono 75% zadania\n",
 'wiersz pierwszy\nwiersz drugi\nA\tB\nUkosnik: \\ i cudzyslow: "\n',
    "sscanf zwrocil 1, a=42\n",
    "wynik=2, a=7, b=2.5\n",
    "wynik=0, a=123\n",
    "wynik=1, a=7, b=-1.0\n",
    "wynik=-1, EOF=-1\n",
    "wynik=2, f=1.25, x=2.50\n",
    "r1=1, pierwszy_kod=32\nr2=1, drugi=A\n",
    "Blad danych: oczekiwano int, wynik=0\n",
    "sqrt(9)=3.00\npow(2,3)=8.00\nfabs(-3.5)=3.50\n"
    "floor(2.7)=2.00, ceil(2.7)=3.00\n",
    "exp(2)=7.389056\nlog(exp(2))=2.000000\nlog10(1000)=3.000000\n",
    "pow(5,-3.9)=0.001879\npow(10,2.4)=251.188643\n"
    "exp(x+y)=298.867401\nlog(exp(5))=5.000000\n",
    "pi=3.141593\nsin(pi/2)=1.000000\natan2(1,1)=0.785398\n",
    "cos(0)=1.000000, tan(0)=0.000000\n"
    "asin(0.5)=0.523599, acos(0.5)=1.047198\n"
    "atan(1)=0.785398\n"
    "sinh(0)=0.000000, cosh(0)=1.000000, tanh(0)=0.000000\n",
    "sqrt(9.00)=3.00\n",
    "delta=1.00, x1=2.00, x2=1.00\n",
]

# File, stdin, expected status, expected stdout substrings, expected stderr substrings.
SAMPLE_CASES = [
    ("sterowanie_terminalem.c", "", 0,
     ("ABCDE\rZ\n", "ABCDE\b!\n", "A\vB\n", "apostrof: '\n"), ()),
    ("printf.c", "", 0, ("|    12|12    |", "|      2.50|", "Postep: 75%"), ()),
    ("stdio_terminal.c", "", 0, ("ABC\n", "printf zapisal 4 znaki"), ("komunikat na stderr",)),
    ("scanf_stany.c", "7 2.5\n", 0, ("scanf zwrocil 2", "Pierwsze pole: 7", "Drugie pole: 2.50"), ()),
    ("scanf_stany.c", "7 kot\n", 1, ("scanf zwrocil 1", "Pierwsze pole: 7", "Nie udalo"), ()),
    ("scanf_stany.c", "kot\n", 1, ("scanf zwrocil 0", "Nie udalo"), ()),
    ("scanf_stany.c", "", 1, ("scanf zwrocil -1", "Koniec wejscia (EOF)"), ()),
    ("scanf.c", "7 2.5\n", 0, ("a=7, b=2.50",), ()),
    ("scanf.c", "7 kot\n", 1, (), ("przypisano tylko 1 z 2 pol",)),
    ("scanf.c", "kot\n", 1, (), ("przypisano tylko 0 z 2 pol",)),
    ("scanf.c", "", 1, (), ("EOF",)),
    ("math.c", "0\n", 0, ("sin(0.00)=0.000000", "cos(0.00)=1.000000"), ()),
    ("math.c", "kot\n", 1, (), ("oczekiwano liczby",)),
    ("pow.c", "2\n", 0, ("x^2=4.000", "pow(x,2.31)="), ()),
    ("pow.c", "-2\n", 1, (), ("podstawa musi byc nieujemna",)),
    ("logs.c", "10\n", 0, ("log(10.00)=2.302585", "log10(10.00)=1.000000"), ()),
    ("logs.c", "-5\n", 1, (), ("argument logarytmu musi byc dodatni",)),
    ("logs.c", "nan\n", 1, (), ("argument logarytmu musi byc dodatni",)),
    ("pole_kola.c", "2\n", 0, ("Promien: 2.00", "Obwod: 12.57", "Pole: 12.57"), ()),
    ("pole_kola.c", "-2\n", 1, (), ("promien musi byc dodatni",)),
    ("pole_kola.c", "kot\n", 1, (), ("oczekiwano liczby",)),
    ("pole_kola.c", "", 1, (), ("brak danych (EOF)",)),
    ("pole_kola.c", "nan\n", 1, (), ("promien musi byc dodatni",)),
]


def run(argv, **kwargs):
    env = {**os.environ, "LC_ALL": "C"}
    return subprocess.run(argv, input=kwargs.pop("input", None),
                          capture_output=True, text=True, timeout=10,
                          env=env, **kwargs)


def compile_program(source, executable, optimization):
    command = ["gcc", "-std=c11", optimization, "-Wall", "-Wextra",
               "-Werror", "-pedantic", str(source), "-o", str(executable), "-lm"]
    result = run(command)
    assert result.returncode == 0, (
        f"C11 compilation failed for {source} [{optimization}]\n{result.stderr}")


def main():
    assert shutil.which("gcc"), "Requires GCC"
    doc = json.loads(NB.read_text(encoding="utf-8"))
    assert doc["nbformat"] == 4
    assert doc["metadata"]["kernelspec"]["name"] == "c"
    assert doc["metadata"]["kernelspec"]["language"] == "c"
    cells = doc["cells"]
    code_cells = [c for c in cells if c["cell_type"] == "code"]
    assert len(code_cells) == len(EXPECTED_CELLS) == 22
    assert all(c["execution_count"] is None and c["outputs"] == [] for c in code_cells)
    assert all("int main(void)" in "".join(c["source"]) for c in code_cells)
    assert all(not re.search(r"(?<!s)\bscanf\s*\(", "".join(c["source"]))
               for c in code_cells), "Interactive scanf in notebook code cell"
    markdown = "\n".join("".join(c["source"]) for c in cells
                         if c["cell_type"] == "markdown")
    for section in range(10):
        assert f"## W3.{section} —" in markdown, f"Missing W3.{section}"
    for item in ("stdout", "stderr", "EOF", "sscanf", "//%cflags:-lm",
                 "niezależnej konsoli", "W2", "W4", "dziedzin", "-lm"):
        assert item in markdown, f"Missing teaching point: {item}"
    # Protect the recovered historical topics, especially the lecturer's raptor joke.
    for phrase in ("He forgot about the `&`!!", "scanf_perils.png",
                   "scanf(\"%d\", a)", "pow(5.0, -3.9)",
                   "asin(x)", "sinh(x)", "numer albumu",
                   "\\Delta", "od -An -t x1"):
        assert phrase in markdown, f"Missing recovered W3 topic: {phrase}"
    assert len(EXPECTED_CELLS) == 22
    assert len(SAMPLE_CASES) == 23
    for filename in sorted(set(row[0] for row in SAMPLE_CASES)):
        assert (SAMPLES / filename).exists(), filename
    print(f"PASS: notebook JSON, C kernel, {len(cells)} cells, "
          f"{len(code_cells)} clean C cells, W3.0-W3.9, no interactive code input")

    program_runs = 0
    sample_runs = 0
    with tempfile.TemporaryDirectory(prefix="check_w3_") as tempdir:
        temp = Path(tempdir)
        for ordinal, cell in enumerate(code_cells):
            source = temp / f"cell_{ordinal}.c"
            source.write_text("".join(cell["source"]), encoding="utf-8")
            executable = temp / f"cell_{ordinal}"
            for optimization in ("-O0", "-O2"):
                compile_program(source, executable, optimization)
                result = run([str(executable)])
                assert result.returncode == 0 and result.stderr == "", (
                    ordinal, optimization, result.returncode, result.stderr)
                assert result.stdout == EXPECTED_CELLS[ordinal], (
                    ordinal, optimization, repr(result.stdout),
                    repr(EXPECTED_CELLS[ordinal]))
                program_runs += 1
            print(f"PASS: notebook C cell {ordinal+1:02d}/22 x -O0,-O2")

        for name in sorted(set(row[0] for row in SAMPLE_CASES)):
            executable = temp / Path(name).stem
            for optimization in ("-O0", "-O2"):
                compile_program(SAMPLES / name, executable, optimization)
                cases = [row for row in SAMPLE_CASES if row[0] == name]
                for _, stdin, code, expected_stdout, expected_stderr in cases:
                    result = run([str(executable)], input=stdin)
                    assert result.returncode == code, (
                        name, optimization, repr(stdin), result.returncode,
                        result.stdout, result.stderr)
                    assert all(part in result.stdout for part in expected_stdout), (
                        name, optimization, repr(stdin), repr(result.stdout), expected_stdout)
                    assert all(part in result.stderr for part in expected_stderr), (
                        name, optimization, repr(stdin), repr(result.stderr), expected_stderr)
                    sample_runs += 1
            print(f"PASS: {name}, {len(cases)} fixtures x -O0,-O2")

    print(f"PASS: W3 C11 — {program_runs} notebook runs + "
          f"{sample_runs} console fixture runs; no generated artifacts in repo")


if __name__ == "__main__":
    main()
