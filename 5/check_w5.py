#!/usr/bin/env python3
"""W5 regression: Python stdlib + GCC. Temporary binaries are always removed.

Run from any directory. Optional Jupyter smoke is reported separately.
Numerical checks use absolute tolerance 1e-12 for small, documented arguments.
"""
import importlib.util
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
ENV = dict(os.environ, LC_ALL="C")
FLAGS = ["-std=c11", "-Wall", "-Wextra", "-Werror", "-pedantic"]
# Independent regression baselines, reviewed against the teaching narrative.
EXPECTED = {'goto': '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n24\n25\n26\n27\n28\n29\n30\n31\n32\n33\n34\n35\n36\n37\n38\n39\n40\n41\n42\n43\n44\n45\n46\n47\n48\n49\n50\n51\n52\n53\n54\n55\n56\n57\n58\n59\n60\n61\n62\n63\n64\n65\n66\n67\n68\n69\n70\n71\n72\n73\n74\n75\n76\n77\n78\n79\n80\n81\n82\n83\n84\n85\n86\n87\n88\n89\n90\n91\n92\n93\n94\n95\n96\n97\n98\n99\n100\n', 'while_limits': '| limit=0 i=0\n0 | limit=1 i=1\n0 1 2 3 4 5 6 7 8 9 | limit=10 i=10\n', 'do_false': 'while=100 do=101\n', 'for_trace': 'init\ntest 0\nbody 0\nupdate\ntest 1\nbody 1\nupdate\ntest 2\nkoniec 2\n', 'for_empty': '0 1 2 \n', 'bounds': '< : n=10 i=10\n<=: n=11 i=11\n10 8 6 4 2 0 | i=-2\n', 'increments': '0 1 2 \n1 2 3 \n', 'scope': 'wewnatrz=0 wewnatrz=1 po=7 globalna=20\nj=3\n', 'float_grid': '0 0.000\n1 0.100\n2 0.200\n3 0.300\n4 0.400\n5 0.500\n6 0.600\n7 0.700\n8 0.800\n9 0.900\n10 1.000\n', 'grid': '0 1 2 3 4\n1 2 3 4 5\n2 3 4 5 6\n3 4 5 6 7\nelementow=20\n', 'control': '0 1 2 3 4 | break i=5\n0 1 2 3 4 6 7 8 9 | continue i=10\n', 'while_continue': '0 1 2 3 4 6 7 8 9 | i=10\n', 'nested_control': '(0,1) wiersz\n(1,0) wiersz\n', 'bounded': 'proby=3\n', 'fib': '0 1 1 2 3 5 8 13 21 34\n', 'game': 'My is greater I win!! 7 8\nYou cheat, I win!!\nBlad danych\n', 'fourier': '-1.00 -0.000000\n-0.75 -0.991777\n-0.50 -1.063054\n-0.25 -0.991777\n0.00 0.000000\n0.25 0.991777\n0.50 1.063054\n0.75 0.991777\n1.00 0.000000\n', 'primes': '2 3 5 7 11 13 17 19 23 29 \n'}


def run(args, data="", timeout=15):
    return subprocess.run(args, input=data, text=True, capture_output=True,
                          timeout=timeout, env=ENV)


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def compile_c(source, opt, scratch, fail=False):
    src, exe = scratch / "case.c", scratch / "case"
    src.write_text(source)
    r = run(["gcc", *FLAGS, opt, str(src), "-o", str(exe), "-lm"])
    if fail:
        require(r.returncode != 0, "EXPECTED FAIL unexpectedly compiled")
        require("undeclared" in r.stderr and "'i'" in r.stderr and "'j'" in r.stderr,
                "scope failure must reject both i and j: " + r.stderr)
        return
    require(r.returncode == 0, "compilation failed:\n" + r.stderr)
    return exe


def execute(source, output, opt, scratch, data="", status=0, stderr=""):
    exe = compile_c(source, opt, scratch)
    r = run([str(exe)], data, timeout=2)
    require((r.returncode, r.stdout, r.stderr) == (status, output, stderr),
            f"execution mismatch ({opt}): {r.returncode=} {r.stdout=} {r.stderr=} expected={output!r}")


