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


## 12. Stan wykonania i dowody (wyłącznie ta gałąź)

Tryb CONTINUOUS, zakres CP0–CP8 zatwierdzony 2026-11-06. Koordynator odpowiada za integrację i testy. Stan Git zawsze sprawdzaj przez `git rev-parse HEAD`; dokument nie zawiera własnego SHA.

### CP0 — PASS

- Baza master: `9a42b0348e74c25795dad19a1bafc25f349a9d92`; wejściowy HEAD: `5b5b6c10f8f3fe7881066c68474d3b955bcdc9c0`.
- Czysty worktree: `/home/sgepner/.codex/worktrees/w1-w5-audit/Lecture`, gałąź `feature/W1-W5-audyt-poprawki`. Pierwotny katalog pozostawiony na odłączonym wejściowym HEAD; wszystkie istniejące zmiany i pliki nieśledzone zachowane. Kopia diffu: `/tmp/w1-w5-audit/original-local.patch`. Audyt i wdrożenie dotyczą wersji zapisanej w Git, nie lokalnych niezatwierdzonych edycji.
- Komplet 20/20 wskazanych plików źródłowych istnieje. Brak lokalnych AGENTS/CURRENT/ROADMAP/DECISIONS; niniejszy kontrakt jest jedynym planem i rejestrem.
- GCC 11.4.0, Python 3.10, nbformat i jupyter_client dostępne. Kernel C uruchomiony z istniejącego `/home/sgepner/Virtualenv/jupyter/bin/python`; rzeczywisty test Jupyter zwrócił `C_KERNEL_OK`. Tymczasowy kernelspec: `/tmp/w1-w5-audit/jupyter/kernels/c/kernel.json`; bez zmiany konfiguracji użytkownika. Lokalna komunikacja kernela wymaga uruchomienia poza ograniczeniem gniazd sandboxa.
- PDF: tekst wszystkich stron odczytany; `/usr/bin/pdftoppm` wyrenderował 17/20/13/12/16 stron. Koordynator obejrzał zestawienia wszystkich stron; drobne szczegóły kodu sprawdzane w TeX/tekście. Bundlowany renderer ma konflikt GLIBC, rozwiązany użyciem systemowego.
- Istniejące `2/check_w2.py` i `3/check_w3.py` wykryły niezgodne liczby komórek już na wejściu (134 zamiast 133; 25 zamiast 22). To ustalenie bazowe, nie PASS regresji; naprawa w CP6/CP2 przy zachowaniu dotychczasowych wyroczni wyników.
- Dowody i ekstrakty robocze: `/tmp/w1-w5-audit/`. Następny checkpoint: CP1, pełna macierz.

### CP1 — PASS (inwentarz audytu, nie odbiór niepoprawionych wykładów)

Macierze poniżej dotyczą wejściowego SHA `5b5b6c10f8f3fe7881066c68474d3b955bcdc9c0`; indeksy komórek od zera. Każda komórka źródłowa i każdy istotny temat slajdów ma przypisanie. MISSING jest listą prac CP2–CP6 i musi zniknąć przed CP8. Dowody CP0 rozwiązują ograniczenie oględzin PDF odnotowane przez recenzentów; koordynator obejrzał wszystkie 78 stron w zestawieniach.

Role: `audit_w1_w2` — rzeczywisty agent_type `doc_clerk` (konfiguracja roli: gpt-6-luna/low), mechaniczna macierz W1/W2; `audit_w3_w5` — `independent_reviewer` (gpt-6.1-sol/medium), niezależna macierz W3–W5. Nie edytowali repozytorium. Obaj ukończyli raporty źródłowe; dalsza próba pracy zakończyła się komunikatem braku kredytów. CP7 wykona osobne przejście recenzenckie koordynatora, jeżeli agent pozostanie niedostępny; kontrakt dopuszcza tę formę.

Uściślenia koordynatora: W2 końcowe `printf`/wartość zwracana jest MOVED do W3 komórek 3–5; `sizeof(int)` z W1 jest MOVED do W2 komórek 8/11. W2 c19 nie zawiera obecnie duplikatu — nie zmieniać. W1 ma 24 komórki kodu, ostatnia w indeksie 79, nie 80; poniższa dodatkowa klasyfikacja c80 recenzenta nie stanowi dowodu. Ciągłość linkowania: W1 c14–20 (etapy kompilacji), c69–70 (prototyp i definicja), W4 CP4 dopowie kompilację osobnych plików. Powtórki operatorów W3 są MOVED do W2 c115–129, arytmetyka do W2 c44–53, konwersje do W2 c74–83.

# CP1 comparative audit — W1/W2

Scope: W1/W2 only, per assignment. Contract read in full at `Lecture/W1_W5_AUDYT_POPRAWKI_AGENT_CONTRACT.md`. Sources: English notebooks, Polish notebooks, `lec1.tex`/`lec1.pdf`, `lec2.tex`/`lec2.pdf`. Notebook text inventories are `/tmp/w1-w5-audit/w1-{en,pl,pdf}.txt` and `w2-{en,pl,pdf}.txt`; PDF text extraction covers the provided extracted document text. Coordinator reports rendered and visually inspected contact sheets of all PDF pages using `/usr/bin/pdftoppm`; PDF page visuals are coordinator-reviewed. TeX frame inventory from source.

## W1 matrix

