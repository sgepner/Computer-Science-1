# Kontrakt wykonawczy: audyt i korekty dydaktyczne W1–W5

Status: **DO IMPLEMENTACJI — praca autonomiczna**  
Repozytorium: `sgepner/Computer-Science-1`  
Gałąź robocza: `feature/W1-W5-audyt-poprawki`  
Punkt odniesienia: aktualny `master` z chwili utworzenia gałęzi, 2026-11-06.  
Odbiorca: lokalny agent Codex i ewentualni agenci kontrolni.  
Własność dokumentu: **wyłącznie gałąź robocza; NIGDY nie przenosić do master.**

## 0. Cel, decyzje prowadzącego, zasady nadrzędne

Przeprowadź niezależny, kompletny audyt i poprawę polskich notebooków W1–W5. Porównaj każdy bieżący wykład polski ze starszym angielskim notebookiem i historyczną prezentacją PDF (oraz źródłem `lecN.tex`). Wszystkie istotne treści dydaktyczne i wartościowe eksperymenty powinny być obecne w nowej wersji. **Nie kopiuj historii kursu, nie opisuj zmian jako tłumaczenia ani modernizacji w tekstach dla studentów.** Każdy polski wykład musi być autonomiczną, spójną całością.

Prowadzący zatwierdził kierunek:
1. W3: naucz `puts`, `fputs`, historycznej i niebezpiecznej `gets`, oraz `fgets` zanim `puts` pojawi się w W4/W5.
2. W4: explicite pokaż, że bez klamer `if` obejmuje **jedną instrukcję** (nie „pierwszą linię”!), a z klamrami blok. Pokaż osobno zasięg nazwy zmiennej, jej czas życia, przesłanianie i pułapkę średnika po `if`.
3. W4: zastąp finałowy przykład z `const char *` i `sscanf` **dwoma wariantami tego samego zadania**: (A) całość w `main()`, (B) to samo rozwiązanie podzielone na funkcje/procedury. Cel: składnia i logika `if` oraz sens dekompozycji proceduralnej; nie parsowanie napisów.
4. W5: odzyskaj z historycznych materiałów krótkie eksperymenty i interaktywność, szczególnie grę z `while`/`scanf`/`break` i eksperyment numeryczny z inkrementowaniem `float`.
5. W1/W2: zachowaj rozbudowaną wersję polską, usuwaj tylko stwierdzone błędy lub braki; nie przebudowuj bez potrzeby.

**Tryb pracy: CONTINUOUS (autonomicznie do zakończenia).** Nie czekaj po checkpointach na „kontynuuj”. Wykonuj kolejny etap, jeśli poprzednia bramka PASS. Przy FAIL napraw i powtórz; nie przechodź dalej z niespełnioną bramką. Pytaj prowadzącego **tylko** przy rzeczywistej sprzeczności merytorycznej, nieodwracalnej operacji lub nieusuwalnej blokadzie. Korzystaj z lokalnych deterministycznych narzędzi zamiast modelu tam, gdzie to możliwe; agenta recenzenckiego włącz do niezależnego przeglądu. Nie uruchamiaj ciężkich operacji bez potrzeby. **Nie zmieniaj `master`, nie wykonuj merge/rebase do master, nie twórz PR wymagającego mergowania całej gałęzi.**

## 1. Inwentarz źródeł (jawnie weryfikuj faktyczny stan plików)

| W | Polska wersja docelowa | Notebook angielski | Prezentacja |
|---|---|---|---|
| W1 | `1/Wykład 1.ipynb` | `1/Lecture 1 examples.ipynb` | `1/lec1.pdf`, `1/lec1.tex` |
| W2 | `2/Wykład 2.ipynb` | `2/Lecture 2 Examples.ipynb` | `2/lec2.pdf`, `2/lec2.tex` |
| W3 | `3/Wykład 3.ipynb` | `3/Lecture 3 Examples.ipynb` | `3/lec3.pdf`, `3/lec3.tex` |
| W4 | `4/Wykład 4.ipynb` | `4/Lecture 4 examples.ipynb` | `4/lec4.pdf`, `4/lec4.tex` |
| W5 | `5/Wykład 5.ipynb` | `5/Lecture 5 examples.ipynb` | `5/lec5.pdf`, `5/lec5.tex` |

