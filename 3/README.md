# Wykład 3 — wejście, wyjście i funkcje matematyczne

**Aktualny materiał do prowadzenia wykładu:** [`Wykład 3.ipynb`](Wyk%C5%82ad%203.ipynb), w języku polskim, z kernelem Jupyter **C** (`kernelspec.name = c`). Materiał jest kontynuacją `1/Wykład 1.ipynb` i `2/Wykład 2.ipynb` i celowo nie powtarza wykładu o operatorach i konwersjach.

Kolejność: krótkie nawiązanie do W2 → `printf` i liczba zapisanych znaków → formatowanie → `stdout`/`stderr` → `scanf` i liczba przypisanych pól / `EOF` → rozróżnienie `%f` i `%lf` → `<math.h>` → ćwiczenie integrujące. Po każdym ważnym kroku przewidujemy wynik, uruchamiamy program, zmieniamy jeden szczegół i uzasadniamy obserwację.

## Ważne: Jupyter nie jest terminalem

W notebooku **celowo nie ma wykonywalnych komórek z interaktywnym `scanf`**. Kernel C może nie udostępniać standardowego wejścia tak jak terminal, dlatego doświadczenia z konwersją wykonujemy deterministycznie przez `sscanf("dane", "format", &zmienna)`. To nie to samo źródło danych co `scanf`, lecz analogiczne formatowanie i reguły zliczania przypisań.

Prawdziwe wejście z klawiatury, błędne dane, koniec pliku, komunikaty na `stderr` i przekierowania **sprawdzamy w niezależnej konsoli**, poza Jupyterem, analogicznie do kompilacji `hello.c` w W1.

```bash
# z katalogu głównego repozytorium
gcc -std=c11 -Wall -Wextra -Werror -pedantic 3/samples/scanf_stany.c -o /tmp/w3_scanf
/tmp/w3_scanf
printf '7 2.5\n' | /tmp/w3_scanf
printf '7 kot\n' | /tmp/w3_scanf
printf 'kot\n' | /tmp/w3_scanf
/tmp/w3_scanf < /dev/null

# zwrócona wartość 2 / 1 / 0 / EOF
# status zakończenia procesu to inna informacja niż wynik scanf
```

Wpisując w terminalu znak EOF na początku wejścia na Linuksie, zwykle używa się `Ctrl+D`. Program zakończony kodem `1` **celowo sygnalizuje błędne dane**. Nie należy interpretować tego jako awarii testu.

## Programy do uruchamiania w konsoli

| Plik | Do czego służy? | Polecenie kompilacji |
|:--|:--|:--|
| `samples/printf.c` | Szerokość pola, precyzja, `%%` | `gcc -std=c11 -Wall -Wextra -Werror -pedantic 3/samples/printf.c -o /tmp/w3_printf` |
| `samples/sterowanie_terminalem.c` | `\\b`, `\\r`, `\\v`, apostrof i różnice między terminalem a plikiem | `gcc -std=c11 -Wall -Wextra -Werror -pedantic 3/samples/sterowanie_terminalem.c -o /tmp/w3_sterowanie` |
| `samples/stdio_terminal.c` | `printf` zwraca liczbę zapisanych znaków; `stdout` kontra `stderr` | `gcc -std=c11 -Wall -Wextra -Werror -pedantic 3/samples/stdio_terminal.c -o /tmp/w3_stdio` |
| `samples/scanf_stany.c` | Sukces 2, sukces częściowy 1, niedopasowanie 0, EOF | `gcc -std=c11 -Wall -Wextra -Werror -pedantic 3/samples/scanf_stany.c -o /tmp/w3_scanf` |
| `samples/scanf.c` | Sprawdzanie pełnego odczytu dwóch pól | `gcc -std=c11 -Wall -Wextra -Werror -pedantic 3/samples/scanf.c -o /tmp/w3_dane` |
| `samples/math.c` | Kąt w radianach, `sin` i `cos` | `gcc -std=c11 -Wall -Wextra -Werror -pedantic 3/samples/math.c -o /tmp/w3_math -lm` |
| `samples/pow.c` | Potęgowanie dla nieujemnych podstaw | `gcc -std=c11 -Wall -Wextra -Werror -pedantic 3/samples/pow.c -o /tmp/w3_pow -lm` |
| `samples/logs.c` | Logarytm naturalny i dziesiętny oraz dziedzina | `gcc -std=c11 -Wall -Wextra -Werror -pedantic 3/samples/logs.c -o /tmp/w3_logs -lm` |
| `samples/pole_kola.c` | Zadanie integrujące: wejście → sprawdzenie → wynik | `gcc -std=c11 -Wall -Wextra -Werror -pedantic 3/samples/pole_kola.c -o /tmp/w3_kolo -lm` |

