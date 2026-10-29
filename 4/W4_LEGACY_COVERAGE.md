# W4 — audyt pokrycia materiałów historycznych i zamrożenie zakresu

**Checkpoint:** W4.0 — audyt, bez modernizacji kodu.  
**Repozytorium:** `sgepner/Computer-Science-1`, gałąź robocza `feature/W4-modernizacja`.  
**Punkt odniesienia:** `master` = `f2e4c94b83431c8ee37267cee3b9688e11751c24` (2026-10-29).  
**Status W4.0:** `VERIFIED PASS`; **W4.1:** `VERIFIED PASS`; **W4.2:** `IMPLEMENTED / VERIFICATION PENDING`.

## 1. Źródła audytu i ich stan

| Materiał | Referencja / identyfikator | Zakres |
|:--|:--|:--|
| `4/lec4.tex` | blob `d7f1592bfeab55c6f73c930e66318d4d8bf78fe2` | 12 slajdów/ramek, w tym tytułowa; tematy: branching i funkcje |
| `4/Lecture 4 examples.ipynb` | blob `dab67363443784d340b649a23b96482428ef1604` | 58 komórek, oryginalny notebook angielski, kernel C |
| `4/samples/` | tree `41913630be1efbc8f0459ace780ae71539c634da` | 10 programów C |
| `4/lec4.pdf` | blob `84dbf387854b144c70b5fb2cc6582e1de2df5b80` | historyczny plik PDF; zachować, nie regenerować w W4.0 |
| `1/Wykład 1.ipynb` | wersja na powyższym `master` | program, funkcje, prototypy, `return`, spirala dydaktyczna |
| `2/Wykład 2.ipynb` | wersja na powyższym `master` | `bool`, operatory porównania, priorytety, `void` |
| `3/Wykład 3.ipynb` i `3/README.md` | wersja na powyższym `master` | `printf`, `sscanf`/`scanf`, `math.h`, kontrola wejścia, delta i pierwiastki |
| `5/Lecture 5 examples.ipynb` | wersja na powyższym `master` | kolejny wykład: pętle, `break`, `continue` |

**Metoda:** audyt treści źródłowych `lec4.tex`, komórek historycznego notebooka oraz wszystkich plików `samples`. W W4.0 nie porównywano niezależnie wyrenderowanych stron `lec4.pdf` z `lec4.tex`; zgodność PDF ze źródłem wymaga osobnego sprawdzenia wizualnego przy przygotowywaniu materiałów prezentacyjnych. Dokument mapuje **zakres merytoryczny**, nie obiecuje zachowania błędnych programów 1:1.

## 2. Granica zakresu — decyzja dydaktyczna

**Temat główny W4:** złożone wyrażenia logiczne i rozgałęzienia przepływu sterowania w C.  
**Cel:** student potrafi (1) obliczyć wartość warunku, (2) przewidzieć, które operandy będą rzeczywiście obliczone, (3) wskazać wykonywane gałęzie, (4) zbudować i przetestować drzewo decyzji.

Metodyka W1–W3: **problem → przewidywanie → eksperyment w C → obserwacja → wyjaśnienie → zmiana pojedynczego warunku → sprawdzenie**. Nie tworzymy oddzielnego wykładu z algebry Boole'a; reguły logiczne wprowadzamy na kodzie, tabelach i grafach.

### Docelowy przebieg 105 minut (sekcje wewnątrz nowego notebooka)

| Sekcja | Temat | Czas |
|:--|:--|--:|
| W4.0 | Od wartości i danych wejściowych do decyzji | 5 min |
| W4.1 | Wyniki porównań i warunki (krótki powrót do W2) | 8 min |
| W4.2 | `&&`, `\|\|`, `!`, tabele prawdy, negacja warunków i de Morgan | 20 min |
| W4.3 | Priorytety, nawiasy, short-circuit i efekty uboczne | 12 min |
| W4.4 | `if` / `else` / `else if`, niezależne warunki, zagnieżdżenia | 20 min |
| W4.5 | Operator warunkowy `?:` jako wyrażenie | 10 min |
| W4.6 | `switch` / `case` / `break` / `default` i fall-through | 10 min |
| W4.7 | Równanie kwadratowe jako drzewo decyzji | 15 min |
| W4.8 | Pytania kontrolne i przejście do pętli W5 | 5 min |