Nazwy plików uwzględniają dokładną wielkość liter, szczególnie `5/Lecture 5 examples.ipynb`. Jeśli PDF nie jest dostępny, odczytaj `lecN.tex`, sprawdź powiązane grafiki, odnotuj brak możliwości porównania wyglądu slajdów. Nie udawaj, że kontrola PDF została zakończona. Nie zmieniaj oryginalnych źródeł angielskich, `lecN.tex` ani historycznych PDF.

## 2. Obowiązkowy audyt 1:1 i metodologia

Dla każdego W1–W5:
- Odczytaj każdą komórkę angielskiego notebooka, każdą sensowną ramkę PDF/TeX i polski notebook; uwzględnij kod, komentarze, grafiki, pytania, doświadczenia, pułapki i narrację.
- Sporządź **macierz pokrycia**, z wpisem `źródło → polska sekcja/komórka → status`: COVERED, EXTENDED, MOVED (ze wskazaniem wykładu), MISSING, INTENTIONALLY OMITTED (z uzasadnieniem), UNVERIFIED.
- Oddziel brak treści od innego, często lepszego sposobu prezentacji tej samej koncepcji. Zachowaj sens edukacyjny, nie literalne tłumaczenie.
- Sprawdź kolejność wymagań wstępnych pomiędzy W1–W5 (pierwsze użycie symbolu/funkcji/konstrukcji powinno być wyjaśnione lub oznaczone jako świadoma zapowiedź).
- Rozpoznaj ilustracje, które trzeba przenieść obok notebooków, i sprawdź działanie względnych ścieżek offline.
- Nie wstawiaj do notebooków `W4-INT`, `dawniej`, `historyczny wykład` ani opisów projektowych. Dokumentacja wyników należy wyłącznie do tego roboczego pliku lub końcowego raportu/komunikatu agenta.
- Każdy nowy kod C ma pokazać jedną myśl naraz; unikaj nagromadzenia wskaźników, parsowania i złożonych API w przykładach uczących `if` lub pętli.

## 3. W3 — prace obowiązkowe

**W3-IO.1 [P0]** Umieść po podstawach `printf`/`scanf` spójne wprowadzenie do:
- `puts(s)`: napis na `stdout` + automatyczny znak końca wiersza;
- `fputs(s, stream)`: do wskazanego strumienia, bez automatycznego końca wiersza;
- `gets(s)`: **wyłącznie historyczna, usunięta ze standardu C11, niebezpieczna**; wyjaśnij brak ograniczenia długości i nie kompiluj/nie uruchamiaj kodu, który jej używa;
- `fgets(buf, sizeof buf, stdin)`: ograniczenie długości, `NULL` w przypadku niepowodzenia/EOF, zachowywany `\n` o ile zmieści się w buforze, `\0` na końcu poprawnie odczytanego napisu.
- Minimalne, czytelne objaśnienie `char buf[N]`, bufora i napisu zakończonego `\0`, bez wykładu o wskaźnikach/parsowaniu.

**W3-IO.2 [P0]** Stwórz krótkie, wykonywalne doświadczenia `printf` vs `puts` vs `fputs` (różnice końca wiersza) oraz `fgets` z przykładem wejścia krótkiego i dłuższego od bufora. Interaktywne `stdin` uruchamiaj w terminalu lub deterministycznie podawaj dane; nie blokuj kernela Jupyter C.

**W3-IO.3 [P1]** Zachowaj kontrolę wyniku `scanf` oraz poprawne `if` wykorzystywane jako zapowiedź W4; nie twórz pełnego drugiego wykładu z rozgałęzień.

