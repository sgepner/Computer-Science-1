# W9 — plan i kontrakt wykonawczy modernizacji

Status: ZATWIERDZONY DO REALIZACJI PO URUCHOMIENIU PRZEZ PROWADZĄCEGO.
Repozytorium: sgepner/Computer-Science-1
Baza: master @ a9e95d68bb5cf25e3020373ceb4b7019bc864ec9
Gałąź: feature/W9-modernizacja
Artefakt docelowy: 9/Wykład 9.ipynb (Jupyter C).
Ten dokument jest instrukcją dla lokalnego agenta, nie materiałem dla studentów.

## 0. Uruchomienie, worktree i granice upoważnienia

Pracuj wyłącznie w lokalnym worktree przypisanym do feature/W9-modernizacja. Sprawdź git status --short, git branch --show-current, git rev-parse HEAD i git worktree list; nie przełączaj innych drzew roboczych, nie resetuj cudzych zmian. Przeczytaj obowiązujące AGENTS.md i instrukcje katalogowe, jeśli istnieją. Nie twórz drugiego worktree dla tej samej gałęzi. Nie aktualizuj bazy przez merge/rebase bez zgody. Nie uruchamiaj ChatGPT Work.

Polecenie startowe prowadzącego autoryzuje realizację W9-INT.1–W9-INT.9 w trybie ciągłym, z kontrolą bramek. Jeżeli dostępne, stosuj Execution Control continuous max_workers=2 oraz Test Review Advance, z niezależnym przeglądem przed zamknięciem. Niniejszy kontrakt jest samowystarczalny również bez tych skills. Po każdym PASS automatycznie przejdź do następnego etapu; przy FAIL popraw ten sam etap i ponów testy; realny blocker zgłoś z dowodem. Nie rozszerzaj zakresu. Nie modyfikuj W1–W8 ani W10–W15, wspólnego README, CI, instrukcji globalnych czy innych gałęzi. Lokalne commity na gałęzi roboczej są dozwolone; nie pushuj, nie merguj ani nie publikuj na master bez osobnej dyspozycji. Przed zatwierdzeniem końcowym pozostaw czyste drzewo lub wyjaśnij stan.

## 1. Źródła i wzorzec