**Granica powtórzeń:** `bool` i porównania tylko przywołujemy z W2.9; operatory przypisania i podstawowe priorytety z W2.11; formatowanie/odczyt z W3.1–W3.5; `sqrt` i wzór kwadratowy z W3.6–W3.7; podstawy funkcji, prototypów, `void` i `return` z W1 oraz W2.10. Nie powtarzamy ich pełnego wywodu.

**Funkcje i zmienne globalne:** zachować mapę dawnego materiału, ale szczegółowe przekazywanie przez wartość, przesłanianie nazw i globalny stan umieścić w **materiale uzupełniającym W4**, nie w głównej części o logice. Pokażemy, że funkcja może zwrócić wynik warunku, ale nie będziemy uczyć używania globalnych zmiennych jako domyślnego zamiennika argumentów i wartości zwracanych.

**Ustalenia prowadzącego (2026-10-29):**
1. Przykład `if (a = 7)` **może znaleźć się jako wykonywalne doświadczenie w notebooku**; nie ograniczać go do zewnętrznego pliku. Należy wyjaśnić, że to przypisanie, a nie porównanie, oraz odróżnić ostrzeżenie kompilatora od składniowego błędu C. Diagnostykę `-Wall`/`-Werror` sprawdzamy w osobno oznaczonym teście; poprawny eksperyment można zapisać także jako `if ((a = 7))`, nie ukrywając jego skutku ubocznego.
2. W C **nie ma przeciążania funkcji na podstawie typów/liczby argumentów** (w przeciwieństwie do C++). Sprzeczność slajdów i notebooka poprawiamy jednoznacznie.

## 3. Pełna mapa historycznych slajdów `lec4.tex`

| Ramka / temat | Nowe miejsce | Decyzja |
|:--|:--|:--|
| 1. Strona tytułowa | W4.0 | Tytuł polski; nowa obietnica dydaktyczna |
| 2. *Code branching*: `if`, `?:`, `switch` | W4.0, W4.4–W4.6 | Zachować trzy mechanizmy, osadzić w jednym problemie |
| 3. *if()*: prawda/fałsz i operatory `> < >= <= == !=` | W4.1 → W2.9 | Tylko niezbędne przypomnienie; `=` vs `==` jako eksperyment |
| 4. *AND and OR* | W4.2–W4.3 | Rozwinąć o `!`, tabele, de Morgana, short-circuit i kolejność obliczeń |
| 5. *Basic if syntax* i klamry | W4.4 | Zamienić niekompilowalny pseudokod na program i graf |
| 6. *What else?* — `else` | W4.4 | Eksperyment: warunek prawdziwy/fałszywy, tylko jedna z dwóch gałęzi |
| 7. `else if` | W4.4 | Niezależne `if` kontra jeden łańcuch, binding `else` |
| 8. *Inline if* / `?:` | W4.5 | Naprawić pseudokod, podkreślić wynik wyrażenia |
| 9. `switch`, `case`, `break`, `default` | W4.6 | Naprawić błędne `case expr`: etykieta wymaga stałego wyrażenia całkowitego; pokazać fall-through |
| 10. *Functions*: argumenty, wynik, procedury | W4.7 (krótkie nawiązanie), uzupełnienie | Nie powtarzać W1 i W2.10, użyć do modularnego algorytmu |
| 11. *Functions* i linker | W1, uzupełnienie | Sprostować: osobne kompilowanie dotyczy jednostek translacji, nie jest obowiązkową cechą każdej funkcji |
| 12. *Functions*: deklaracje/definicje, nazwy | W1, uzupełnienie | Skorygować błędną sugestię przeciążania i wywołanie `fun1(5, 7)` przy jednoargumentowej definicji |

