# W3 — audyt pokrycia materiałów historycznych

Stan odniesienia: `3/lec3.tex` oraz `3/Lecture 3 Examples.ipynb` (25 komórek).
Materiał obowiązujący: [`Wykład 3.ipynb`](Wyk%C5%82ad%203.ipynb).
Cel: zachować koncepcje, przykłady i humor z oryginału, nie powielać pełnego W2 oraz naprawić błędy i niebezpieczne zachowania. Mapa dotyczy **zakresu merytorycznego**, nie identyczności kodu czy grafiki.

## Oryginalne slajdy `lec3.tex`

| Slajd/temat historyczny | Gdzie teraz? | Decyzja |
|:--|:--|:--|
| Lista typów `int/float/double/char/bool/void` | W3.0 → W2.2, W2.6, W2.8–W2.10 | Krótkie przypomnienie z odsyłaczami. |
| Zmienne, deklaracja, przypisanie, wyrażenie z `sqrt(delta)` | W3.0 → W2.3; W3.7 (wzór kwadratowy) | `delta` obliczana jawnie, program kompletny. |
| Konwersja `double`/`int`, rzutowanie | W3.0 → W2.7 | Nie powielamy omówienia utraty informacji. |
| Priorytety, nawiasy | W3.0 → W2.11; W3.7 | Powrót przy `(2.0*a)`. |
| `++`, `--` w formie przedrostkowej i przyrostkowej | W3.0 → W2.11 | Materiał W2, bez zbędnych duplikatów. |
| `+=`, `-=`, `*=`, `/=` | W3.0 → W2.11 | Materiał W2. |
| `printf`, typy, liczba wypisanych znaków i błędy | W3.1 | Wyraźne rozróżnienie wydruku od wartości zwracanej. |
| `%[flags][width][.prec]specifier`, `+`, `-`, `d/f/e/g` | W3.1–W3.2 | Rozszerzone przykłady precyzji i notacji naukowej. |
| Sterujące `\\n`, `\\t`, `\\b`, `\\r`, `\\v`, `\\\\`, cudzysłów/apostrof | W3.3 i `samples/sterowanie_terminalem.c` | Kontrolne sekwencje w terminalu, nie w Jupyterze. |
| `scanf`, `&`, żart i wynik funkcji | W3.4–W3.5 | Humor przywrócony, poprawiono błędny opis wyniku i dodano walidację wejścia. |
| Trygonometryczne i odwrotne `sin/cos/tan/asin/acos/atan/atan2`; hiperboliczne `sinh/cosh/tanh` | W3.6 | Radiany, tabela i eksperyment rozszerzający. |
| `exp/log/log10/pow/sqrt/ceil/fabs/floor` | W3.6 | Demonstracje i sprawdzanie dziedziny. |

## Oryginalny notebook `Lecture 3 Examples.ipynb`

| Komórki historyczne | Temat i reprezentacja w bieżącym W3 |
|:--|:--|
| 0–1 | `Hello World`, typy i `char` — W3.0 z odsyłaczami do W1/W2; formaty W3.1. |
| 2–3 | `++`, `-=`, reszta, dzielenie całkowite i rzutowanie — wyłożone w W2.5, W2.7, W2.11; mapa W3.0. |
| 4–5 | `printf` jako funkcja zwracająca liczbę zapisanych znaków — W3.1. |
| 6–8 | Znaczniki formatu, wyrównanie, szerokość, precyzja `int`/`double`, `e/E/g`, 15 cyfr — W3.2. |
| 9–10 | `\\n`, `\\b`, `\\t`, `\\v`, `\\r`, `\\\\`, cudzysłów — W3.3 + terminal. |
| 11–13 | `scanf` z klawiatury, adres `&`, żart, `int` i `double` — W3.4–W3.5, `samples/scanf*.c`; błędne wejście/EOF. |
| 14–15 | `sin`, `cos`, `tan`, kąt `2\pi` — W3.6 oraz `samples/math.c`; uzupełniająca mapa funkcji. |
| 16–18 | `pow(int,int)` i `pow(double,double)`, ujemne wykładniki — W3.6 z przykładami `pow(5,-3.9)`, `pow(10,2.4)`. |
| 19–20 | `exp(x+y)` — W3.6, test wartości `x=1.9,y=3.8`. |
| 21–22 | Dlaczego `exp(x)` zamiast `pow(exp(1.0),x)`; `log`, `log10`, `sqrt` — W3.6. |
| 23 | `#define PI 4.0*atan(1.0)`, `sin(\pi/2)` — W3.6: komentarz o alternatywie i wersja z `acos(-1.0)`; makra z W1. |
| 24 | Imię i nazwisko, numer albumu w zmiennej i z klawiatury, działania na dwóch `double` — W3.8 „Zadanie 0” i kontynuacja matematyczna. |

## Korekty i świadome zmiany

1. **`scanf` nie zwraca liczby wypisanych znaków**. Liczy poprawnie przypisane pola, a przy błędzie wejścia przed pierwszym przypisaniem może zwrócić `EOF`; w praktyce programy sprawdzają wartość względem liczby oczekiwanych pól.
2. Oryginalny obraz `3/scanf_perils.png` został przywrócony do repozytorium przez prowadzącego. Nowy notebook wyświetla ten właśnie plik obok puenty **„He forgot about the `&`!!”**. Bez zamiany na inny komiks i bez zależności od internetu.
3. W oryginalnym `lec3.tex` występowały błędy składni C (m.in. brak średników, literówka `doubly` w `atan2` i niezdefiniowana `delta`). Nowy notebook prezentuje samodzielne programy poprawne składniowo, z zadeklarowanymi wartościami i walidacją.
4. Przykłady `scanf` w niezależnej konsoli zastąpiły ryzykowne uruchamianie interaktywnego odczytu w kernelu `c`. Deterministyczne testy parsingowe wykonujemy przez `sscanf` w notebooku.
5. Nie tworzymy sztucznego przykładu niepoprawnego `scanf("%d", a)` jako wykonywalnej komórki: jest oznaczony jako **antyprzykład, NIE URUCHAMIAĆ**.
6. Nowy materiał rozszerza oryginał o `stdout/stderr`, kontrolę odczytu `1/0/EOF`, dziedziny `math.h` i testy regresyjne, żeby uczniowie nabyli bezpieczne nawyki.
7. Dla każdego programu C przetestowanego w `check_w3.py` zachowujemy zgodność z GCC C11 pod `-O0` i `-O2`; właściwe uruchomienie w specyficznym kernelu Jupyter C wymaga osobnego sprawdzenia na komputerze wykładowym.

**Wniosek:** wszystkie istotne tematy z obydwu historycznych źródeł są przedstawione w W3 albo jasno wskazane jako materiał już omówiony w W2. Celowo **nie kopiujemy** błędnych lub niebezpiecznych programów 1:1 ani oryginalnego nieobecnego pliku graficznego.