Obowiązkowo przejrzyj 9/lec9.tex, 9/lec9.pdf (jeśli dostępny lokalny odczyt), 9/Lecture 9 examples.ipynb, 9/samples/* (2d_1–4, 2d_fun, 2d_fun2, dma_1–5, sin.dat), 6/Wykład 6.ipynb, 7/Wykład 7.ipynb, 7/W7_MODERNIZATION_PLAN.md, 8/lec8.tex i 10/lec10.tex dla granic zakresu. W8 jest równolegle modernizowany: nie zależ od niedostępnego jeszcze polskiego notebooka i nie pobieraj zmian z obcej gałęzi. Wykonaj mapę pokrycia: każdy istotny temat i przykład -> zachowaj/przebuduj/świadomie pomiń + uzasadnienie. Zweryfikuj rzeczywisty format sin.dat przed wyborem danych. Oryginalne pliki pozostają bez zmian.

Wzorzec W6–W7: autonomiczny polski materiał, nie tłumaczenie ani kronika modernizacji. Problem -> intuicja -> przewidź wynik -> eksperyment w C -> interpretacja -> mała samodzielna modyfikacja. Zachowaj spójność terminologii i stylu, naturalny humor, czytelne wzory LaTeX (matematyka w delimitatorach notebooka, kod w backtickach). Bez rozkładu minut, komentarzy agentowych, odwołań do starych wersji. Nie mnoż komórek bez potrzeby. Każda wykonywalna komórka powinna być samodzielnym, kompletnym programem C11 z int main(void), odpowiednimi nagłówkami i ewentualnymi jawnie wyjaśnionymi danymi wejściowymi.

## 2. Cele i narracja

Tytuł sugerowany: „Wykład 9 — Więcej wymiarów i pamięć na żądanie: tablice 2D oraz alokacja dynamiczna”.

| Sekcja | Pytanie | Obowiązkowa treść |
|---|---|---|
| W9.1 | Czy tablica musi być jednowymiarowa? | Motywacja tabelą danych, deklaracja int tab[2][3], inicjalizacja przez zagnieżdżone klamry, odczyt i zapis, pętle zagnieżdżone. |
| W9.2 | Jak komputer przechowuje tabelę? | Tablica wierszy, row-major, adresy, sizeof całej tablicy, wiersza i elementu; diagram i wzór przesunięcia. |
| W9.3 | Co oznacza przesunięcie o wiersz? | tab, tab[0], &tab[0][0], tab+1, int (*p)[3], typy i rozmiary kroku; nie utożsamiać z int **. |
| W9.4 | Jak przekazać macierz do funkcji? | int A[][MAXCOL], równoważność parametru ze wskaźnikiem do wiersza, pojemności i aktywne wymiary n,m, inicjalizacja i drukowanie. |
| W9.5 | Co można zrobić z macierzą? | Kopia przekątnej, wiersza, kolumny, wstawianie wiersza i kolumny; adres wiersza vs rzeczywista kopia, modyfikacje przez alias. |
| W9.6 | A jeśli rozmiaru jeszcze nie znamy? | W7/W8: liczba pomiarów z pliku, stała pojemność, potrzeba dobrania rozmiaru w trakcie działania. |
| W9.7 | Jak zamówić i oddać pamięć? | malloc, sizeof, void *, NULL, inicjalizacja, free, własność i czas życia bloku; schemat stanów. |
| W9.8 | Czy dynamiczna tablica działa jak zwykła? | Indeksowanie, rozmiar od użytkownika, przekazywanie do znanych funkcji 1D, ponowne użycie bubble sort z W7. |
| W9.9 | Od pliku do wyniku | Liczba punktów, alokacja dwóch tablic double, odczyt par x,y, min/max/średnia y, sprzątanie na wszystkich ścieżkach; pytania kontrolne. |

Student powinien umieć wytłumaczyć, czemu do funkcji 2D potrzeba informacji o długości wiersza, przeprowadzić bezpieczną operację na macierzy prostokątnej, dobrać rozmiar dynamicznej tablicy, sprawdzić alokację i zwolnić pamięć. Bez rozwijania dynamicznych macierzy (W10), calloc/realloc, zaawansowanego API alokatorów, teorii sterty czy struktur danych. WLA/VLA tylko krótka uwaga o standardzie; preferuj stałe pojemności w części 2D.

## 3. Wiążące korekty merytoryczne

- Tablica 2D jest tablicą tablic. Jej reprezentacja jest ciągła, w kolejności wierszy. Dla R wierszy i C kolumn rozmiar wynosi R*C*sizeof(T); przesunięcie bajtowe elementu [i][j] od początku całego obiektu to (i*C+j)*sizeof(T). Rozróżnij aktywne m od fizycznego MAXCOL. Ilustracja: 2x3 z wartościami 11,12,13;21,22,23.
- Nie wykonuj arytmetyki int* przez granice wierszy: historyczne p[3] po p=&tab[0][0] jest niedozwolonym odczytem, nawet jeśli fizycznie pamięć sąsiaduje. Pokazuj adresy przez &tab[i][j], pętle po wierszach i prawidłowo typowane wskaźniki do wierszy. Nie odejmuj wskaźników int* z różnych wierszy; do demonstracji użyj rozmiarów obiektów, adresów %p i ewentualnie reprezentacji bajtowej całego obiektu przez unsigned char*. Nie myl fizycznej ciągłości z dozwoloną arytmetyką.
- tab w typowym wyrażeniu konwertuje się na int (*)[C]; tab[0] na int*. int** ma inną semantykę. Rozmiary i adresy opisuj jako typowe dla Linux/GCC, nie gwarancje standardu. %p wymaga (void*), sizeof drukuj przez %zu. Nie twierdź, że size_t to unsigned int.
- Używaj stałych MAXROW/MAXCOL zgodnie z W7. Waliduj 0 < n <= MAXROW, 0 < m <= MAXCOL i indeksy przed użyciem; kopiowanie wiersza obejmuje m, kolumny n, przekątnej n dla kwadratowej macierzy. W przypadku prostokątnej albo jawnie ogranicz operację do macierzy kwadratowej, albo użyj min(n,m) i wyjaśnij decyzję. Bufory wyjściowe muszą mieć odpowiednią pojemność. Wstawianie danych sprawdza długość. Testuj rzeczywiste prostokątne przypadki, nie tylko kwadraty. Przy przykładzie aliasu pokaż, że wskaźnik do wiersza nie kopiuje danych, żyje tylko tak długo jak tablica i nie podlega free. Nazwy funkcji nie mogą sugerować kopii, jeśli zwracają adres. Nie używaj nieprzenośnej konwersji wielowymiarowej tablicy do const-qualified typu wskaźnika do tablicy w C11; dobierz poprawny interfejs bez komplikowania narracji.
- malloc jest zadeklarowany w stdlib.h jako void *malloc(size_t size); nie ma alternatywnego prototypu unsigned int. W C nie potrzeba rzutowania wyniku. Pokaż int *p = malloc(n * sizeof *p) po walidacji n; nie używaj magicznej liczby 24. Wyjaśnij sizeof *p jako rozmiar typu, bez dereferencji w tym przypadku.
- Rozmiar z wejścia musi być poprawnie odczytany, dodatni, ograniczony bezpieczną pojemnością i wolny od przepełnienia iloczynu (np. po konwersji zweryfikowanego n: (size_t)n <= SIZE_MAX / sizeof *p, z odpowiednim nagłówkiem). Dobierz prosty, czytelny limit aplikacyjny i bezpieczny parser; nie polegaj na scanf %d dla dowolnie dużego niesprawdzonego tekstu. Jeśli wejście ograniczone dydaktycznie, jawnie opisz kontrakt i zapewnij bezpieczną obsługę nieprawidłowego wejścia. Nie wykładaj szczegółowo size_t.
- Sprawdź NULL przed dostępem, inicjalizuj wszystkie odczytywane elementy. Dla każdego udanego malloc jedno odpowiadające free, także przy częściowej alokacji lub nieudanym odczycie. Nie zwalniaj wskaźnika do środka bloku, tablicy automatycznej ani aliasu. Nie używaj po free, nie zwalniaj dwukrotnie. free(NULL) jest poprawne; przypisanie NULL do p po free nie unieważnia innych aliasów. Pokaż te błędy tylko w niewykonywalnym Markdown.
- Nie utożsamiaj tablicy o stałej pojemności ze statycznym czasem przechowywania. Nie wprowadzaj skomplikowanych dygresji; krótko rozróżnij obiekt lokalny i zaalokowany blok.
- Program integracyjny: sprawdzaj fopen/fclose i wynik każdej konwersji przed użyciem danych, poprawność separatorów zgodnie z rzeczywistym formatem, skończoność danych jeśli potrzebna, dodatnie n (bez dzielenia przez zero), obsłuż niepełne/malformed wejście. Nie nadpisuj oryginalnego sin.dat. W razie potrzeby dodaj mały jawny fixture w 9/w9_dane/ lub generuj dane w kodzie. Przy 2 alokacjach obsłuż niepowodzenie każdej. Nie wymuszaj rzeczywistego OOM dla testu.
- Nie przenoś mechanicznie komórek 24–29 z historycznego notebooka: stare, częściowo niekompletne zadania testowe niezwiązane z W9. Odnotuj w mapie pokrycia; zastąp pytaniami o bieżący materiał.

## 4. Zasoby i przykłady

Zachowaj sens historycznych programów 2d_1–4, 2d_fun/2d_fun2 oraz dma_1–5, nie ich błędy. Scalone, krótkie eksperymenty są lepsze od serii niemal identycznych programów. Użyj niewielkich macierzy, np. 2x3 i 3x4, oraz osobnego kwadratu dla przekątnej. Przykłady inicjalizacji i aliasu zachowują pojęcia z W6/W7. Sortowanie ma dowodzić zgodności interfejsu 1D; nie ucz ponownie algorytmu. Użyj deterministycznych danych lub stałego ziarna w testach. Przygotuj schematy: (1) tablica 2D jako ciąg wierszy z indeksami i bajtami, (2) pojemność fizyczna vs aktywny prostokąt, (3) kopia vs alias wiersza, (4) cykl życia malloc–inicjalizacja–użycie–free. Preferuj osadzone obrazy Markdown attachments jak W6/W7; użyj względnych linków tylko jeśli konieczne. Zastąp brakujące fig.png. Diagramy muszą odpowiadać kodowi i semantyce. Bez zewnętrznych usług i absolutnych ścieżek.

## 5. Bramki wykonawcze

| Etap | Zadanie | PASS |
|---|---|---|
| W9-INT.1 | Inwentaryzacja źródeł, środowiska, instrukcji i mapa pokrycia | Zapisane decyzje zachowaj/przebuduj/pomiń dla wszystkich istotnych motywów, sprawdzony zakres W10. |
| W9-INT.2 | Szkielet polskiego notebooka | W9.1–W9.9 układają się w autonomiczny wykład, brak metakomentarzy. |
| W9-INT.3 | Sekcje W9.1–3: tablice 2D, pamięć, typy | Poprawne granice, rozmiary, inicjalizacja, brak UB, rysunki zgodne z kodem. |
| W9-INT.4 | W9.4–5: funkcje i operacje macierzowe | Testy prostokątne i kwadratowe, poprawne długości kopii, wstawianie, alias i walidacja. |
| W9-INT.5 | W9.6–7: motywacja i alokacja | Poprawne malloc/sizeof/free, sprawdzanie wejścia/NULL/rozmiaru, brak wycieków. |
| W9-INT.6 | W9.8–9: dynamiczne tablice, sortowanie, integracja z plikiem | Odtwarzalne wyniki, wszystkie ścieżki błędów posprzątane, brak zależności od innych wykładów. |
| W9-INT.7 | Ilustracje, ćwiczenia, spójność narracji | Wszystkie grafiki renderują się, brak martwych odwołań, zadania kontrolne zgodne z zakresem. |
| W9-INT.8 | Końcowy audyt techniczny i dydaktyczny | Wszystkie obowiązkowe kontrole z §6 zaliczone; niezależny przegląd jeśli dostępny; realne braki jawnie zgłoszone. |
| W9-INT.9 | Raport, czyste drzewo i lista plików publikacji | Weryfikowalny stan, lista zmian tylko w W9, dowody i status wszystkich bramek, bez zmian master. |

Prowadź stan w jednym istniejącym pliku planu lub pojedynczym pliku 9/w9_validation/STATUS.md na gałęzi roboczej; nie twórz rozproszonej dokumentacji. Zapisuj komendy, wynik i SHA testowanego kodu; nie przypisuj PASS testom niewykonanym. Na każdym etapie dobierz minimalne adekwatne testy, na W9-INT.8 wykonaj pełną kontrolę W9. Nie zmieniaj zakresu ani nie osłabiaj testów dla uzyskania PASS.

## 6. Odbiór i testy

- Prawidłowy notebook nbformat, kernelspec.name=c, wyczyszczone przypadkowe outputs/execution_count, niezbędne metadata i attachments zachowane. Kod C11, gcc -std=c11 -Wall -Wextra -Wpedantic w -O0 i -O2 (linkowanie -lm tam gdzie uzasadnione). Każda wykonywalna komórka sprawdzona; ewentualne dyrektywy kernela obsłuż jawnie w harnessie, nie usuwaj semantycznie istotnego kodu.
- Uruchom wszystkie przykłady w rzeczywistym kernelu C jeśli dostępny i odpowiednio zapewnij stdin/fixtures. Jeżeli niedostępny, nie instaluj globalnie bez zgody; wykonaj równoważne testy GCC, zgłoś brak weryfikacji integracji z kernelem jako jawne ograniczenie do odbioru, nie oznaczaj go jako PASS.
- ASan/UBSan dla wszystkich przykładów dotykających pamięci i alokacji; kontrola wycieków (LSan jeśli dostępny). Sanitizery nie zastępują przeglądu semantyki C. Nie wykonuj przykładów UB w zwykłych komórkach.
- Macierze: 2x3 i 3x2, 1x1, aktywne wymiary mniejsze niż pojemność, oba krańcowe indeksy, błędne n/m/indeksy, różnica między kopią i aliasem, spodziewane wartości przekątnej/wiersza/kolumny oraz wstawiania.
- Alokacja: n=1, kilka elementów, 0, ujemne, zbyt duże i błędne wejście; test ochrony przepełnienia iloczynu, test lub bezpieczne deterministyczne wstrzyknięcie niepowodzenia alokacji (w harnessie, bez realnego OOM). Sprawdź brak podwójnego free, use-after-free i wycieku również przy błędzie drugiej alokacji. Sortowanie: posortowane, odwrotne, duplikaty.
- Plik: poprawny format, brak pliku, błędny nagłówek, nadmiarowy/błędny rozmiar, niepełne dane, błędny separator lub konwersja. Sprawdź oczekiwane statystyki na małym deterministycznym zbiorze. Testowe pliki w katalogu tymczasowym lub jawnej lokalizacji testowej; nie nadpisuj historycznych danych.
- Audyt wszystkich lokalnych referencji i attachments; wzory oraz diagramy czytelne; zgodność z W6/W7, zakres W8/W10, bez zbędnych dygresji. Zweryfikuj mapę pokrycia. Oryginalne źródła pozostają bez zmian.
- Raport: bazowy SHA, końcowy HEAD, testowany SHA, polecenia i wyniki, każda bramka PASS/FAIL/BLOCKED, zastrzeżenia, zmienione pliki, dokładna lista plików do selektywnego przeniesienia na master po decyzji prowadzącego. Nie ogłaszaj ukończenia przy obowiązkowym FAIL. Kończ COMPLETE lub BLOCKED.

## 7. Publikacja

Jedynym planowanym artefaktem studenckim jest 9/Wykład 9.ipynb i konieczne zasoby, jeśli nie można ich sensownie osadzić. Dokument niniejszy, skrypty testowe, raporty, dane tymczasowe, binaria, cache i instrukcje robocze pozostają poza końcowym master. Nie modyfikuj historycznych lec9.tex, lec9.pdf, notebooka EN ani samples. Nie rób merge całej gałęzi. Prowadzący sam zatwierdzi publikację selektywną po audycie.

Kryterium sukcesu: student rozumie pamięć i typy tablic 2D, potrafi operować na macierzy oraz bezpiecznie przydzielić, wykorzystać i zwolnić pamięć tablicy 1D o rozmiarze znanym dopiero w czasie działania.
