#!/usr/bin/env python3
"""W4.3: if, else if, ?:, switch; GCC C11 / O0 + O2."""
import json
import subprocess
import tempfile
from pathlib import Path

path = Path(__file__).with_name("Wykład 4.ipynb")
nb = json.loads(path.read_text(encoding="utf-8"))
assert nb["metadata"]["kernelspec"]["name"] == "c"
programs = []
inside = False
for cell in nb["cells"]:
    content = "".join(cell["source"])
    if cell["cell_type"] == "markdown" and content.startswith("## W4.4"):
        inside = True
    if cell["cell_type"] == "markdown" and content.startswith("## W4.7"):
        break
    if inside and cell["cell_type"] == "code":
        assert not cell["outputs"], "W4.3 has saved outputs"
        programs.append(content)
assert len(programs) == 7, f"Expected 7 W4.3 C examples, got {len(programs)}"
assert "if (a = 7)" in programs[3] and "/* fall through */" in programs[6]

expected = [
    "ujemne\ndruga instrukcja bloku\nkoniec\n",
    "Niezalezne if:\nrowne\na >= b\na <= b\nLancuch else if:\nrowne\n",
    "a > 0 i b <= 0\n",
    "warunek prawdziwy\na=7\n",
    "if=17, operator=17\n",
    "dwa\n",
    "dwa\ntrzy\n",
]
variants = [
    (0, "int a = -1;", "int a = 1;", "dodatnie\nkoniec\n"),
    (0, "int a = -1;", "int a = 0;", "koniec\n"),
    (1, "int a = 5, b = 5;", "int a = 7, b = 5;",
     "Niezalezne if:\na >= b\nLancuch else if:\na > b\n"),
    (1, "int a = 5, b = 5;", "int a = 3, b = 5;",
     "Niezalezne if:\na <= b\nLancuch else if:\na < b\n"),
    (2, "int a = 2, b = 0;", "int a = 2, b = 1;", "a > 0 i b > 0\n"),
    (2, "int a = 2, b = 0;", "int a = -2, b = 0;", "a <= 0\n"),
    (4, "int a = 10, b = 5, c = 7;", "int a = 10, b = 9, c = 7;",
     "if=19, operator=19\n"),
    (4, "int a = 10, b = 5, c = 7;", "int a = 10, b = 7, c = 7;",
     "if=17, operator=17\n"),
    (5, "int kod = 2;", "int kod = 1;", "jeden\n"),
    (5, "int kod = 2;", "int kod = 3;", "trzy\n"),
    (5, "int kod = 2;", "int kod = 8;", "inny kod\n"),
    (6, "int kod = 2;", "int kod = 1;", "jeden\n"),
    (6, "int kod = 2;", "int kod = 3;", "trzy\n"),
    (6, "int kod = 2;", "int kod = 8;", "inny kod\n"),
]

with tempfile.TemporaryDirectory(prefix="w43_") as directory:
    src = Path(directory) / "case.c"
    exe = Path(directory) / "case"

    def run(source, optimization, assignment):
        src.write_text(source, encoding="utf-8")
        base = ["gcc", "-std=c11", "-Wall", "-Wextra",
                "-Werror", "-pedantic", optimization]
        flags = base + (["-Wno-error=parentheses"] if assignment else [])
        result = subprocess.run(
            flags + [str(src), "-o", str(exe)],
            capture_output=True, text=True,
        )
        assert result.returncode == 0, result.stderr
        if assignment:
            assert "-Wparentheses" in result.stderr, "Assignment warning missing"
            strict = subprocess.run(
                base + [str(src), "-o", str(exe)],
                capture_output=True, text=True,
            )
            assert strict.returncode != 0 and "-Werror=parentheses" in strict.stderr
        result = subprocess.run(
            [str(exe)], check=True, capture_output=True, text=True, timeout=5,
        )
        return result.stdout

    for opt in ("-O0", "-O2"):
        for i, program in enumerate(programs):
            output = run(program, opt, i == 3)
            assert output == expected[i], (opt, i, output, expected[i])
    for i, before, after, answer in variants:
        assert before in programs[i], (i, before)
        output = run(programs[i].replace(before, after), "-O2", i == 3)
        assert output == answer, (i, before, after, output, answer)

print("W4.3 PASS: 7 programs x 2 optimizations + 14 variants = 28 runs")