**Pokrycie:** wszystkie 12 ramek mają decyzję; żaden historyczny temat nie znika bez odsyłacza albo uzasadnienia.

## 4. Pełna mapa 58 komórek historycznego notebooka

Indeksy są **zerowe**, zgodne z plikiem `Lecture 4 examples.ipynb`.

| Komórki | Treść pierwotna | Nowa lokalizacja / korekta |
|:--|:--|:--|
| 0 | Cel *branching* i równanie kwadratowe | W4.0, W4.7; zachować główny przykład integrujący |
| 1–3 | Operatory relacyjne i `!`; wydruki wartości | W4.1–W4.3; wytłumaczyć `!5 > 4` jako `(!5) > 4`, nie `!(5 > 4)` |
| 4–8 | `if`, wartości zero/niezero, nawiasy klamrowe | W4.4; zamienić opis *scope* na precyzyjne rozróżnienie bloku i instrukcji sterowanej; naprawić zapisane wyniki |
| 9–14 | `!=`, `==`, `=`, porównania i zadanie | W4.1 / W4.4; `5 != 4` daje `1`, nie historyczny wydruk `4`; przypisanie w `if` dopuścić w notebooku jako celowy eksperyment |
| 15–18 | `&&`, `\|\|` i priorytety | W4.2–W4.3; dołożyć negację warunków, short-circuit, tablice prawdy i nawiasy |
| 19–23 | `if / else / else if` i usuwanie `else` | W4.4; wyeksponować różnicę między wyłącznym wyborem i niezależnymi `if` |
| 24–25 | Zagnieżdżone `if` | W4.4; graf gałęzi oraz jawne określenie, do którego `if` należy `else` |
| 26–29 | Warunkowy `?:` i równoważny `if/else` | W4.5; zachować parę przykładów, pokazać wynik wyrażenia |
| 30–32 | `switch` z wyrażeniem całkowitym | W4.6; uzupełnić o brak `break`, domyślną etykietę i stałość `case` |
| 33–34 | Pierwsza wersja równania kwadratowego | W4.7; rozdzielić `a==0`, `delta<0`, `delta==0`, `delta>0`, wejście; kontrolować dostępność pierwiastków rzeczywistych |
| 35–39 | Wprowadzenie do proceduralnego C i deklaracji funkcji | W1, W2.10, krótkie nawiązanie w W4.7 + uzupełnienie; nie pozostawiać niedziałającego pseudokodu jako komórki C |
| 40–45 | Funkcja zwracająca wynik, argumenty przez wartość, `void` | Uzupełnienie W4; połączyć z wcześniejszym `sum`, nie powtarzać definicji i składni |
| 46–50 | Zmienne globalne, modyfikacja i przesłanianie | Uzupełnienie W4; nie przedstawiać globalnego stanu jako właściwego lekarstwa na przekazanie przez wartość |
| 51–54 | Solver podzielony na funkcje, `scanf`, globalne dane i `switch` | W4.7 (algorytm) + uzupełnienie (funkcje); usunąć nadpisanie danych wpisanych przez użytkownika, sprawdzać wejście, wypisywać znalezione pierwiastki |
| 55–56 | Wyjaśnienie braku przeciążania i celowo błędny program | Uzupełnienie W4; zachować jednoznaczną różnicę C/C++; `fun1()` ma błędną nazwę, dwie definicje `fun` mają konflikt |
| 57 | Pusta komórka | Nie przenosić |

**Ważne:** w oryginalnym notebooku są zapisane wyniki wykonania, które nie odpowiadają aktualnemu kodowi. Nowy notebook będzie miał oczyszczone `outputs`, a oczekiwane wyniki zostaną podane w opisie i sprawdzone testami.

## 5. Pełna mapa `4/samples/` (10 plików)