| English source | Polish destination | Status | Notes |
|---|---|---|---|
| EN cells 0–2: Hello World, accept unexplained syntax, compile via gcc, staged preprocessing/compiler/assembler/linker, Godbolt | PL 9–21 | EXTENDED | Stages elaborated; diagram `GCC_CompilationProcess.png` and path local. Includes executable command paths `1/hello/hello.c`; verify environment/path operation later if needed. |
| EN 3–19: basic elements, case sensitivity, brackets, names, keyword/case distinction, underscore, leading digit | PL 22–40 | COVERED/EXTENDED | Same positive/negative samples; expanded allowable characters and C89 keyword list. Negative snippets intentionally noncompiling. |
| EN 20–23: comments and annotated Hello World | PL 41–45 | EXTENDED | Includes joke comment plus humorous maintainer comment. |
| EN 24–29: preprocessor, `#include`, stdio explanation, `main`, single entry | PL 46–52 | EXTENDED | `main` duplicate deliberately presented as error; PL 51 has duplicate main. |
| EN 30–38: `#define`, PI example, textual replacement danger (`da main`) | PL 53–61 | EXTENDED | Demonstrates macro substitution and link-time missing entry point. `#define PI 3` with `%d` is internally format-consistent, albeit poor PI naming/value; introduced as “good approximation” joke. |
| EN 39: procedural paradigm intro | PL 64 | EXTENDED | More precise introductory framing. |
| EN 40–43: unknown function, define sum, declaration/prototype vs later definition | PL 65–70 | EXTENDED | Adds explicit `void`, `return 0`, distinction between definition and prototype. |
| EN 44–49: sum evolves to parameters, return value, ignored/used/assigned | PL 71–79 | EXTENDED | Explicitly stages procedure and return semantics. |
| EN 50: `sizeof(int)` output example | W2 PL cells 8 and 11 | MOVED | Direct `sizeof(int)` experiment and type-size comparison. |

### W1 TeX/PDF substantive frame mapping

Frames treated as overlay/repetition groups where content accumulates:

- Title/administrative (`lec1.pdf` opening and `lec1.tex` title, `Rules and Regulations`) → PL 0–3 plus separate `1/Rulesandregulations.pdf`; course logistics intentionally stay outside notebook: INTENTIONALLY OMITTED (separate handout).
- Resources frame → PL 2, 21 (practice/Godbolt); exact resource list not retained: INTENTIONALLY OMITTED as non-core duplicative resource listing.
- Programming/history (Ada/Babbage) → PL 4–5, EXTENDED.
- C history, standard timeline, uses, descendants/operator syntax → PL 6–7, EXTENDED.
- First program and compilation → PL 8–21, EXTENDED; compiler graphic included (local).
- Basic C characters → PL 23; keywords and valid identifiers → PL 29–40, COVERED/EXTENDED.
- Comments, including Stack Overflow “42 hours” joke → PL 41–45; humorous comment retained with wording variation, COVERED.
- Program structure frames (header, macro PI, main, braces/body, extra function and prototype/global variable example) → PL 46–50, 53–79; EXTENDED. The standalone legacy global-variable example is not repeated, but function parameters/return are expanded; global variable is not a W1 learning objective: INTENTIONALLY OMITTED.
- Headers → PL 49, EXTENDED (more precise include-search explanation).
- Functions frame → PL 63–79, EXTENDED.

Graphics inventory: `1/Ada_Lovelace_portrait.jpg` (referenced in PL cell 5; source attribution there); `1/GCC_CompilationProcess.png` (PL cell 14); `1/therecanbeonlyone.jpg` (PL cell 52). All exist beside notebook. `Rulesandregulations.pdf` is separate and exists. No other graphics referenced by W1 sources found in TeX/notebook scan. Visual appearance of PDF pages coordinator-reviewed. Notebook image rendering/offline display not separately verified.

## W2 matrix

| English source | Polish destination | Status | Notes |
|---|---|---|---|
| EN 0–3: review of W1; main and `int` | PL 0–4, 2–3 | EXTENDED | Uses W1 sum example to bridge into types. |
| EN 4–21: `int`, size, initialization, integer formats, octal/hex, range/overflow, integer ops/division | PL 5–51 (W2.2–2.5) | EXTENDED | Far more detailed and careful. Historical defects corrected conceptually (e.g. size_t `%zu`, signed overflow UB); see fixes below. |
| EN 22–34: float/double sizes, formatting/arithmetic, integer division vs cast | PL 52–72 and 73–85 | EXTENDED | Adds `float`/`double` representation, precision, conversions, format correctness. |
| EN 35–37: char/ASCII, numeric and control chars, null, single/double quotes | PL 87–97 | EXTENDED | Full ASCII table, `'0'`/`0`/`"0"`, signedness. |
| EN 38–39: bool, `stdbool.h`, true/false | PL 98–105 | EXTENDED | Includes bool normalization and size discussion. |
| EN 40–41: void, invalid object/sizeof | PL 106–114 | EXTENDED | Correctly frames invalid `sizeof(void)`/void object as expected error. |
| EN 42–46: assignments, implicit/explicit conversion, loss | PL 73–86 | EXTENDED | More targeted sequence and explicit format-mismatch warning. |
| EN 47–48: precedence examples | PL 115–120 | EXTENDED | Additional expression examples. |
| EN 49–57: increment/decrement, prefix/postfix examples and claim prefix efficient | PL 121–126 | EXTENDED / INTENTIONALLY OMITTED | Core behaviors covered. Historical claim that prefix is more efficient for primitive int omitted; not needed to teach semantics. |
| EN 58–60: compound assignments | PL 127–129 | EXTENDED | Adds modulo form. |
| EN 61–66: functions, prototypes, return values, `printf` return example | PL W1 63–79; W3 PL cells 3–5 | MOVED/EXTENDED | Function return fundamentals are in W1; `printf` return count is explicitly taught in W3. |

### W2 TeX/PDF substantive frame mapping