def kernel_smoke(scratch):
    os.environ.setdefault("IPYTHONDIR", str(scratch / "ipython"))
    try:
        from jupyter_client.kernelspec import KernelSpecManager
    except ImportError:
        print("OPTIONAL SKIP: jupyter_client unavailable; GCC checks remain applicable")
        return
    specs = KernelSpecManager().find_kernel_specs()
    if "c" not in specs:
        print("OPTIONAL SKIP: C kernelspec unavailable")
        return
    spec = KernelSpecManager().get_kernel_spec("c")
    # Detect the installed but unusable specification in this environment.
    if "jupyter_c_kernel" in spec.argv and importlib.util.find_spec("jupyter_c_kernel") is None:
        r = run([sys.executable, "-m", "jupyter_c_kernel", "--help"])
        require(r.returncode != 0, "kernel availability detection inconsistent")
        print("OPTIONAL UNAVAILABLE: C spec exists, module missing: " + r.stderr.strip())
        return
    from jupyter_client import KernelManager
    km = KernelManager(kernel_name="c", connection_file=str(scratch / "kernel.json"))
    client = None
    try:
        km.start_kernel(cwd=str(scratch), env=dict(ENV, IPYTHONDIR=str(scratch / "ipython")))
        client = km.client()
        client.start_channels()
        client.wait_for_ready(timeout=15)
        ident = client.execute('#include <stdio.h>\nint main(void){puts("W5 kernel OK");return 0;}')
        output = ""
        while True:
            msg = client.get_iopub_msg(timeout=15)
            if msg.get("parent_header", {}).get("msg_id") != ident:
                continue
            require(msg["msg_type"] != "error", "C kernel error: " + repr(msg["content"]))
            if msg["msg_type"] == "stream":
                output += msg["content"]["text"]
            if msg["msg_type"] == "status" and msg["content"]["execution_state"] == "idle":
                break
        require("W5 kernel OK" in output, "kernel smoke output missing: " + output)
        print("PASS optional C kernel smoke")
    finally:
        if client is not None:
            client.stop_channels()
        if km.has_kernel:
            km.shutdown_kernel(now=True)