**W3-LEGACY [P0]** Zweryfikuj wszystkie sekcje prezentacji i angielskiego notebooka: formaty i wartości zwrotne `printf`, szerokość/precyzja, znaki kontrolne, `scanf`, poprawne `&`, `math.h`, `pow`, `exp`, trygonometria, historyczny żart/ilustracja o `&`. Nie usuwaj utrwalonego żartu.

## 4. W4 — prace obowiązkowe

**W4-IF.1 [P0]** Dodaj zestawione bezpośrednio, w pełni objaśnione doświadczenia:
- `if (warunek) instrukcja;` — dotyczy **jednej instrukcji**, niezależnie od wcięć i podziału na linie;
- `if (warunek) { instrukcja1; instrukcja2; }` — cały blok;
- z `x` ustawionym tak, by pokazać różne wyniki;
- `if (warunek); { ... }` — pusta instrukcja spowodowana przypadkowym średnikiem, kod oznaczony jako antywzorzec;
- `if/else` i problem przypisania `else` do najbliższego niepowiązanego `if`, oraz dobra praktyka stosowania klamer.

**W4-IF.2 [P0]** Wprowadź *oddzielnie*:
- scope nazwy: `b` zadeklarowane w bloku `{...}` jest niewidoczne poza blokiem;
- czas życia obiektu lokalnego o automatycznym czasie przechowywania podczas wykonania bloku (nie utożsamiaj tego z zasięgiem nazwy);
- przesłanianie nazwy lokalnej/globalnej oraz zasięg parametrów funkcji;
- blok `{...}` tworzy zasięg także bez `if`;
- połączenie z W5: zmienna deklarowana w nagłówku `for` ma ograniczony zasięg.
Pokazuj **kompilowalne** przykłady oraz jawnie zakomentowany/oznaczony fragment o spodziewanym błędzie kompilacji przy użyciu nazwy poza zasięgiem.

**W4-IF.3 [P1]** Zadbaj o kontrast niezależnych `if` i łańcucha `if–else if–else`, `=` vs `==` i pułapki, tabele prawdy `&&/||/!`, de Morgana, priorytet `&&` vs `||`, short-circuit i dzielenie przez zero, `?:`, `switch`, `break/default`. Zachowaj proste historyczne przykłady, jeśli mają odrębną wartość dydaktyczną; nie kopiuj redundantnych wariantów bez celu.

**W4-PROC.1 [P0, WARUNEK KRYTYCZNY]** **Usuń z głównego przykładu równania kwadratowego `const char *wejscie` i `sscanf`**. Zbuduj dwa kolejno prezentowane, samodzielne programy C, rozwiązujące *identyczne zadanie*:
- A: **wyłącznie `main()`** — `scanf` współczynników liczbowych, kontrola wyniku odczytu, obsługa `a == 0`, wyróżnik, `if–else if–else`, pierwiastki/wynik oraz wydruk w `main()`. Brak własnych funkcji.
- B: wersja **proceduralna** z wyraźnym rozbiciem na logiczne etapy: wczytanie liczb, wyliczenie delty, decyzja o liczbie pierwiastków, obliczenie i wydruk. Nie kopiuj automatycznie wad historycznego przykładu (globalne `a,b,c` i nadpisywanie danych z `scanf` stałymi). Preferuj czytelne parametry wartościowe; jeśli zwrócenie kilku wyników wymagałoby nauczania wskaźników, dobierz API funkcji zachowujące poziom kursu, np. funkcja odczytu jednej liczby w `main()` z kontrolą sukcesu albo jawnie wydzielone funkcje obliczeń i wypisywania. Unikaj globalnego stanu jako domyślnego rozwiązania.
- Obie wersje mają obsługiwać **tę samą politykę przypadków**: co najmniej `a != 0` z `delta < 0`, `== 0`, `> 0`, błędne wejście, oraz `a == 0` (przypadek liniowy, równanie sprzeczne i tożsamościowe, jeśli wybrana taka polityka). Jednolite komunikaty i testy parytetu A/B.
- Wyjaśnij, dlaczego wersja proceduralna jest łatwiejsza do rozumienia, testowania, konserwacji i ponownego użycia; nie sugeruj, że ma inną matematykę.
- Pozostaw `sqrt` z `math.h` i linkowanie `-lm` tam, gdzie potrzebne. Nie zasłaniaj przekazu zbyt zaawansowanym kodem.
- Uwzględnij funkcje i prototypy, przekazywanie przez wartość, lokalność argumentów oraz związek z W1/W2. Rysunek przebiegu/dwa schematy mile widziane, ale nie są konieczne.