- Opening/review and function recap → PL 0–4, EXTENDED.
- “Program” frame with deliberately broken missing semicolons/format argument → PL W1 63–79 and W2 106–114, learning content covered; malformed composite sample intentionally not copied: INTENTIONALLY OMITTED because isolated syntactic defects are not needed here.
- Data types framing/sizeof portability → PL W2 5–13, EXTENDED.
- `int` formats, octal/hex, arithmetic and division → PL 17–51, EXTENDED.
- Float/double ranges, formatting, math PI with `atan`, arithmetic → PL 52–72, EXTENDED. Historical assertions that fixed sizes/ranges are universal are qualified in PL.
- Char and ASCII → PL 87–97, EXTENDED. Bad legacy assignment `char a = "R"` is not copied; proper distinctions are taught in PL.
- Bool → PL 98–105, EXTENDED. Bool true/false output is covered; optional ternary text rendering is not a separate requirement.
- Void / function no args/return → PL 106–114, EXTENDED; does not run invalid legacy code.
- Assignment/conversion/casting → PL 73–86, EXTENDED.
- Operator precedence → PL 115–120, EXTENDED.
- Prefix/postfix increment/decrement → PL 121–126, EXTENDED; inaccurate efficiency assertion intentionally omitted.

## W1/W2 graphics and files

- W1 graphics: `1/Ada_Lovelace_portrait.jpg`, `1/GCC_CompilationProcess.png`, `1/therecanbeonlyone.jpg` all present, referenced by Polish notebook using same-directory relative paths. Visual display/offline rendering UNVERIFIED.
- W2 TeX contains no `\\includegraphics`; notebook has no image reference in extracted text. Supplementary binary/IEEE754 PDF and helper notebook exist at `2/materialy_pomocnicze/` but are not listed as canonical W2 source in contract; their coverage/use is outside this subtask.

## Concrete W1/W2 errors / minimal CP6 attention

1. **W2 Polish cell 27**: example is described as corrected/initialized, but assignments `b = 10;` and `c = 40;` are commented out. The cell therefore reads uninitialized automatic variables. Minimal CP6 fix: uncomment assignments or initialize declarations; align the observation in cell 28. This is the only confirmed W1/W2 code defect from this mechanical audit.
2. **W2 Polish cell 5** reference command uses `-Werror`; describe as a strict command for valid examples if appropriate, since later cells intentionally show malformed/diagnostic cases. This is optional clarification, not a confirmed defect.
3. **W2 cells 57–64** contain extensive IEEE binary32/binary64 encodings. Mapping confirms their presence; no scientific correctness claim is made by this mechanical audit. Escalate any suspected technical inconsistency to coordinator.
4. PDF visuals: coordinator rendered and inspected all PDF page contact sheets; visual status is reviewed, not UNVERIFIED. Notebook-local image rendering still not tested.

## CP1 W1/W2 conclusion

Coverage is strong; no substantive English notebook or TeX topic is clearly MISSING for W1/W2, with intentional relocation/omission documented above. CP6 recommendation: correct W2 cell 27 initialization only. W1 graphics files exist; their files and PDF visuals are reviewed, but notebook-local rendering/offline display has not been tested. No repo files edited.


## W1 Polish code-cell execution classification

The following classifies every W1 Polish code cell in the extracted notebook. “Expected diagnostic” states the language/toolchain-level failure category (exact wording varies by compiler/version); all malformed examples are explicitly preceded by a Polish warning/instruction. No unsafe or destructive code found.

| PL cell | Class | Preceding Polish label / expected diagnostic |
|---|---|---|
| 10 | Valid full program (pedagogical omission of explicit return is valid for `main`) | Cell 9 introduces Hello World. |
| 25 | Expected link error | Cell 24 says casing is intentionally wrong. `Main` is not the required `main`; compilation can produce an object, link fails for missing entry point (`undefined reference to main`). |
| 26 | Expected compile/link error | Cell 24 introduces wrong case. `Printf` is undeclared in C11 (diagnostic: implicit declaration / undeclared identifier; with strict C11 `-Werror`, compile fails); otherwise link fails with undefined reference to `Printf`. |
| 28 | Expected compile error | Cell 27 explicitly says brackets are intentionally mixed. Parser errors: expected `(` after `main`, then invalid function/body syntax / expected declaration. |
| 31 | Valid fragment | Cell 30 introduces an `int` declaration. Not a standalone program; valid function-body declaration. |
| 34 | Expected compile error | Cell 33 labels reserved keyword attempt. `double` cannot be identifier; diagnostic expected identifier before `double`. |
| 36 | Valid full program | Cell 35 asks why capitalized `Double` is allowed; valid. |
| 38 | Valid full program | Cell 37 introduces underscore names; valid. |
| 40 | Expected compile error | Cell 39 explicitly says identifier may not start with digit. Parser/lexer diagnostics around invalid numeric token `9_myVariable` (invalid suffix / expected `,`, `;`, or identifier). |
| 42 | Valid fragment | Cell 41 describes comment syntax. Only comments; no translation-unit declaration needed. |
| 45 | Valid full program | Cell 44 introduces commented Hello World. |
| 47 | Valid fragment | Cell 46 labels `#include`; directive is valid as an isolated preprocessing fragment. |
| 51 | Expected compile error | Cell 50 explicitly states only one `main`; contains duplicate definitions. Diagnostic: redefinition of `main` (points to prior definition). |
| 54 | Valid preprocessing fragment | Cell 53 introduces `#define`; valid directive, not a full program. |
| 56 | Valid full program | Cell 55 calls this an example of `#define`; `%d` matches macro replacement integer 3. |
| 58 | Expected link error (after macro expansion) | Cell 57 warns about textual replacement; code itself is not preceded by explicit “do not compile,” though cell 59 explains the result. `#define main da` removes `main`; translation unit can compile, linker reports missing `main`. This is pedagogical expected failure and clearly explained immediately after, but not labeled before execution. |
| 60 | Valid fragment showing preprocessed output | Cell 59 explicitly introduces simplified post-preprocessing fragment. |
| 65 | Expected compile/link error | Cell 64 introduces unknown `sum`; preceding cell 64 says compiler does not know function. In C11, undeclared `sum` violates constraints (diagnostic required; with strict flags compilation fails); permissive compiler may proceed then linker reports undefined `sum`. |
| 67 | Valid full program | Cell 66 directs placing definition before `main`; definition and call valid. |
| 70 | Valid full program | Cell 69 introduces prototype then later definition; valid. |
| 72 | Valid full program | Cell 71 introduces arguments passed by value; valid. |
| 75 | Valid full program | Cell 74 introduces return value. Return value ignored intentionally. |
| 77 | Valid full program | Cell 76 introduces using return value in `printf`; valid. |
| 79 | Valid full program | Cell 78 introduces storing result; valid. |
| 80 | Valid full program | Closing/checkpoint cell after summary; `sizeof(int)` printed with `%d` after explicit cast to int; valid. |