| Plik | Nowa lokalizacja | Decyzja |
|:--|:--|:--|
| `true_and_false.c` | W4.1–W4.2 | Użyć do szybkiego przypomnienia W2; bez długiego wykładu o samych porównaniach |
| `if1.c` | W4.4 | Zachować eksperyment `if (a = 7)` oraz skutki przypisania; test ostrzeżeń oddzielić od zwykłej ścieżki `-Werror` |
| `if2.c` | W4.4 | Zachować jako prosty przykład `if/else`; uprościć niepotrzebne `include` |
| `if3.c` | W4.4 (zadanie) | Zachować zabawę „I win”; sprawdzać wynik `scanf` i jasno określić dopuszczalny zakres |
| `if4.c` | W4.5 | Zachować porównanie `if/else` z `?:`, wyraźnie rozdzielić wydruki |
| `switch.c` | W4.6 | Zachować; sprawdzić wejście, rozwinąć o `fall-through` |
| `quadratic.c` | W4.7 | Przebudować błędną klasyfikację `delta==0`, sprawdzić wejście i `a==0` |
| `global.c` | Uzupełnienie W4 | Przekazywanie przez wartość i globalny stan; usunąć nieużywaną zmienną i zbędne nagłówki |
| `rest.c` | W3.6 (odsyłacz) | `ceil`, `floor`, `fabs` są już zakresem matematyki W3; bez powtórzenia na W4 |
| `roots.c` | W2.5, W3.6 (odsyłacz) | Zachować pułapkę `1/3` vs `1.0/3.0` jako ćwiczenie utrwalające, nie nowe zagadnienie W4 |

Powyższe mapowanie obejmuje **wszystkie 10 programów**. Nie usuwamy historycznych plików w W4.0.

## 6. Rejestr wymaganych poprawek merytorycznych

| ID | Usterka / ryzyko | Naprawa w kolejnych etapach |
|:--|:--|:--|
| R01 | Nieaktualne `outputs` w notebooku, m.in. wyświetlenie `4` po `a != b` dla `5` i `4` | W4.1/W4.7: wyczyścić wyniki i porównać z rzeczywistym wykonaniem |
| R02 | Niejasna semantyka `!5 > 4`: `!` wiąże silniej od `>` | W4.2–W4.3: nawiasy, przewidywanie, graf operatorów |
| R03 | Brak short-circuit, pomieszanie wartości wyniku i przebiegu obliczania | W4.2: osobny eksperyment z obserwowalnym wywołaniem funkcji i bezpiecznym warunkiem `b != 0 && a / b > 2` |
| R04 | `if (a = b)` bywa przedstawione jako składniowo niedozwolone | W4.4: poprawne rozróżnienie przypisania, ostrzeżenia i warunku; wykonywalny przykład w notebooku |
| R05 | Brak wyraźnej różnicy między kilkoma `if` a łańcuchem `else if`; „dangling else” | W4.4: graf i eksperyment |
| R06 | Na slajdach pseudokod `if`/`?:` oraz `else if()` wygląda jak składnia C | W4.4–W4.5: zamienić na poprawne programy lub jednoznacznie oznaczone pseudokody |
| R07 | Slajd `switch` używa etykiety `case expr1` bez warunku stałości | W4.6: `case` musi być stałym wyrażeniem całkowitym; pokazać `break` i brak `break` |
| R08 | `quadratic.c` używa `delta >= 0` jako „dwa pierwiastki”, a końcowego `else` jako „jeden” | W4.7: odrębne przypadki `delta<0`, `==0`, `>0`; uwaga na NaN (porównania z NaN są fałszywe) |
| R09 | `quadratic.c`/notebook nie weryfikują konsekwentnie `scanf` oraz `a==0` | W4.7: warunki wstępne, przypadki liniowe i błędne wejście |
| R10 | Notebook po `scanf` nadpisuje współczynniki; wynik liczby pierwiastków nie jest ich wydrukiem | W4.7: deterministyczne dane w notebooku, prawdziwy `scanf` w terminalu, poprawny wydruk |
| R11 | Historyczne slajdy sugerują przeciążanie funkcji w C; notebook później temu przeczy | Uzupełnienie W4: jasno **C nie obsługuje overloadingu funkcji**; wyjaśnić błąd w kompilacji |
| R12 | Opis funkcji sugeruje, że są zawsze kompilowane oddzielnie i że stan globalny rozwiązuje problem argumentów | Uzupełnienie W4: rozróżnić jednostkę translacji i funkcję, preferować argumenty i `return` |
| R13 | `roots.c` używa `pow(a, 1/3)`: dzielenie całkowite daje zero | W3.6 (odsyłacz), nie powtarzać matematyki w głównym W4 |
| R14 | Fragmenty o `bool` mogą zacierać różnicę: wynik relacyjnego operatora to `int` 0/1, a zmienna `bool` z W2 jest osobnym typem | W4.1: pojedyncze precyzyjne przypomnienie |
| R15 | Niektóre przykłady `scanf` są niedeterministyczne w notebookowym kernelu C | W4.4/W4.7: `sscanf` z napisów w notebooku; `scanf` z klawiatury w terminalu. **Wyjątkiem nie jest** doświadczenie `if (a=7)` — ono może być w notebooku |

