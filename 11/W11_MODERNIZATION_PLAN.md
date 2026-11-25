# W11 — plan i kontrakt wykonawczy modernizacji

Status: gotowy do realizacji po poleceniu uruchamiającym lokalnego agenta.
Repozytorium: `sgepner/Computer-Science-1`; gałąź robocza: `feature/W11-modernizacja`.
Bazowy master: `a9e95d68bb5cf25e3020373ceb4b7019bc864ec9`.
Artefakt: **11/Wykład 11.ipynb** (polski, kernel C).

## 0. Upoważnienie i praca w worktree

Pracuj wyłącznie w lokalnym worktree tej gałęzi. Sprawdź git status, git branch --show-current, git rev-parse HEAD i git worktree list; nie przełączaj głównego drzewa, nie resetuj cudzych zmian, nie twórz kolejnej gałęzi. Przeczytaj obowiązujące AGENTS.md, jeżeli istnieją. Polecenie wykonania tego planu upoważnia do autonomicznej realizacji wszystkich checkpointów w trybie ciągłym, z lokalną weryfikacją i niezależnym przeglądem, jeśli dostępny. Korzystaj z Execution Control i Test Review Advance, jeśli dostępne; poniższe zasady są samowystarczalne. Po PASS przechodź dalej bez pytania; przy FAIL napraw bieżący etap i powtórz test, nie osłabiaj kryteriów. Przy rzeczywistym blokerze zakończ z raportem. Commituj logiczne zmiany na tej gałęzi; nie publikuj na master, nie wykonuj merge/rebase/cherry-pick ani push bez osobnej dyspozycji. Nie zmieniaj innych wykładów, README, środowiska wspólnego ani historycznych źródeł. Nie mnoż dokumentacji: stan checkpointów i końcowy raport dopisz do tego pliku. Testy robocze tylko na gałęzi implementacyjnej.

## 1. Źródła i granice

