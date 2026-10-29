#!/usr/bin/env python3
"""Testy W4.2: GCC C11, -O0/-O2, wejścia brzegowe."""
import json
import subprocess
import tempfile
from pathlib import Path

nb = json.loads(Path(__file__).with_name("Wykład 4.ipynb").read_text(encoding="utf-8"))
assert nb["metadata"]["kernelspec"]["name"] == "c"

programy = []
for komorka in nb["cells"]:
    tekst = "".join(komorka["source"])
    if komorka["cell_type"] == "markdown" and tekst.startswith("## W4.4"):
        break
    if komorka["cell_type"] == "code":
        programy.append(tekst)
assert len(programy) == 7, f"Oczekiwano 7 programow, znaleziono {len(programy)}"

# Regresja tabeli Markdown: surowy `||` w komorce tabeli rozbija kolumny.
tabele = [
    "".join(cell["source"])
    for cell in nb["cells"]
    if cell["cell_type"] == "markdown"
    and "— tabela prawdy" in "".join(cell["source"])
]
assert len(tabele) == 1
wiersze = [w for w in tabele[0].splitlines() if w.startswith("|")]
assert len(wiersze) == 6, f"Oczekiwano 6 linii tabeli: {wiersze}"
assert wiersze[0] == "| p | q | AND | OR | NOT p |"
assert all(w.count("|") == 6 for w in wiersze), "Nadmiarowe separatory tabeli"


wyniki = [
    "Przed warunkiem\nx jest ujemne\nPo warunku\n",
    "x=7, w_przedziale=1\n",
    "p q AND OR NOT_p\n0 0  0   0   1\n0 1  0   1   1\n"
    "1 0  0   1   0\n1 1  1   1   0\n"
    "-2 && 7 = 1, -2 || 0 = 1, !(-2) = 0\n",
    "x=11, w=0, !w=1, poza=1\n",
    "p || (q && r) = 1\n(p || q) && r = 0\n",
    "0 && P: 0\nObliczam prawy operand\n1 && P: 1\n"
    "1 || P: 1\nObliczam prawy operand\n0 || P: 0\n",
    "mianownik=0, wynik=0\n",
]
warianty = [
    (1, "int x = 7;", "int x = -1;", "x=-1, w_przedziale=0\n"),
    (1, "int x = 7;", "int x = 0;", "x=0, w_przedziale=1\n"),
    (1, "int x = 7;", "int x = 10;", "x=10, w_przedziale=1\n"),
    (1, "int x = 7;", "int x = 11;", "x=11, w_przedziale=0\n"),
    (3, "int x = 11;", "int x = -1;", "x=-1, w=0, !w=1, poza=1\n"),
    (3, "int x = 11;", "int x = 0;", "x=0, w=1, !w=0, poza=0\n"),
    (3, "int x = 11;", "int x = 10;", "x=10, w=1, !w=0, poza=0\n"),
    (6, "mianownik = 0;", "mianownik = 2;", "mianownik=2, wynik=1\n"),
    (6, "mianownik = 0;", "mianownik = 5;", "mianownik=5, wynik=0\n"),
]

with tempfile.TemporaryDirectory(prefix="w4_logic_") as tmp:
    source = Path(tmp) / "program.c"
    executable = Path(tmp) / "program"

    def uruchom(kod, opt):
        source.write_text(kod, encoding="utf-8")
        subprocess.run(
            ["gcc", "-std=c11", "-Wall", "-Wextra", "-Werror",
             "-pedantic", opt, str(source), "-o", str(executable)],
            check=True, capture_output=True, text=True,
        )
        return subprocess.run(
            [str(executable)], check=True, capture_output=True,
            text=True, timeout=5,
        ).stdout

    for opt in ("-O0", "-O2"):
        for i, kod in enumerate(programy):
            got = uruchom(kod, opt)
            assert got == wyniki[i], (i, opt, got, wyniki[i])

    for i, stary, nowy, expected in warianty:
        assert stary in programy[i], (i, stary)
        got = uruchom(programy[i].replace(stary, nowy), "-O2")
        assert got == expected, (i, stary, nowy, got, expected)

print("W4.2 PASS: 7 komorek x 2 optymalizacje + 9 wariantow = 23 uruchomienia")