**Uwaga numeryczna do R08:** opis „końcowa gałąź jest nieosiągalna” dotyczy tylko skończonej rzeczywistej `delta`. Dla NaN porównania `delta >= 0` i `delta < 0` są fałszywe; nie wolno używać tego `else` do klasyfikacji pierwiastka podwójnego. W podstawowym zadaniu zakładamy skończone dane; ewentualna obsługa `isfinite` jest rozszerzeniem.

## 7. Planowane grafy i kryteria ich użycia

| Graf | Sekcja | Co studenci muszą móc z niego odczytać? |
|:--|:--|:--|
| G1 — drzewo składni wyrażenia | W4.2–W4.3 | Różnica `a \|\| b && c` vs `(a \|\| b) && c`; struktura nie musi oznaczać kolejności wykonania |
| G2 — ewaluacja short-circuit | W4.3 | Kiedy `&&`/`\|\|` pomija prawy operand i dlaczego to chroni operacje |
| G3 — graf instrukcji `if/else if/else` | W4.4 | Różnica między niezależnymi `if`, łańcuchem i zagnieżdżeniem |
| G4 — drzewo decyzyjne równania kwadratowego | W4.7 | Poprawny podział wejścia, liniowe/kwadratowe, `delta` i ścieżki wyniku |

Opcjonalnie osobny mały diagram **`switch` i fall-through**, jeśli eksperyment bez `break` będzie trudny do przeczytania z samego kodu. Grafy powinny być lokalnymi SVG, dostępne offline, czytelne na projektorze i w skali szarości. W W4.0 **nie tworzymy jeszcze grafik**.

## 8. Studium przypadku — kontrakt funkcjonalny na W4.7

Program przyjmuje trzy współczynniki `a, b, c`. Dla poprawnych skończonych danych i rachunku rzeczywistego ma rozróżnić:

| Przypadek | Oczekiwany wynik |
|:--|:--|
| Niepoprawnie wczytane dane | Komunikat błędu; bez użycia nieprzypisanych zmiennych |
| `a == 0, b != 0` | Równanie liniowe, jedno rozwiązanie |
| `a == 0, b == 0, c != 0` | Brak rozwiązań |
| `a == 0, b == 0, c == 0` | Nieskończenie wiele rozwiązań |
| `a != 0, delta < 0` | Brak rozwiązań rzeczywistych |
| `a != 0, delta == 0` | Jeden pierwiastek rzeczywisty (podwójny) |
| `a != 0, delta > 0` | Dwa różne pierwiastki rzeczywiste |