def main():
    doc = json.loads((ROOT / "Wykład 5.ipynb").read_text())
    require(doc["metadata"]["kernelspec"] == {"name": "c", "language": "c", "display_name": "C"}, "C kernel metadata")
    text = "\n".join("".join(c["source"]) for c in doc["cells"] if c["cell_type"] == "markdown")
    markers = re.findall(r"^## W5\.(\d) —", text, re.M)
    require(markers == list("012345678"), "missing, reordered or duplicated sections")
    require(not re.search(r"Czas na sali|trasa 105 minut|Quiz na 5 minut", text, re.I),
            "teaching notebook must be organized by narrative, not minute allocations")
    images = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text) + re.findall(r'<img[^>]+src="([^"]+)"', text)
    require(len(images) >= 9, "required diagrams/animation missing")
    for image in images:
        require(not re.match(r"[a-z]+:|/", image), "nonlocal image " + image)
        require((ROOT / image).is_file(), "missing image " + image)
    require("goto.png" in images and "XKCD #292" in text, "XKCD attribution and figure")
    require("Fourier_series_for_square_wave.gif" in images and "something-5.png" in images, "animation/static fallback")
    codes = {}
    for cell in doc["cells"]:
        if cell["cell_type"] != "code":
            continue
        require(cell.get("outputs") == [] and cell.get("execution_count") is None, "saved execution products")
        source = "".join(cell["source"])
        require(not re.search(r"(?<![a-zA-Z_])scanf\s*\(", source), "interactive scanf in notebook")
        require("main(" in source, "incomplete translation unit")
        name = cell["metadata"]["w5"]["name"]
        require(name not in codes, "duplicate program id " + name)
        require(cell["metadata"]["w5"]["stdout"] == EXPECTED[name], "notebook expected output drift: " + name)
        codes[name] = source
    require(set(codes) == set(EXPECTED), "uncovered ordinary code cells")
    scope_text = next("".join(c["source"]) for c in doc["cells"] if "EXPECTED FAIL" in "".join(c["source"]))
    scope_fail = re.search(r"```c\n(.*?)```", scope_text, re.S).group(1)
    game = (ROOT / "samples/gra_w5.c").read_text()
    prompt = "Give me a value that is not greater than 10\n"
    console = [
        ("", 0, prompt + "Koniec wejscia\n", ""),
        ("0\n", 0, prompt + "My is greater I win!!\n0 1\n" + prompt + "Koniec wejscia\n", ""),
        ("11\n", 0, prompt + "You cheat, I win!!\n", ""),
        ("kot\n", 1, prompt, "Blad danych\n"),
        ("7x\n", 1, prompt, "Blad danych\n"),
        ("7 8\n", 1, prompt, "Blad danych\n"),
        ("\n", 1, prompt, "Blad danych\n"),
        ("999999999999999999999999999999\n", 1, prompt, "Blad danych\n"),
        ("1" * 200 + "\n", 1, prompt, "Za dlugi wiersz\n"),
        ("10\n" * 5, 0, (prompt + "My is greater I win!!\n10 11\n") * 5 + "Koniec 5 tur\n", ""),
        (" -2 \n11\n", 0, prompt + "My is greater I win!!\n-2 -1\n" + prompt + "You cheat, I win!!\n", ""),
        ("7", 0, prompt + "My is greater I win!!\n7 8\n" + prompt + "Koniec wejscia\n", ""),
    ]
    variants = []
    for limit in [0, 1, 10, 11]:
        variants.append((codes["while_limits"].replace("proba(0);\n    proba(1);\n    proba(10);", f"proba({limit});"),
                         "".join(f"{i} " for i in range(limit)) + f"| limit={limit} i={limit}\n"))
        trace = "init\n" + "".join(f"test {i}\nbody {i}\nupdate\n" for i in range(limit)) + f"test {limit}\nkoniec {limit}\n"
        variants.append((codes["for_trace"].replace("i < 2", f"i < {limit}"), trace))
    variants.extend([
        (codes["do_false"].replace("a = 100, b = 100", "a = 9, b = 9"), "while=10 do=10\n"),
        (codes["float_grid"].replace("n = 11", "n = 6"), "".join(f"{i} {i / 5:.3f}\n" for i in range(6))),
        (codes["scope"].replace("for (int i = 0", "for (i = 0"), "wewnatrz=0 wewnatrz=1 po=2 globalna=20\nj=3\n"),
        (codes["primes"].replace("n < 30", "n < 10"), "2 3 5 7 \n"),
    ])
    quiz_heading = "### Sprawdź, czy potrafisz przewidzieć wynik"
    require(text.count(quiz_heading) == 1, "missing or duplicated quiz heading")
    quiz = text.split(quiz_heading, 1)[1].split("### Co umiesz teraz wyjaśnić?", 1)[0]
    quiz_fragments = re.findall(r"```c\n(.*?)```", quiz, re.S)
    require(len(quiz_fragments) == 2, "quiz prediction/bug fragments missing")
    quiz_program = "#include <stdio.h>\nint main(void) {\n" + quiz_fragments[0] + "\nreturn 0;\n}\n"
    # The second quiz fragment intentionally does not terminate; never execute it.
    require("if (i == 5) continue;" in quiz_fragments[1], "quiz bug identity")
    with tempfile.TemporaryDirectory(prefix="w5-check-") as tmp:
        scratch = Path(tmp)
        for opt in ["-O0", "-O2"]:
            for name, source in codes.items():
                if name == "fourier":
                    exe = compile_c(source, opt, scratch)
                    r = run([str(exe)], timeout=2)
                    require(r.returncode == 0 and not r.stderr, "Fourier execution status")
                    got = [list(map(float, row.split())) for row in r.stdout.splitlines()]
                    baseline = [list(map(float, row.split())) for row in EXPECTED[name].splitlines()]
                    require(len(got) == len(baseline), "Fourier sample count")
                    require(all(abs(a-b) <= 1e-6 for row, ref in zip(got, baseline) for a, b in zip(row, ref)), "Fourier printed samples")
                else:
                    execute(source, EXPECTED[name], opt, scratch)
            execute(quiz_program, "0 1 3 4 | i=5\n", opt, scratch)
            compile_c(scope_fail, opt, scratch, fail=True)
            for source, output in variants:
                execute(source, output, opt, scratch)
            for data, status, output, err in console:
                execute(game, output, opt, scratch, data, status, err)
            # Include the ACTUAL notebook function and replace only demonstration main.
            harness = '#define main demo_main\n' + codes["fourier"] + '''
#undef main
int main(void) {
    for (int N=1; N<=5; ++N) {
        for (int i=-4; i<=4; ++i) {
            double x=i/4.0;
            printf("%d %.2f %.17g %.17g\\n",N,x,szereg(x,1.0,N),szereg(2*x,2.0,N));
        }
    }
    return 0;
}
'''
            exe = compile_c(harness, opt, scratch)
            r = run([str(exe)], timeout=2)
            require(r.returncode == 0 and not r.stderr, "Fourier numeric harness")
            values = {}
            for row in r.stdout.splitlines():
                ns, xs, ys, zs = row.split()
                n, x, y, z = int(ns), float(xs), float(ys), float(zs)
                reference = 4 / math.pi * math.fsum(math.sin((2*k+1)*math.pi*x)/(2*k+1) for k in range(n))
                require(abs(y-reference) < 1e-12 and abs(y-z) < 1e-12, "Fourier reference/scaling")
                if x in [-1, 0, 1]:
                    require(abs(y) < 1e-12, "Fourier jump value")
                values[n, x] = y
            require(len(values) == 45, "Fourier numeric rows")
            require(abs(values[1, .5] - 4/math.pi) < 1e-12, "N=1 analytic")
            require(abs(values[2, .5] - 8/(3*math.pi)) < 1e-12, "N=2 analytic")
            for (n, x), y in values.items():
                require(abs(y + values[n, -x]) < 1e-12, "Fourier odd symmetry")
            print(f"PASS {opt}: {len(codes)} ordinary C programs; {len(variants)} edge variants; "
                  f"{len(console)} console inputs; 1 quiz prediction; 45 Fourier rows (L=1/2, atol=1e-12); 1 EXPECTED FAIL")
        kernel_smoke(scratch)
    print(f"PASS notebook: W5.0–W5.8, C kernel metadata, {len(images)} offline images, no saved output")
    print(run(["gcc", "--version"]).stdout.splitlines()[0])


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, subprocess.TimeoutExpired, OSError, KeyError, ValueError) as error:
        print("FAIL:", error, file=sys.stderr)
        sys.exit(1)