Unsafe code scan: no buffer overflow, invalid pointer dereference, division by zero, uninitialized read, or unsafe library call identified in W1 Polish code cells. Expected compile/link failures are confined to cells explicitly meant to demonstrate syntax/name/entry-point errors; cell 58 is explained immediately afterward but could be given an explicit pre-run label if notebook polish permits.


# CP1 independent audit W3–W5
Read-only repository audit at `5b5b6c10f8f3fe7881066c68474d3b955bcdc9c0`. Reviewer role: independent_reviewer; no repository edits. All English and Polish cell source, complete lec3/4/5.tex and extracted PDF text read. Cell indices below are zero based and refer to CP1 snapshot extracts `/tmp/w1-w5-audit/wN-{en,pl,pdf}.txt`. Source outputs were not used as numerical proof. PDF text coverage verified; rendered PDF layout and embedded animation playback UNVERIFIED. No C execution or kernel verification belongs to this CP1 review.
## Required corrections

- CP2 P0: teach puts/fputs/gets/fgets including buffer, NUL, newline and failure semantics; add deterministic newline and fgets short/equal/long tests. No executable gets. Fix W3 c27 false heading (two-field complete success is 2). Convert c24 unguarded interactive scanf code to terminal-only text or checked deterministic demonstration. Remove project/history wording from c21, c23 alt and c49; preserve joke and mathematical meaning.
- CP3 P0: explicit adjacent one-statement vs block programs for both condition signs, empty statement after if, dangling else rule, standalone block scope, parameter scope, automatic lifetime distinct from visibility, shadowing and EXPECTED-FAIL out-of-scope test. Preserve logical/short-circuit extensions.
- CP4 P0: replace c37 text parser with two identical-task complete numeric scanf programs A main-only and B procedural, no global state, same complete case policy/status/messages, explicit prototypes, return-value example, and decomposition benefits. Keep clear terminal-only requirements. Verify numerical semantics of both versions, not just their agreement. W4 c32 explains return but lacks a simple executed value-return assignment example (legacy c41/45); add or explicitly cross-reference verified W1 cells. Explain static if retained in helper declarations, or omit it at this level.
- CP5 P1: bounded float accumulation vs index experiment, explicit parity step/filter code contrast (currently merely exercises), actual while/scanf/break game and deterministic runs using that same program; retain all W5 extensions/Fourier. Remove duplicate stranded “liczby pierwsze” heading in c59. W5 c28 heading “która zmienna nadal istnieje” conflates visibility with lifetime; clarify.
- W4 PDF final frame contains incorrect claim C permits overloading, and typo fun1(5,7) vs fun2: intentionally correct rather than reproduce. W5 Fourier PDF and legacy c61–63 sum all harmonics: this differs from square-wave series; preserve lesson using corrected odd harmonics and explicit N definition, already done in Polish.
## English notebook cell matrix

Every source cell occurs once below. COVERED means its educational topic exists, not all literal code is preserved. Exercise-only coverage is explicitly identified and may still require improvement under contract.

### W3

| English cell(s) | Polish destination cells | Status | Evidence / resolution |
|---|---|---|---|
| 0 | 1; W2 | MOVED | Type recap retained briefly; full simple types belong to W2. |
| 1 | 6–8 | COVERED | int/double/char formatted output. |
| 2–3 | 1; W2 | MOVED | Arithmetic, increment, compound assignment, remainder, integer vs cast division; W2 primary destination, independently audited by W1/W2 reviewer. |
| 4–5 | 3–5 | EXTENDED | printf declaration, stdout, return count and negative error. |
| 6–7 | 10–13,16–17 | EXTENDED | Flags, minimum width, integer precision, overflow width. |
| 8 | 12–15 | COVERED | Floating width/precision and scientific output. |
| 9–10 | 18–21 | EXTENDED | Control characters and terminal byte observation; corrected v/newline misconception. |
| 11 | 22–23 | EXTENDED | scanf, address, original image/joke; correct return meaning. |
| 12 | 24–26,35,40–42 | COVERED | Single int input; c24 currently unsafe notebook placement and unchecked result, fix CP2. |
| 13 | 27–35,42 | EXTENDED | int/double input, partial success/EOF; c27 heading incorrect. |
| 14–15 | 43,49–52 | EXTENDED | math.h, trig and radians. |
| 16–17 | 43–44 | COVERED | pow integer exponent. |
| 18 | 45,47–48 | EXTENDED | Negative fractional power with positive base and domain. |
| 19–20 | 45–48 | COVERED | exp and exp(x+y). |
| 21 | 45,47 | COVERED | Prefer exp rather than pow(exp(1),...). |
| 22 | 44–48 | EXTENDED | exp/log/log10/pow/sqrt with domains. |
| 23 | 49–50 | COVERED | PI from atan explained; acos(-1) chosen in code, macro prerequisite from W1. |
| 24 | 57 | EXTENDED | All name/ID/input/arithmetic/math exercises retained. |