Przeczytaj 11/lec11.tex, 11/Lecture 11 examples.ipynb (komórki 0–35: napisy; 36–59: struktury i wskaźniki do funkcji), wszystkie istotne 11/sample/*.c, 10/lec10.tex, 12/lec12.tex, README oraz polskie notebooki W1–W7, zwłaszcza W6–W7 i 7/W7_MODERNIZATION_PLAN.md. Sprawdź dostępne materiały W8–W10 bez zakładania, że ich modernizacja już nastąpiła. Jeśli PDF dostępny lokalnie, porównaj jego zakres z TeX. Wykonaj mapę pokrycia źródeł z decyzjami zachowaj/przebuduj/pomiń i uzasadnieniem. W11 dotyczy wyłącznie napisów; struktury, roboty, listy i wskaźniki do funkcji pozostaw do rozpatrzenia w W12, bez edycji W12. Usuń z nowej narracji historyczne daty kolokwium, nie usuwaj starych plików.

## 2. Koncepcja dydaktyczna

Tytuł: „Wykład 11 — Od pojedynczego znaku do tekstu”. Napis to konwencja reprezentacji danych w pamięci, nie odrębny typ C. Wykorzystaj spiralnie char i reprezentację danych (W2), wejście/wyjście (W3), pętle (W5), adresy i tablice (W6–W7), pliki i alokację (W8–W10). Samodzielny polski wykład, nie translacja ani dziennik modernizacji. Rytm: problem → intuicja → przewidywanie → eksperyment C → interpretacja → małe zadanie. Krótkie kompletne programy, printf jako podstawowe wyjście, bez rozkładu minut, metakomentarzy, nadmiernego rozdrobnienia i nowych zależności. Student ma rozumieć mechanizm przed API.

## 3. Narracja obowiązkowa

| Sekcja | Treść i przykłady |
|---|---|
| W11.1 | char, ASCII na typowej platformie, znaki drukowalne i specjalne, '7' vs 7, '0' vs 0 vs '\0'; krótka uwaga o UTF-8 i bajtach, bez wykładu o Unicode. |
| W11.2 | Ręcznie zbuduj Hello World lub krótszy napis w tablicy; %c vs %s; przesuwanie pierwszego terminatora po zainicjalizowaniu wszystkich potrzebnych bajtów; pusty napis i wewnętrzny NUL. Zachowaj eksperyment z dopisywaniem znaków z oryginału. |
| W11.3 | Inicjalizacja listą i literałem, rozmiar wywnioskowany, większy bufor, sizeof vs strlen; długość, wymagane bajty i pojemność to trzy różne rzeczy. Wskaż że elementy po terminatorze mogą być niezainicjalizowane przy ręcznym przypisywaniu, lecz są zerowane przy inicjalizacji tablicy krótszym literałem. |
| W11.4 | Zachowaj czarnego i białego kota: char a[] = "..."; const char *p = "..."; char *q = a; modyfikacja tablicy, zmiana adresu p, brak przypisania całej tablicy, zakaz modyfikacji literału. Wskaźnik char* nie oznacza automatycznie pamięci tylko do odczytu. |
| W11.5 | scanf z ograniczeniem szerokości vs fgets z pojemnością, stdin i plik, kontrola wyników; spacje, pozostające znaki wejścia, newline, EOF, zbyt długa linia. Zachowaj odczyt sample/read4.c lub równoważnego małego pliku za pomocą while(fgets(...)). |
| W11.6 | Własne mystrlen i mystrcmp jako proste algorytmy iteracji; popraw znak porównania, użyj const i porównuj unsigned char, nie zakładaj wyniku dokładnie +/-1. Pokaż działanie na prefiksach i pustych napisach. |
| W11.7 | Wszystkie sześć funkcji string.h: strlen, strcmp, strcpy, strcat, strchr, strstr. Dla każdej krótki działający przykład, kontrakt i pułapka. Dla wyszukiwania pokaż wskaźnik do wnętrza tablicy, indeks p-s, wydruk sufiksu, brak trafienia. |
| W11.8 | Zachowaj dynamiczne wczytanie dwóch napisów i łączenie w trzeci. Rozmiar wyniku strlen(a)+strlen(b)+1; kontrola wejścia, granic, alokacji i przepełnienia lub jawne małe ograniczenie rozmiaru; strcpy przed strcat; free na wszystkich ścieżkach. Bez rozbudowanego API automatycznie rosnących napisów. |
| W11.9 | Program integracyjny: uproszczony grep, wczytaj niepusty fragment, otwórz mały plik tekstowy, wyszukaj strstr, wypisz numery pasujących linii i ich liczbę. Jawnie ogranicz długość linii lub odrzucaj za długie linie z komunikatem (nie licz fragmentów jako osobnych linii); obsłuż EOF bez newline i błędy. Pytania kontrolne i krótkie zadania. |

Losowe znaki są opcjonalne; nie kosztem głównej narracji. Nie wprowadzaj rozbudowanego Unicode, struktur, wskaźników funkcyjnych ani pełnego parsera.

## 4. Wiążące korekty techniczne

- NUL '\0' to znak o wartości zero, nie NULL (stała wskaźnika pustego). '0' to inny znak. sizeof(char)==1 bajt C, nie gwarantuj 8 bitów ani zakresu 0–255 dla zwykłego char; ASCII przyjęte dla Linux/GCC. strlen liczy bajty do pierwszego NUL.
- Popraw prototypy biblioteczne (C11): size_t strlen(const char *s); int strcmp(const char *s1, const char *s2); char *strcpy(char *restrict dest, const char *restrict src); char *strcat(char *restrict dest, const char *restrict src); char *strchr(const char *s, int c); char *strstr(const char *s1, const char *s2); char *fgets(char *restrict s, int n, FILE *restrict stream). Nie rozwijaj restrict ani size_t jako osobnych tematów; używaj odpowiednich nagłówków, %zu dla size_t, %td dla różnicy wskaźników i %p z (void *) dla adresów obiektów. mystrlen najlepiej zwraca size_t.
- Nie wywołuj %s, strlen ani innych funkcji napisowych bez gwarantowanego terminatora. Nie czytaj niezainicjalizowanych bajtów. Nie wykonuj UB jako eksperymentu; błędny kod tylko w Markdown z wyjaśnieniem.
- Nie modyfikuj literału (UB), nie twierdź, że każdy char* wskazuje dane niemodyfikowalne. Tablica nie jest wskaźnikiem. Nie używaj sizeof parametru wskaźnikowego jako pojemności bufora.
- scanf("%99s", text) dla char text[100], sprawdź wynik; bez scanf("%d\n", &n). Jeżeli łączysz scanf z fgets, jawnie obsłuż resztę linii lub wybierz spójny odczyt liniowy. fgets czyta co najwyżej n-1 bajtów, może zachować newline, nie gwarantuje pełnej linii. Usuwaj newline tylko gdy występuje. Rozróżnij EOF od błędu przez ferror tam, gdzie istotne. W notebooku wejście interaktywne oznacz i zapewnij deterministyczną alternatywę/test z przekierowanym stdin.
- strcpy i strcat wymagają pojemności uwzględniającej NUL, niepokrywających się obszarów i poprawnych napisów wejściowych; strcat także poprawnego napisu docelowego. Nie przedstawiaj strncpy jako automatycznie bezpiecznego zamiennika.
- Sprawdzaj NULL przed dereferencją i odejmowaniem wskaźników; różnica tylko w tej samej tablicy. strcmp gwarantuje znak wyniku, nie jego konkretną wartość.
- malloc sprawdź, nie rzutuj wyniku bez potrzeby; połączone napisy wymagają +1. Oryginalny przykład malloc(strlen(p1)+strlen(p2)); strcat(p3,p1); strcat(p3,p2); ma dwa niezależne błędy: brak bajtu NUL i niezainicjalizowany cel. Zachowaj jako zadanie do analizy, nie wykonywalną komórkę.
- fopen sprawdzaj przed użyciem, zamykaj pliki, nie nadpisuj plików użytkownika. Wszystkie przykłady C11, int main(void), poprawne nagłówki.

## 5. Grafiki i zasoby

Przygotuj czytelne polskie schematy: tablica i NUL, przesunięcie terminatora, długość/pojemność (w tym zerowana reszta), tablica a wskaźnik do literału, wyszukiwanie fragmentu (np. "Ala ma kota", p-s=7, sufiks "kota"), dynamiczne łączenie z +1. Zachowaj styl W6/W7; etykiety i kod zgodne z grafiką. Statyczne diagramy lub małe sekwencje wystarczą; animacja opcjonalna, bez nowych ciężkich zależności. Ścieżki względne, zasoby w 11/figures jeśli konieczne; nie duplikuj istniejących danych bez potrzeby. Zachowaj historyczne sample/, wykorzystaj read4.c po sprawdzeniu, ewentualnie dodaj mały deterministyczny plik wejściowy. Brak martwych linków.

## 6. Checkpointy i bramki

| Etap | Zadanie | PASS |
|---|---|---|
| W11-INT.1 | Inwentaryzacja i mapa źródeł | Wszystkie ważne motywy i pliki pomocnicze ocenione; granica W10/W12 uzasadniona |
| W11-INT.2 | Szkielet notebooka | Samodzielna narracja W11.1–9 bez komentarzy o modernizacji |
| W11-INT.3 | Znaki, NUL i pamięć | Poprawne eksperymenty, grafiki i przypadki brzegowe |
| W11-INT.4 | Inicjalizacja i wskaźniki | Pojemność, sizeof/strlen, const i literały poprawne |
| W11-INT.5 | Wejście i pliki | Poprawny odczyt, EOF, błędy, długa linia |
| W11-INT.6 | Algorytmy i string.h | mystrlen/mystrcmp oraz sześć funkcji poprawnie przetestowane |
| W11-INT.7 | Dynamiczne napisy i grep | Poprawna pamięć, wynik i obsługa błędów |
| W11-INT.8 | Audyt techniczny i dydaktyczny | Wszystkie obowiązkowe kontrole PASS; niezależny przegląd jeśli dostępny |
| W11-INT.9 | Raport i lista publikacyjna | Zapis dowodów, SHA, zakresu zmian, testów, odstępstw; master nietknięty |

Po każdym etapie wykonaj testy adekwatne do zmian, zapisz komendy, wyniki i SHA testowanej rewizji. Nie utożsamiaj braku testu z PASS. Przy niedostępnym kernelu C jawnie oznacz weryfikację notebooka jako nieprzeprowadzoną; nie udawaj pełnego odbioru. Nie wykonuj następnego etapu przy istotnym FAIL. Nie wymagaj pełnej regresji całego repo po każdym małym kroku.

## 7. Odbiór

- JSON notebooka, nbformat, kernelspec.name=c, brak przypadkowych outputów, zbędnych metadanych i pustych komórek wykonywalnych. Wszystkie przykłady samodzielne lub jawnie opisane zależności.
- Kompiluj wykonywalne komórki GCC C11 -Wall -Wextra -Wpedantic w -O0 i -O2. Testuj pamięć ASan/UBSan (nie gwarantują pełnej poprawności). Uruchom w realnym kernelu C, jeśli dostępny. Testy stdin przez kontrolowane dane, pliki wyjściowe w tymczasowym katalogu.
- Testy: pusty i jednoznakowy napis, wewnętrzny NUL, dokładne dopasowanie bufora, identyczne napisy, prefiks, oba znaki relacji, brak trafienia, trafienie na początku i wewnątrz, pusta linia, spacje, długa linia, EOF bez newline, brak pliku, niepoprawny rozmiar, łączenie dwóch pustych napisów, kontrola niepowodzenia alokacji (test lub udokumentowany przegląd ścieżki), grep z zerem i wieloma trafieniami. Zweryfikuj zachowanie na granicy pojemności, brak wycieków i brak podwójnego free.
- Audyt dydaktyczny: mapowanie źródeł, brak nieuzasadnionych pominięć, poprawność diagramów, terminologia polska, brak zadań wymagających W12; wynik można przewidzieć przed uruchomieniem.
- Końcowy raport w tym pliku: baza i testowany SHA, status każdego checkpointu, polecenia/wyniki testów, nieprzeprowadzone kontrole, odstępstwa i lista plików do publikacji (tylko polski notebook i konieczne zasoby). Nie przenoś planu/testów/raportu na master. Nie ogłaszaj pełnego ukończenia przy obowiązkowym FAIL.

## 8. Stan początkowy

W11-INT.1–9: PENDING. Przygotowano wyłącznie kontrakt; nie wykonano implementacji ani testów. Następny krok: W11-INT.1.

Kryterium sukcesu: student potrafi wyjaśnić, jak tekst jest zapisany w pamięci, przewidzieć działanie terminatora, bezpiecznie czytać, kopiować, łączyć i wyszukiwać napisy oraz wykorzystać poznane wcześniej mechanizmy do stworzenia prostego narzędzia przetwarzania tekstu.
