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
    "|    12|12    |\n|1234567|1234567|\n|   +12|-12   |\n",
    "|     12.35|\n|1.23e+01|\n|12.35|\n|007|\n",
    "naukowo = 1.001e+03\nduze E  = 1.001E+03\n"
    "15 cyfr = 1.000888800000000e+03\nogolny  = 1000.9\n",
    "  007\nnumer=00007\nujemny=-0007\nwypelniono 75% zadania\n",
 'wiersz pierwszy\nwiersz drugi\nA\tB\nUkosnik: \\ i cudzyslow: "\n',
    "sscanf zwrocil 1, a=42\n",
    "wynik=2, a=7, b=2.5\n",
    "wynik=0, a=123\n",
    "wynik=1, a=7, b=-1.0\n",
    "wynik=-1, EOF=-1\n",
    "wynik=2, f=1.25, x=2.50\n",
    "r1=1, pierwszy_kod=32, znak=[ ]\nr2=1, drugi_kod=65, znak=[A]\n",
    "Blad danych: oczekiwano int, wynik=0\n",
    "sqrt(9)=3.00\npow(2,3)=8.000\nabs(-3)=3\nfabs(-3.5)=3.50\n"
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
]

# Existing notebook additions, in source order.
EXPECTED_CELLS.insert(1, "a=3, b=31400000000.000000\na=3, b=3.14e+10\n")
EXPECTED_CELLS.insert(8, "ABCDE\rZ\nABCDE\b!\nA\vB\napostrof: '\n")
EXPECTED_CELLS.insert(17, "AB\nCD\nE\n\n")

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
    data = kwargs.pop("input", None)
    result = subprocess.run(argv, input=None if data is None else data.encode(),
                            capture_output=True, timeout=10, env=env, **kwargs)
    # Preserve CR/backspace bytes; text=True would silently normalize CR.
    result.stdout = result.stdout.decode()
    result.stderr = result.stderr.decode()
    return result


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
    assert len(code_cells) == len(EXPECTED_CELLS) == 24
    assert all(c["execution_count"] is None and c["outputs"] == [] for c in code_cells)
    assert all("int main(void)" in "".join(c["source"]) for c in code_cells)
    assert all(not re.search(r"\bscanf\s*\(", re.sub(r"//[^\n]*|/\*.*?\*/", "", "".join(c["source"]), flags=re.S))
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
                   "od -An -t x1"):
        assert phrase in markdown + "\n".join("".join(c["source"]) for c in code_cells), f"Missing recovered W3 topic: {phrase}"
    # The quadratic case study belongs to W4 in the current approved course.
    quadratic = json.loads((HERE.parent / "4" / "Wykład 4.ipynb").read_text())
    assert "delta" in "\n".join("".join(c["source"]) for c in quadratic["cells"])
    assert len(EXPECTED_CELLS) == 24
    assert len(SAMPLE_CASES) == 23
    for filename in sorted(set(row[0] for row in SAMPLE_CASES)):
        assert (SAMPLES / filename).exists(), filename
    print(f"PASS: notebook JSON, C kernel, {len(cells)} cells, "
          f"{len(code_cells)} clean C cells, W3.0-W3.9, no interactive code input")

    assert not any(re.search(r"(?<![A-Za-z_])gets\s*\(", "".join(c["source"]))
                   for c in code_cells), "Never execute gets"
    for phrase in ("puts", "fputs", "fgets", "NULL", "C11", "N−1"):
        assert phrase in markdown, phrase
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
            print(f"PASS: notebook C cell {ordinal+1:02d}/24 x -O0,-O2")

        # Compile the exact terminal-only fgets program printed in the notebook.
        io_cell = next(c for c in cells if c.get("id") == "w3-io-fgets")
        fences = re.findall(r"```c\n(.*?)```", "".join(io_cell["source"]), re.S)
        assert len(fences) == 1
        source = temp / "fgets.c"
        source.write_text(fences[0])
        fixtures = [
            ("kot\n", 0, "1:[kot\n]\nBrak drugiego odczytu\n"),
            ("123456\n", 0, "1:[123456\n]\nBrak drugiego odczytu\n"),
            ("1234567\n", 0, "1:[1234567]\n2:[\n]\n"),
            ("123456789\n", 0, "1:[1234567]\n2:[89\n]\n"),
            ("", 1, "Brak pierwszego odczytu\n"),
            ("abc", 0, "1:[abc]\nBrak drugiego odczytu\n"),
            ("1234567", 0, "1:[1234567]\nBrak drugiego odczytu\n"),
            ("\n", 0, "1:[\n]\nBrak drugiego odczytu\n"),
        ]
        for opt in ("-O0", "-O2"):
            exe = temp / "fgets"
            compile_program(source, exe, opt)
            for data, status, output in fixtures:
                result = run([str(exe)], input=data)
                assert (result.returncode, result.stdout, result.stderr) == (status, output, ""), (
                    opt, repr(data), result)
        print("PASS: fgets exact notebook program: 8 boundary/EOF fixtures x -O0,-O2")

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