Polish cell index / stable ID lookup (all destination cells):

0=`ac9e6834`, 1=`61177174`, 2=`6e0ae160`, 3=`34abbd04`, 4=`563b69c7`, 5=`7ac96c2f`, 6=`cf166ec2`, 7=`d7a2005b-6d6b-4136-b9a6-cfdaa86de247`, 8=`ec80c0c2`, 9=`39e4baab`, 10=`f124da40`, 11=`21f43340`, 12=`0eb3823e`, 13=`1136a8d3`, 14=`da83cd82`, 15=`f68f01fc`, 16=`d08e0a04`, 17=`72ab0f21`, 18=`56810979`, 19=`dc115699`, 20=`f8a49a45-8d4a-45e8-860a-7765224b4b4c`, 21=`4d30bc04`, 22=`a1966700`, 23=`49887456`, 24=`8a3d1998-fe53-4e6b-a833-96a6f4b1dc00`, 25=`f7200a4e`, 26=`36ebf919`, 27=`a5aa0641`, 28=`6cd2d612`, 29=`19556362`, 30=`668b6ff2`, 31=`64562ecc`, 32=`449e5bad`, 33=`59b1bdd3`, 34=`6c75fd0b`, 35=`bc5ff25c`, 36=`10ee39d1`, 37=`8c404d7f`, 38=`41cfcc24`, 39=`1d57b6bf`, 40=`1755e83d`, 41=`8fed68d0`, 42=`8a78cd53`, 43=`f0d4c144`, 44=`b1939165`, 45=`02e6c393`, 46=`f9d6cf59`, 47=`38101f2b`, 48=`b141698c`, 49=`10ffb63e`, 50=`4ac22ab3`, 51=`021df52c`, 52=`92df2ded`, 53=`cd33f9b7`, 54=`80ab5835`, 55=`ff14e679`, 56=`1be31e84`, 57=`971d753d`, 58=`e607df67`, 59=`9a83bde6-4b6e-42bd-92cf-2f8e7ded6b58`

### W4

| English cell(s) | Polish destination cells | Status | Evidence / resolution |
|---|---|---|---|
| 0 | 0,26,29,36 | COVERED | Branching and quadratic goal. |
| 1–3 | 1,5,8–9 | COVERED | Relational values and negation; ! vs relational precedence implicit, explicit example useful. |
| 4–8 | 3–5,20 | MISSING | Nonzero truth/block examples exist but single statement vs braces controlled contrast absent. |
| 9–10 | 1,5–7 | COVERED | Comparison value stored in int; statement/block issue handled in missing row above. |
| 11 | 3,20–21 | MISSING | Comparison branches covered; commented accidental-semicolon warning has no explicit experiment. |
| 12–14 | 1,23–25 | COVERED | Equality vs assignment, printed results. |
| 15–16 | 6–11 | EXTENDED | AND/OR/NOT plus truth tables and de Morgan. |
| 17–18 | 12–13 | EXTENDED | AND before OR, parenthesis contrast. |
| 19–20 | 19–20 | COVERED | if/else. |
| 21–23 | 19,21 | COVERED | Independent if vs else-if chain; source equality-boundary exercise consolidated. |
| 24–25 | 22 | COVERED | Nested branches; dangling-else narrative still required by CP3. |
| 26–29 | 26–28 | COVERED | if/else vs conditional expression same arithmetic. |
| 30–32 | 29–31 | COVERED | Integer switch, expression switch, break/default. |
| 33–34 | 36–37 | MISSING | Quadratic mathematics covered but main-only full program missing; current parser is prohibited by contract. |
| 35–36 | 32–33 | MISSING | Functions mentioned; substantive procedural-decomposition rationale and type/return progression too compressed. |
| 37 | 32–33 | COVERED | Invalid generic function syntax intentionally replaced by real C definition. |
| 38–40 | 32–33 | COVERED | Function call and void no-result counterpart; int no-argument function is also prerequisite in W1. |
| 41–42 | 32–33 | MISSING | By-value covered; simple executed returned-value assignment missing here, verify W1 or restore. |
| 43–44 | 32–33 | COVERED | By-value mutation does not mutate caller. |
| 45 | 32; W1 | UNVERIFIED | Returned-value assignment not demonstrated in W4; must verify exact W1 destination or add. |
| 46–48 | 34–35 | COVERED | Global state mutated by function; avoid as default design. |
| 49–51 | 34–35 | COVERED | Global/local shadowing. |
| 52–54 | 36–37 | MISSING | No procedural decomposition solver; correct legacy global-state and overwritten-input defects, do not copy. |
| 55–56 | 32 | COVERED | No overloading explicitly stated; broken duplicate-definition cell intentionally replaced by prose. |
| 57 | — | INTENTIONALLY OMITTED | Empty source cell. |

Polish cell index / stable ID lookup (all destination cells):