Na typowym Linuksie `-lm` występuje **na końcu polecenia**. W komórkach Jupytera, które korzystają z `<math.h>`, zachowano dyrektywę kernela C `//%cflags:-lm` (jak w historycznym notebooku). Jest ona komentarzem dla GCC. Uruchomienie tych komórek w konkretnym kernelu Jupyter należy dodatkowo zweryfikować na komputerze wykładowym.

Wyjście i błędy można badać osobno:

```bash
/tmp/w3_stdio > /tmp/w3_stdout.txt 2> /tmp/w3_stderr.txt
cat /tmp/w3_stdout.txt
cat /tmp/w3_stderr.txt
```

## Regresja C11

Z katalogu głównego repozytorium:

```bash
python3 3/check_w3.py
```

Skrypt nie wymaga uruchamiania Jupytera. Sprawdza metadane `kernelspec`, strukturę W3.0–W3.9, brak zapisanych wyników, brak interaktywnego `scanf` w komórkach kodu, a następnie kompiluje **wszystkie 22** programów z notebooka oraz **9** programów konsolowych pod GCC C11 z `-Wall -Wextra -Werror -pedantic` w konfiguracjach `-O0` i `-O2`. Weryfikuje **44 wykonania komórek i 46 scenariuszy konsolowych** (również nieprawidłowe wejście i EOF). Programy i wyniki nie pozostają w repozytorium; pliki tymczasowe zostają usunięte.

Testy mają oczekiwane wyniki dla typowej konfiguracji Linux/x86-64, GCC, standard C11 i lokalizacja `C`. Nie są bezpośrednim uruchomieniem kernela `c` — to osobny test w środowisku wykładowym.

## Zachowane wątki oryginalnego W3 i żart z welociraptorem

Pełne zestawienie historycznych slajdów `lec3.tex` i komórek `Lecture 3 Examples.ipynb` z aktualnym notebookiem: [`W3_LEGACY_COVERAGE.md`](W3_LEGACY_COVERAGE.md).

W W3.4 przywrócono **oryginalną ilustrację `scanf_perils.png`** (dodana do repozytorium przez prowadzącego) wraz z puentą **„He forgot about the `&`!!”**. Ilustracja jest przechowywana lokalnie obok notebooka, więc działa również offline.

Uzupełniono również odrębny przykład `\\r` / `\\b` / `\\v` wykonywany w terminalu, notację wykładniczą z wieloma cyframi, ujemne i niecałkowite wykładniki `pow`, `exp(x+y)`, funkcje `asin`, `acos`, `atan`, `sinh`, `cosh`, `tanh`, pierwiastki równania kwadratowego i oryginalne ćwiczenie z numerem albumu. Powtórki typów i operatorów pozostają w W2 z wyraźnymi odsyłaczami.

## Materiały historyczne

`Lecture 3 Examples.ipynb` oraz `lec3.pdf` pochodzą z wcześniejszej wersji wykładu i **nie stanowią aktualnego materiału dydaktycznego**. Zachowano je dla porównania. `lec3.tex` jest historycznym źródłem slajdów; jego wykryte błędy merytoryczne i składniowe korygujemy bez zastępowania bieżącego polskiego notebooka. Historycznego PDF **nie regenerowano** w ramach modernizacji notebooka, więc jego treść może nie odzwierciedlać poprawek w źródle `.tex`.