Używać prostych wartości dokładnie reprezentowalnych do obowiązkowych testów rozgałęzień; problemy tolerancji i obliczeń zmiennoprzecinkowych odsyłają do W2.6. Nie wymagać w głównym W4 numerycznie stabilnej implementacji dla skrajnie uwarunkowanych współczynników.

## 9. Kryteria zamknięcia W4.0 i zasady testowania

1. Zweryfikować, że źródłem jest dokładnie `f2e4c94b83431c8ee37267cee3b9688e11751c24` i że gałąź W4 powstała z tego commita.
2. Potwierdzić istnienie i kompletność map: **12 ramek `lec4.tex`, 58 komórek notebooka (0–57), 10 plików `samples`**.
3. Potwierdzić decyzję o uruchamianym `if (a = 7)` w notebooku oraz brak przeciążania funkcji w C.
4. Sprawdzić spójność mapy z zakresem W1–W3 i 105-minutową strukturą.
5. W W4.0 nie zmieniać `.ipynb`, `.c`, `.tex`, `.pdf` ani skryptów testowych; to **tylko dokumentacyjny checkpoint**.
6. Jako gate nowej rewizji wystarczą: obecność/treść pliku audytu, `git diff --check` i kontrola tego, że commit zawiera tylko ten dokument. Kompilacja C i regresja notebooka **rozpoczną się od W4.1/W4.2**, stosownie do zakresu zmian.
7. Dopiero po dostarczeniu pozytywnego lokalnego wyniku W4.0 przejść w trybie `@Test Review Advance` do **W4.1**.

## 10. Roadmapa modernizacji — stan po przygotowaniu audytu

- **W4.0** — audyt i zamrożenie zakresu: `VERIFIED PASS`.
- **W4.1** — konstrukcja nowego `4/Wykład 4.ipynb`: `VERIFIED PASS`.
- **W4.2** — wyrażenia logiczne, de Morgan, short-circuit: `IMPLEMENTED / VERIFICATION PENDING`.
- **W4.3** — `if`, `else`, `else if`, zagnieżdżenia, `?:`, `switch`: `PENDING`.
- **W4.4** — grafy przepływu sterowania: `PENDING`.
- **W4.5** — solver równania kwadratowego i przypadki brzegowe: `PENDING`.
- **W4.6** — funkcje i materiał uzupełniający: `PENDING`.
- **W4.7** — testy regresyjne i weryfikacja: `PENDING`.
- **W4.8** — dokumentacja, test prezentacji i zamknięcie: `PENDING`.

**Uwaga o numeracji:** W4.0–W4.8 powyżej to **checkpointy projektu**. W tabeli z ` 2 numeracja W4.0–W4.8 opisuje **rozdziały notebooka**; oba podziały nie są tożsame.

**Następny autoryzowany krok po pozytywnym gate:** tylko **W4.1**, bez wyprzedzania prac W4.2–W4.8.


## 11. Weryfikacja W4.1 i otwarcie W4.2

**W4.1 — VERIFIED PASS (dodo, 2026-10-29).** Na `124fcac1c9bb9f7dad5f5c2ae3006fef2950410f` test zwrócił `W4.1 STRUCTURE PASS`, a pierwsza komórka C wykonała oczekiwane trzy wiersze. `git diff --check` bez uwag. Skróty prowadzącego z rewizji `2ef0cdfe8e563b512ef1cfa582ceca7d143b4a02` zachowano, łącznie z zapisanym wynikiem pierwszej komórki.

**W4.2 — IMPLEMENTED / VERIFICATION PENDING.** Dodano przykłady wyrażeń logicznych, de Morgana, priorytetów i short-circuit oraz zabezpieczenia przed dzieleniem przez zero. Przed commitem programy testowano przez GCC C11 `-Wall -Wextra -Werror -pedantic` (`-O0` i `-O2`, 6 programów, 9 wariantów). Nowa rewizja wymaga lokalnego `python3 4/check_w4_logic.py` i sprawdzenia komórek Jupyter C. Zakres W4.3+ pozostaje poza checkpointem.