0=`e94ad798`, 1=`w4-int1-logical-intro`, 2=`1d08c690`, 3=`61d45c4a`, 4=`e81143cc`, 5=`33806cd2`, 6=`2c5b3ee2`, 7=`4bfe372e`, 8=`14c6cddf`, 9=`2e32f995`, 10=`7400c472`, 11=`ae30e57f`, 12=`b901711b`, 13=`1a2c80e2`, 14=`2fe4a973`, 15=`ebedf0a8`, 16=`c29eced9`, 17=`7c7e8639`, 18=`1d870c1d`, 19=`f40ddaae`, 20=`w4-branch-blocks`, 21=`w4-branch-independent-chain`, 22=`w4-branch-nested-else`, 23=`796328b8-a5dc-4224-bc3d-9d1e6e8333cf`, 24=`w4-branch-assignment`, 25=`w4-branch-assignment-note`, 26=`2303c3fc`, 27=`dd027695-8bf4-47cb-85da-bf44f5163516`, 28=`373cbd16-59af-4dde-93fd-4d423a66de4c`, 29=`9fffc9ba`, 30=`44960722-9222-433e-8af8-0b53ec184a3b`, 31=`b19c4849-ad7f-41c8-b464-181c394837b7`, 32=`w4-functions-supplement`, 33=`w4-functions-value-scope`, 34=`w4-int3-global-note`, 35=`w4-int3-global-shadow`, 36=`7688fa03`, 37=`w4-quadratic-decision-tree`, 38=`ac2d7f8e`

### W5

| English cell(s) | Polish destination cells | Status | Evidence / resolution |
|---|---|---|---|
| 0 | 0,4–5 | COVERED | Purpose of loops, sequence and diagrams. |
| 1–2 | 2 | COVERED | Manual repetition explained in prose, repeated printf block omitted as redundant. |
| 3–5 | 3–5 | EXTENDED | goto label example and comic; avoids scientifically false blanket claim every goto is poor programming. |
| 6–7 | 6–10 | EXTENDED | while pretest, counter and state. |
| 8 | 25–26 | COVERED | < vs <= contrast moved from while to for; same boundary lesson. |
| 9 | 27–28 | COVERED | Increment-before-print vs after; explicit prefix/postfix stronger contrast. |
| 10–12 | 11–15 | EXTENDED | do-while prefalse comparison and required semicolon. |
| 13–18 | 61 | MISSING | Parity while/do-while/filter/step-2 topics present only as exercise; no executable short contrast. |
| 19–21 | 16–22 | EXTENDED | for lifecycle, omitted fields, equivalence caveat with continue. |
| 22–23 | 28–30 | EXTENDED | Scope and intentionally failing i/j fragment retained as non-executable text. |
| 24 | 29–30 | COVERED | Value retained outside loop; j terminal counter example plus narrative; copying last printed value exercise can be inferred. |
| 25–27 | 25–30 | EXTENDED | Postloop counter and nested shadowing. |
| 28–30 | 30–32 | MISSING | double indexed grid present but float repeated addition versus index experiment absent. |
| 31–34 | 33–36 | EXTENDED | 4x5 table, reset j, 20 executions, readability. |
| 35 | 46–47 | EXTENDED | Infinite loops distinguished from loops with break and guaranteed termination. |
| 36–38 | 37–41,61 | COVERED | break and print placement; multiple-of-three variant retained as exercise. |
| 39–40 | 61 | COVERED | Stop before 14 exercise; canonical break program in c40 teaches same mechanism. |
| 41–42 | 40–43,61 | EXTENDED | continue target correctly explained for for/while/do-while; mod3 as exercise. |
| 43–45 | 61 | COVERED | Skip multiples 7/3 consolidated as exercises; c40 runnable same continue mechanism. |
| 46–49 | 61 | MISSING | step-2 vs continue parity only exercise; restore short executable pair. |
| 50–53 | 61 | COVERED | Odd numbers excluding multiples 9, both solution methods requested; canonical mechanism demonstrated elsewhere. |
| 54–55 | 55–57 | MISSING | Game preserved as text-parsing function without loop; terminal wrapper uses strtol instead of teaching while/scanf/break. |
| 56–57 | 49–51 | EXTENDED | Fibonacci state invariant, first ten and overflow bounds. |
| 58–60 | 57–59 | EXTENDED | Square Fourier odd-harmonic sum, sampling, N semantics and illustrations. |
| 61–63 | 57–59 | INTENTIONALLY OMITTED | All-harmonic variants do not compute declared square-wave series; corrected odd-harmonic lesson subsumes function/prototype/sampling differences, bounded indexed coordinate from c31. |
| 64 | — | INTENTIONALLY OMITTED | Empty source cell. |

Polish cell index / stable ID lookup (all destination cells):

0=`(no id)`, 1=`(no id)`, 2=`(no id)`, 3=`(no id)`, 4=`(no id)`, 5=`(no id)`, 6=`(no id)`, 7=`(no id)`, 8=`(no id)`, 9=`(no id)`, 10=`(no id)`, 11=`(no id)`, 12=`(no id)`, 13=`(no id)`, 14=`(no id)`, 15=`(no id)`, 16=`(no id)`, 17=`(no id)`, 18=`(no id)`, 19=`(no id)`, 20=`(no id)`, 21=`(no id)`, 22=`(no id)`, 23=`(no id)`, 24=`(no id)`, 25=`(no id)`, 26=`(no id)`, 27=`(no id)`, 28=`(no id)`, 29=`(no id)`, 30=`(no id)`, 31=`(no id)`, 32=`(no id)`, 33=`(no id)`, 34=`(no id)`, 35=`(no id)`, 36=`(no id)`, 37=`(no id)`, 38=`(no id)`, 39=`(no id)`, 40=`(no id)`, 41=`(no id)`, 42=`(no id)`, 43=`(no id)`, 44=`(no id)`, 45=`(no id)`, 46=`(no id)`, 47=`(no id)`, 48=`(no id)`, 49=`(no id)`, 50=`(no id)`, 51=`(no id)`, 52=`(no id)`, 53=`(no id)`, 54=`(no id)`, 55=`(no id)`, 56=`(no id)`, 57=`(no id)`, 58=`(no id)`, 59=`(no id)`, 60=`(no id)`, 61=`(no id)`