**W4-LEGACY [P0]** Historyczne `Lecture 4 examples.ipynb` ma osobne pokazy pojedynczej instrukcji i bloku pod `if`, zagnieżdżonych `if`, `switch`, wartości zwracanej i zmiennych globalnych oraz dwóch wariantów równania kwadratowego. Rozstrzygnij każdy punkt w macierzy pokrycia. Jeżeli prezentacja `lec4.tex/pdf` zawiera ujęcie deklaracji/prototypów i linkowania, sprawdź, czy W1/W4 zapewniają odpowiednią ciągłość.

## 5. W5 — prace obowiązkowe

**W5-LOOP.1 [P1]** Przywróć wartościowe kontrasty z historycznego notebooka: `i < 10` vs `i <= 10`, `++i` przed/po wydruku, `i += 2` vs sprawdzanie parzystości, odczyt licznika po zakończeniu pętli; skonfrontuj `while`, `do–while`, `for` i zasięg licznika. Krótkie pary kodu różniące się jedną cechą są lepsze niż duży program.

**W5-LOOP.2 [P1]** Przywróć doświadczenie numeryczne `float`: `x += h` vs `x = x0 + i*h` i konsekwencje akumulacji błędów zaokrągleń. Użyj z góry ograniczonej liczby iteracji, nie twórz nieskończonej pętli przy utracie postępu; połącz z W2.

**W5-LOOP.3 [P1]** Przywróć interaktywną grę „I win!” ze `scanf` i `while`/`break`, zamiast głównego wariantu `ruch(const char *tekst)` i `sscanf`. Sprawdzaj wynik `scanf` i unikaj zapętlenia na błędnym wejściu. Jeśli kernel Jupyter C nie obsługuje interakcji, daj oddzielny przykład terminalowy i deterministyczną demonstrację zachowania. Utrzymaj lekki humor.

**W5-LOOP.4 [P2]** Zachowaj i ewentualnie rozwiń szereg Fouriera: czytelne wytworzenie próbek, zależność od liczby wyrazów i kontrast sumowania/działania pętli.

**W5-LEGACY [P0]** Sprawdź kolejno wszystkie historyczne tematy: niepraktyczne ręczne powtarzanie, `goto` jako antywzorzec, `while`/`do–while`/`for`, parzyste/nieparzyste, zmienne licznika, `float`, pętle zagnieżdżone, pętle nieskończone, `break/continue`, gra, Fibonacci i Fourier. Sprawdź grafiki/schematy z PDF/TeX.

## 6. W1/W2 — przegląd i naprawy punktowe

**W1 [P2]** Potwierdź pokrycie: zasady organizacyjne z prezentacji (mogą pozostać poza notebookiem, ale odnotuj), pierwszy program, składnia/identyfikatory/słowa kluczowe, komentarze, `#include`, `#define`, etapy kompilacji/linkowanie, struktura `main`, prototypy, `void`, `return`, argumenty funkcji. Zachowaj celowo błędne przykłady z jednoznacznym oznaczeniem, zamiast udawać że każdy ma się kompilować.