## PDF/TeX frame matrix

PDF pages counted from form-feed separated extraction: W3=13, W4=12, W5=16. Page numbers below are 1-based. TeX titlepage counts as page 1; repeated titled frames are individually listed or explicitly grouped; no overlay-only additional pages in these PDF text inventories. W4 commented-out printf/scanf frame and W5 commented-out test-announcement frame are inactive TeX, intentionally omitted as stale logistics/duplication. PDF and TeX agree in substantive topic order; corrections/divergences are identified below.

| Source frame / PDF page | Polish destination | Status | Evidence / qualification |
|---|---|---|---|
| W3 p1 title | W3 c0 | COVERED | Lecture title retained in Polish. |
| W3 p2 We know types | W3 c1; W2 | MOVED | Full type recap belongs to W2; exact W2 cells audited separately. |
| W3 p3 Variables | W3 c1; W2; W3 c43–44 | MOVED | Assignment and arithmetic in W2; sqrt in W3. PDF quadratic snippet replaced in TeX by valid simple arithmetic. |
| W3 p4 Substitution | W3 c1; W2 | MOVED | Conversion/information loss and casting; PDF says avoid mixed types, TeX correctly describes conversion. |
| W3 p5 Precedence | W2; W3 c1 | MOVED | Arithmetic priority prerequisite, W1/W2 independent audit must resolve exact cell. |
| W3 p6 Increment/decrement | W2; W5 c27–28 | MOVED | Prefix/postfix retained as prior concept then loop experiment. |
| W3 p7 Compound Assignment | W2 | MOVED | PDF mistaken RHS/LHS wording corrected in TeX; verify W2 coverage. |
| W3 p8 printf | W3 c3–8 | EXTENDED | stdout, return, all listed format types, promotion and UB. |
| W3 p9 printf new stuff | W3 c10–17 | EXTENDED | flags/width/all precision categories. |
| W3 p10 cursor control | W3 c18–21 | EXTENDED | Correct control character semantics and byte observation. |
| W3 p11 scanf + joke | W3 c22–42 | EXTENDED | PDF false character-count return corrected; illustration preserved. |
| W3 p12 math trig | W3 c43,49–52 | EXTENDED | Full function families, radians, domains; PDF atan2 typo corrected. |
| W3 p13 math other | W3 c43–48,51 | EXTENDED | exp/log/log10/pow/sqrt/ceil/fabs/floor and exp idiom. |
| W4 p1 title | W4 c0 | COVERED | Polish framing. |
| W4 p2 Code branching | W4 c0,26,29 | COVERED | All three constructs. |
| W4 p3 if truth/relations | W4 c1,3–5,23–25 | COVERED | Nonzero truth, relations, assignment warning. |
| W4 p4 AND and OR | W4 c6–17 | EXTENDED | Truth tables, de Morgan, priority, short circuit. |
| W4 p5 Basic if syntax | W4 c3,20–22 | MISSING | Single-statement syntax used but absent controlled braces comparison. |
| W4 p6 What else | W4 c19–22 | COVERED | if/else syntax and program. |
| W4 p7 else if | W4 c19,21 | COVERED | Chain vs independent decisions. |
| W4 p8 Inline if | W4 c26–28 | COVERED | Same arithmetic pair; distinction expression vs instruction. |
| W4 p9 switch | W4 c29–31 | COVERED | break/default; claim speed superiority intentionally not repeated, no evidence. |
| W4 p10 Functions syntax/decomposition | W4 c32–33 | MISSING | By-value explained, decomposition rationale/task missing; CP4 restores. |
| W4 p11 Functions compile/link | W1 (pending exact cells) | UNVERIFIED | W4 lacks explicit separate compilation/multifile/linking explanation; coordinator must resolve W1 destinations. |
| W4 p12 Functions declarations/arguments | W4 c32–35; W1 | MISSING | Prototype prose exists without prototype-followed-by-definition example here; parameter scope underspecified. Incorrect overloading claim and wrong fun1 call intentionally corrected in Polish no-overloading prose. |
| W5 p1 title | W5 c0 | COVERED | Course heading. |
| W5 p2 Repeat instructions diagram | W5 c0,2,5 | COVERED | State model and loop flow figure. |
| W5 p3 Manual printf | W5 c2 | COVERED | Inefficiency explained; redundant repeated block intentionally replaced by prose. |
| W5 p4 GO TO diagram + XKCD | W5 c3–5 | EXTENDED | Label example, flow figure, attribution; blanket condemnation corrected. |
| W5 p5 first repeated statement | W5 c3–4 | COVERED | 0..100 and 101 count. |
| W5 p6 while syntax + p7 while diagram (two complementary frames) | W5 c6–10 | EXTENDED | Both code and diagram; prefalse and trace/invariant. |
| W5 p8 do-while syntax + p9 diagram (two complementary frames) | W5 c11–15 | EXTENDED | Posttest, mandatory semicolon corrected. |
| W5 p10 for syntax + p11 diagram (two complementary frames) | W5 c16–22 | EXTENDED | init/test/body/update, omitted fields, continue caveat. |
| W5 p12 Nested loops | W5 c33–36,44 | EXTENDED | Table count and nearest-loop controls. |
| W5 p13 Infinite Loop | W5 c46–47 | EXTENDED | Text-only unbounded code and terminating break variant. |
| W5 p14 break | W5 c40–41,44–47 | EXTENDED | Exit target and termination. |
| W5 p15 continue | W5 c40–45 | EXTENDED | Correct target in each loop form, not vague restart-from-beginning. |
| W5 p16 Fourier function + animation | W5 c57–59 | EXTENDED | Correct odd harmonics; historical PDF/TeX all-n sum is mathematically wrong for square wave, intentionally not retained. |

## Graphics / offline inventory

Verified with filesystem existence and notebook source references, not browser render. All current Polish image references resolve locally. W3: c23 `scanf_perils.png` (also TeX image, same preserved joke); W4: c12 `w4_g1_expression.svg`, c14 `w4_g2_short_circuit.svg`, c19 `w4_g3_branching.svg`, c36 `w4_g4_quadratic.svg`. W4 TeX contains no external substantive graphics; TikZ package alone does not establish a missing diagram.

W5: c5 `loop.png`, `goto2.png`, `goto.png`; c10 `while.png`; c15 `do_while.png`; c22 `for.png`; c38 `w5_control.svg`; c59 `Fourier_series_for_square_wave.gif`, `something-5.png`. The English notebook uses attachments for loop/goto2/while/do_while/for; Polish uses existing corresponding sidecar PNGs. TeX TikZ diagrams correspond to these same flow concepts. TeX `goto` external image resolves to `goto.png`. All `something-0.png` through `something-52.png` are present: TeX animation source frame set is complete. Retaining GIF plus one representative static frame instead of referencing all 53 frame PNGs from Polish notebook is INTENTIONALLY OMITTED as redundant animation internals, not deletion of evidence. `meillogo.png` is presentation branding, INTENTIONALLY OMITTED from notebook teaching content. No new image copying needed at CP1.

## Verification limits and gate

CP1 audit inventory PASS: every English source cell and every substantive PDF/TeX frame topic accounted for. Implementation acceptance FAIL until required MISSING rows resolved by CP2–CP5. MOVED-to-W1/W2 rows and prototype/linking continuity must be resolved against exact cells by coordinator's W1/W2 audit; they are not independent claims of verified W1/W2 coverage. Cross-lecture puts prerequisite is presently MISSING (first executed W4 c9). All runnable C behavior/kernel rendering UNVERIFIED in this read-only source audit. No numerical results are asserted.

Coordinator separately reported rendering and contact-sheet visual inspection of every PDF page (W3=13/W4=12/W5=16) with `/usr/bin/pdftoppm`; that is external reviewer evidence, not an executed command by this reviewer. Fine-size layout and animation playback remain unverified by this reviewer.


Następny checkpoint: CP2 — W3.

### CP2 — PASS

Implementacja: W3 IO w komórkach w3-io-text, w3-io-newlines, w3-io-fgets; interaktywne fgets wyłącznie w oznaczonym programie terminalowym. Usunięto niekontrolowany scanf z komórki wykonywalnej i pustą końcową komórkę, poprawiono sukces dwóch konwersji na 2 oraz projektowe sformułowania. Zachowano żart, doświadczenia formatowania i całą matematykę.

Weryfikacja: python3 3/check_w3.py — PASS: 24 programy × O0/O2 = 48 wykonań, 23 istniejące próby terminalowe × 2 = 46, osiem prób fgets × 2 = 16 (krótki tekst, pełne N−1 z newline, N znaków z newline pozostającym w wejściu, dłuższy, pusty, EOF bez newline, dokładnie N−1 bez newline i pusty wiersz). Porównanie bajtów zachowuje CR/backspace; wcześniejsze text=True zmieniało CR. Wszystkie poprawne przykłady C11 -Wall -Wextra -Werror -pedantic, matematyka -lm. nbformat.validate PASS. kernel_check.py 3 — 24/24 rzeczywiste wykonania Jupyter C, stdout zgodny z osobnym GCC, stderr pusty; log /tmp/w1-w5-audit/cp2-kernel.log.

Checker zaktualizowany do rzeczywiście zastanej zawartości: zachowuje wszystkie istniejące wyrocznie poza przeniesionym wcześniej równaniem kwadratowym (obecność sprawdzana w W4), uwzględnia istniejące dodatkowe formatowanie/sterowanie terminalem i nowy IO. Kompilacja/wykonanie gets zabronione. Ryzyka: scanf nie jest pełnym parserem dowolnych danych; odczyt i walidacja całych wierszy pozostają poza lekcją. Następny CP3.

### CP3 — PASS

W4: bezpośrednia para w4-if-single / w4-if-block, wieloliniowa pojedyncza instrukcja, oba znaki x; w4-if-empty — bezpieczny antywzorzec z oczekiwanym ostrzeżeniem; w4-scope-block i w4-scope-expected-fail — blok bez if, przesłanianie, osobno zasięg i automatyczny czas życia. Dodano regułę najbliższego niepowiązanego if dla else i wyjaśnienie lokalności parametrów. Zachowano wszystkie doświadczenia logiczne i historyczne warianty switch/?:.

python3 4/check_w4.py --if-only — PASS: 54 wykonania złotych/zmienionych przykładów oraz 7 prób granicznych logiki; EXPECTED-FAIL niezadeklarowanej b; cztery kombinacje dangling else z oczekiwanym ostrzeżeniem. Poprawne programy bez ostrzeżeń przy C11 -Wall -Wextra -Werror -pedantic; antywzorce mają osobną kontrolę diagnostyki, nie ukrywamy ostrzeżeń. nbformat.validate PASS. kernel_check.py 4 — 22/22 programy w rzeczywistym Jupyter C zgodne z osobnym GCC. Logi: /tmp/w1-w5-audit/cp3-w4.log i cp3-kernel.log. Weryfikacja koordynatora, niezależny końcowy przegląd CP7 pozostaje. Następny CP4 — parytet A/B równania.