**W2 [P2]** Potwierdź pokrycie: `int`/`float`/`double`/`char`/`bool`/`void`, granice typów, podstawy binarności/IEEE754, ASCII, arytmetyka całkowita, konwersja i rzutowanie, utrata informacji, priorytet operatorów, `++/--`, przypisania złożone. Kontrast `a/b` (int) i `(double)a/b`, prefiks/postfiks, zachowanie undefined behavior przy signed overflow i różnica między działaniem obserwowanym a gwarancją standardu. Nie usuwaj wartościowych rozszerzeń polskiej wersji.

## 7. Implementacja — ograniczenia

- Edytuj tylko niezbędne notebooki `1/Wykład 1.ipynb` … `5/Wykład 5.ipynb`, potrzebne lokalne grafiki/zasoby, ewentualnie adekwatne istniejące testy/checkery. Nie przepisuj niepowiązanych materiałów ani angielskich źródeł.
- Zachowaj `metadata.kernelspec.name = c`, strukturalną poprawność JSON/notebooka, sensowną kolejność komórek i brak przypadkowych zmian metadanych/masowych formatowań. Nowe teksty dla studentów wyłącznie w języku polskim (poza cytowanym kodem/oryginalnym żartem).
- Nie usuwaj ważnego doświadczenia tylko dlatego, że jest stare; połącz duplikaty, lecz zachowaj odmienny wniosek dydaktyczny.
- Używaj standardowego C11, `-Wall -Wextra -pedantic` dla poprawnych przykładów; nie uruchamiaj `gets` ani żadnego świadomie niebezpiecznego programu. Demonstracje błędów kompilacji oznacz i weryfikuj jako EXPECTED-FAIL, nie jako regresję.
- Utrzymuj przykłady interaktywne w terminalu i w notebooku jasno oznacz ich wymagania; nigdy nie blokuj interaktywnego kernela podczas automatycznych testów.
- Osobne checkpointy, małe commity. Nie merge do `master`. Materiały agentowe i raporty rozwojowe są **wyłącznie w tej gałęzi**.

## 8. Plan pracy i bramki jakości (CONTINUOUS)

**CP0 – preflight:** `git status`, `git branch --show-current`, `git rev-parse HEAD`, inwentarz plików, ustalenie dostępności PDF, tex, kompilatora C, kernela C, testów i grafik. Jeśli roboczy katalog nie jest czysty, nie nadpisuj cudzych zmian — użyj nowego worktree lub przerwij tylko w razie rzeczywistej blokady.

**CP1 – audyt porównawczy W1–W5:** kompletna macierz pokrycia dla notebooków + slajdów + grafik; wykryte braki i różnice priorytetyzuj. Przechowuj dowody w raportowaniu końcowym lub w ograniczonym, pojedynczym roboczym dokumencie, który nie trafi do `master`.

**CP2 – W3:** implementacja IO, kontrola spójności i testy; commit po PASS.

**CP3 – W4-IF:** instrukcja vs blok, średnik, scope/lifetime, układ rozgałęzień; testy; commit po PASS.

**CP4 – W4-PROC:** dwa pełne warianty równania, parytet przypadków, brak tekstowego parsowania; testy; commit po PASS.

**CP5 – W5:** kontrasty pętli, `float`, gra, Fourier; testy; commit po PASS.

**CP6 – W1/W2:** napraw wyłącznie potwierdzone braki/błędy, pozostałe oznacz jako PASS; commit tylko przy realnych zmianach.

**CP7 – audyt niezależny:** drugi agent/weryfikator lub osobne niezależne przejście sprawdza całą macierz pokrycia, zgodność W3→W4→W5, brak nierozpoznanych zależności i regresji. W razie FAIL napraw i powtórz.

**CP8 – odbiór:** testy struktury notebooków, testy C, demonstracje, grafiki, raport PASS/FAIL per wykład, SHA i lista commitów. Pozostaw gałąź gotową do selektywnego przeniesienia potrzebnych plików.

**Każdy checkpoint kończy się:** zmianami, listą testów z wynikami, ryzykami i jednoznacznym PASS/FAIL. **PASS powoduje automatyczne przejście do następnego etapu, bez oczekiwania na dodatkową wiadomość.**

## 9. Minimalny zestaw testów odbiorczych

1. Dla każdego notebooka: parsowanie `nbformat`, walidacja `nbformat.validate`, kernel `c`, brak przypadkowo uszkodzonych komórek, wszystkie referencje do lokalnych grafik istnieją.
2. Każdy nowy/zmieniony, poprawny przykład C: kompilacja C11 z ostrzeżeniami, `-lm` dla matematyki, test deterministyczny wyniku. Oddzielnie zanotuj przykłady celowo niekompilujące się i sprawdź spodziewaną diagnostykę.
3. W3: `puts` vs `fputs` różnica końca wiersza; `fgets` odczyt krótszy/równy/dłuższy od pojemności; żadnego użycia `gets` w wykonywalnym kodzie.
4. W4: dla ujemnego/dodatniego warunku potwierdź różnicę jednej instrukcji i bloku; pusta instrukcja po `if`; sprawdzenie błędnego odwołania poza zasięgiem (EXPECTED-FAIL); global/local shadowing.
5. W4: **identyczna semantyka A i B** dla co najmniej `(1,-3,2)`, `(1,2,1)`, `(1,0,1)`, `(0,2,-4)`, `(0,0,1)`, `(0,0,0)` i nieprawidłowego wejścia. Sprawdź status wyjścia, klasę wyniku i wartości liczbowe w tolerancji; nie opieraj testu wyłącznie na dokładnych stringach.
6. W5: `while/do–while` przy fałszywym warunku początkowym, granice licznika, `break/continue`, zakończenie interaktywnej gry przy poprawnych i błędnych danych, deterministyczne porównanie `float`.
7. Macierz pokrycia: żadnych nierozwiązanych MISSING dla treści kluczowych; każde INTENTIONALLY OMITTED uzasadnione, osobne UNVERIFIED dla PDF lub środowiska, którego nie można było przetestować.

Nie uznawaj kompilacji w GCC za dowód poprawnego działania kernela Jupyter C. Jeżeli kernel nie jest dostępny, pozostaw wyraźne UNVERIFIED i listę testów do odtworzenia, nie fałszuj PASS.

## 10. Kryterium finalne i integracja

Na końcu podaj:
- SHA bazowego `master`, SHA końcowy gałęzi, listę commitów oraz zmienionych notebooków/rysunków/testów;
- syntetyczną macierz pokrycia W1–W5 (osobno notebook i prezentacja);
- pełną listę dowodów/testów PASS, FAIL, UNVERIFIED, z krótką informacją jak odtworzyć;
- otwarte ryzyka i ewentualne świadome odstępstwa;
- **konkretną listę plików do cherry-pick/`git restore --source` w celu selektywnego przeniesienia do master**.

**Nie merge całej gałęzi.** Nie przenoś niniejszego `.md`, raportów roboczych, promptów agentowych, historii audytu ani innych plików rozwojowych do `master`. Przenosimy jedynie ostateczne polskie notebooki, konieczne dla nich grafiki i ewentualnie testy niezbędne do utrzymania wykładów.

## 11. Instrukcja startowa do lokalnego Codex

Pracuj autonomicznie w trybie CONTINUOUS na `feature/W1-W5-audyt-poprawki`. Przeczytaj CAŁY niniejszy kontrakt i źródła W1–W5, wykonaj checkpointy CP0→CP8, przechodź przez PASS bez czekania na „kontynuuj”, naprawiaj FAIL przed dalszą pracą. Nie zmieniaj `master` i nie merge. Zadbaj o najmniejszy konieczny zakres zmian, niezależną weryfikację i pełny raport końcowy. Jeżeli dostępne są lokalne instrukcje AGENTS.md, zastosuj je w zakresie niesprzecznym z tym kontraktem.
