# W10 — kontrakt wykonawczy modernizacji

Baza: master, a9e95d68bb5cf25e3020373ceb4b7019bc864ec9.
Gałąź: W10-modernizacja. Praca w lokalnym worktree, wyłącznie w zakresie wykładu 10.

## 1. Tryb pracy i rezultat

Wykonaj plan autonomicznie, kolejno przez checkpointy W10-INT.1–10. Po każdym sprawdź kryteria PASS, zapisz krótki wynik i wykonaj logiczny commit na gałęzi roboczej. Przy FAIL napraw bieżący etap i ponów testy; nie rozszerzaj zakresu. Jeśli dostępne są lokalne Test Review Advance i Execution Control, stosuj ich bramki, tryb continuous i niezależną recenzję. Plan jest samodzielny i nie wymaga tych umiejętności do wykonania. Nie twórz zbędnej hierarchii dokumentów. Przed pracą sprawdź git status, aktywną gałąź i ewentualne lokalne AGENTS.md; nie nadpisuj cudzych zmian. Nie przełączaj innych worktree, nie wykonuj merge/rebase na master ani force push. Nie zmieniaj README ani innych wykładów. Publikacja materiałów na master wymaga osobnej zgody prowadzącego.

Rezultat: 10/Wykład 10.ipynb oraz zmodernizowany 10/Lecture 10 examples.ipynb, zgodne merytorycznie i narracyjnie, z potrzebnymi grafikami i danymi. Zachowaj lec10.tex i lec10.pdf jako źródła historyczne bez zmian. W samples zmieniaj tylko potrzebne przykłady i zasoby, jeśli konieczne do poprawnej realizacji wykładu; bez globalnego porządkowania repozytorium. Pliki agentowe i testy pozostają w gałęzi roboczej, nie w materiałach studenckich.

## 2. Źródła i standard

Przeczytaj pełne 10/lec10.tex, 10/Lecture 10 examples.ipynb, przejrzyj PDF i wszystkie istotne samples (2D_*.c, 2D.c, christmas_*.c, christmas_so.c, data1.dat, data2.dat; kopie ~ i checkpointy nie są źródłem kanonicznym). Porównaj standard W6–W7, zwłaszcza 7/W7_MODERNIZATION_PLAN.md i polski/angielski notebook W7. Sprawdź aktualny zakres W9 i W11. Na bazowym SHA W8 i W9 nie mają jeszcze polskich notebooków; nie zakładaj ukończenia ich modernizacji. Jeśli istnieją równoległe gałęzie, nie scalaj ich; odnotuj ewentualną potrzebę późniejszej kontroli spójności. Sporządź mapę pokrycia: zachowaj/przebuduj/świadomie pomiń z uzasadnieniem, obejmując także przykłady poza notebookiem.

Notebook ma być autonomicznym wykładem, nie tłumaczeniem z komentarzami historycznymi. Bez harmonogramów minutowych, zapisków agentowych i sztucznego rozdrabniania komórek. Zachowaj styl kursu od zera do bohatera, pytania intuicyjne, stopniowanie trudności, kompletne programy w kernelu C, polskie komentarze w PL i angielskie w EN. Wzory LaTeX w Markdown; grafiki spójne z W6–W7, względne ścieżki, bez zbędnych zależności. Zachowaj wartościowe przykłady, humor i sens oryginału. 

## 3. Narracja i cele

Tytuł PL: Wykład 10 — Dynamiczne tablice. Jak zorganizować dane w pamięci?
EN: Lecture 10 — Dynamic arrays: How to organize data in memory?

Główna idea: ta sama macierz matematyczna może mieć różne reprezentacje w pamięci. Student rozumie typy, adresy, indeksowanie, własność i czas życia bloków, nie tylko receptę alokacji.

1. W10.1: krótkie przypomnienie malloc/free/sizeof, wskaźnik jako odrębna zmienna, czas życia obiektu dynamicznego, pamięć niezainicjalizowana, NULL.
2. W10.2: dynamiczne tablice 1D char/int/double, rozmiar z wejścia, porównanie stałej tablicy automatycznej, VLA i alokacji dynamicznej. Nie powtarzaj całego W9.
3. W10.3: współrzędne x,y z samples/data1.dat: dwa bloki kontra jeden blok 2*n elementów, y=x+n. Pokaż schemat oraz różnicę w free; y wewnątrz bloku nie wolno zwalniać osobno.
4. W10.4: int a=5; int *p=&a; int **pp=&p; a, *p, **pp i pp[0][0]. Zachowaj oba warianty allocdouble(n) zwracający wskaźnik i allocdouble2(n,&x) modyfikujący wskaźnik wywołującego. Wyjaśnij przekazywanie argumentów przez wartość. Zachowaj przykład tablicy wskaźników do dwóch lokalnych int, bez zwalniania tych int.
5. W10.5: przypomnienie int A[2][3] z wartościami 11,12,13,21,22,23; row-major, indeks płaskiego dynamicznego bloku k=i*cols+j. Schemat i mały eksperyment z indeksami w C (nie wymagaj widgetów JS ani dodatkowych kernelów).
6. W10.6: zachowaj cztery kroki oryginału: int *p z sześcioma elementami; dwa wskaźniki p0,p1; int *A[2]; dynamiczna tablica wskaźników int **A. Dopiero potem wyprowadź A[i][j] = *(*(A+i)+j). Nie zastępuj wyprowadzenia gotowym helperem.
7. W10.7: porównaj osobne alokacje wierszy (rows+1 bloków) i jeden ciągły blok danych plus dynamiczna tablica wskaźników (2 bloki). Pokaż schemat, kod, identyczne wyniki i różne zwalnianie. Osobne wiersze mogą mieć różne długości; wiersze nie muszą sąsiadować. Wspólny blok ułatwia liniowy dostęp; bez rozbudowanego wykładu o cache.
8. W10.8: funkcje alloc2d/print2d/free2d o jasno określonym kontrakcie, dopasowane do reprezentacji. Zachowaj porównanie parametrów statycznej tablicy o znanej liczbie kolumn i int **; napraw normalize z oryginału, stosując (x-min)/(max-min) dla wszystkich elementów, z jawną polityką dla stałych danych (np. same zera). Zachowaj fill/print i deterministyczne dane testowe. Pokaż kopiowanie wiersza, przekątnej i wstawianie wiersza na poprawnych macierzach prostokątnych, przynajmniej jako krótkie ćwiczenia z rozwiązaniem w kodzie lub dodatku.
9. W10.9: kompletny program odczytu samples/data2.dat: wymiary, alokacja, odczyt, funkcja wyświetlająca/przetwarzająca, zwolnienie i fclose. Obsłuż błędy i częściową alokację. Zachowaj obserwację różnicy adresów wierszy, z rozmiarem sizeof(int) i bez założenia konkretnego adresu.
10. W10.10: zachowaj choinkę ze znaków * i o i oryginalne przykłady christmas; zaproponuj ćwiczenie przejścia od drukowania do dynamicznej siatki char. Bez wprowadzania pełnej obsługi stringów przed W11. Przejrzyj serię źródeł i odnotuj decyzję o każdym istotnym motywie.

## 4. Korekty obowiązkowe i ograniczenia

- malloc ma prototyp void *malloc(size_t size), nie unsigned int; stdlib.h, w C cast void* nie jest konieczny. sizeof jest operatorem, wynik size_t, druk %zu. Typowe rozmiary na Linux x86-64 nie są gwarancją standardu. %p z (void *) dla wskaźników do obiektów.
- Tablica 2D int A[2][3] nie jest int **. Jej typ to tablica tablic, w typowym wyrażeniu konwersja do int (*)[3]. int *A[2] to tablica wskaźników; int **A to wskaźnik do wskaźnika. Wspólna składnia [][] nie oznacza identycznej reprezentacji. Nie wymuszaj nauki skomplikowanych deklaracji ani dynamicznych wskaźników do VLA; krótka uwaga wystarcza.
- VLA nie są wyłącznie rozszerzeniem GCC; wyjaśnij zależność od wersji/implementacji C. Kurs preferuje malloc dla rozmiarów dynamicznych. Nie utożsamiaj automatycznej długości życia z każdym obiektem o stałym rozmiarze, ani stack/heap z gwarantowaną przez standard fizyczną implementacją.
- Nie używaj malloc(24) jako wzorca, stosuj liczbę elementów i sizeof typu lub *p. Rozmiary wejściowe dodatnie, sprawdzenie przepełnień przed mnożeniem, także 2*n i rows*cols; unikaj signed overflow. Ogranicz rozmiar danych demonstracyjnych. Nie rozwijaj wykładu o size_t; zabezpieczenia można objaśnić krótko lub wydzielić w kompletnych przykładach.
- Sprawdzaj NULL przed użyciem, zwalniaj wcześniej przydzielone zasoby przy błędzie (w tym częściowo przydzielone wiersze). Jedno free na żywy przydzielony blok, nie na każdy wskaźnik. Nie zwalniaj adresu wewnątrz bloku ani obiektu automatycznego. Nie używaj pamięci po free, nie wykonuj double-free. Jeśli helper dla wspólnego bloku zwalnia A[0], określ kontrakt: rows>0, A[0] niezmieniony; alternatywnie zachowaj jawnie bazowy p. Nie mieszaj funkcji zwalniających obu reprezentacji.
- Popraw odczyty niezainicjalizowanych elementów (historyczne komórki 30 i 38); przykłady celowo błędne wyłącznie w Markdown, nie uruchamiane. Nie używaj różnicy wskaźników z niezależnych alokacji jako pomiaru odległości.
- normalize: popraw pętlę od 0, skalowanie, przypadek n=0 i max=min. copyrow/insertrow iterują po kolumnach, copydiag po min(rows,cols); sprawdzaj indeks wiersza i pojemność bufora.
- fopen/fscanf: sprawdzaj wyniki przed użyciem danych, obsłuż niepełny plik i błędne wymiary, zamknij zasoby. Ujednolić ścieżki samples/data1.dat i samples/data2.dat. Nie nadpisuj oryginalnych danych.
- Popraw mian, szieof, collumns, błędne nawiasy, aaa, komentarze char/int/double, formatowanie z backspace i niespójne przykłady. Nie zachowuj błędnych outputów. Nie wprowadzaj list, struktur, własnych alokatorów, rozbudowanego realloc, 3D ani optymalizacji sprzętowej jako obowiązkowej części.
- Grafiki: czas życia wskaźnika i danych, dwa/jeden blok x,y, podwójny wskaźnik, macierz/płaski blok, cztery kroki konstrukcji, dwie metody alokacji i zwalniania. Oryginalne TikZ można wykorzystać/przerysować. Oznaczenia adresów mają odpowiadać typom i kodowi; poglądowe adresy jawnie oznaczyć. Nie trzeba tworzyć animacji, jeśli schematy wystarczą.

## 5. Checkpointy i bramki

| ID | Zadanie | PASS |
|---|---|---|
| W10-INT.1 | Inwentaryzacja i mapa pokrycia | Wszystkie ważne motywy źródeł i samples mają decyzję; zidentyfikowane granice W9/W11 |
| W10-INT.2 | Szkielet PL | Samodzielna narracja W10.1–10.10, bez metatekstu |
| W10-INT.3 | Alokacja 1D i podział pamięci | Kod i grafiki zgodne, poprawne zwalnianie i wejście |
| W10-INT.4 | Podwójne wskaźniki | Oba warianty funkcji alokujących oraz przykład a,p,pp działają |
| W10-INT.5 | Wyprowadzenie 2D | Cztery kroki, poprawne typy i indeksy, schematy zgodne z kodem |
| W10-INT.6 | Dwie metody alokacji 2D | Identyczne wyniki, poprawne free, obsługa częściowego FAIL |
| W10-INT.7 | Funkcje i normalizacja | Poprawne wyniki również dla prostokątnych macierzy i danych stałych |
| W10-INT.8 | Pliki i choinka | Kompletny program działa, błędne wejścia obsłużone, zasoby dostępne |
| W10-INT.9 | EN | Pełna zgodność treści, przykładów i grafik z PL |
| W10-INT.10 | Audyt końcowy | Testy obowiązkowe PASS, niezależna recenzja jeśli dostępna, raport i lista plików do publikacji |

## 6. Odbiór i testy

- Notebooki: poprawny JSON, kernelspec zgodny z W7 (C), samodzielne komórki, brak pustych komórek wykonawczych i przypadkowych outputów, poprawne linki i renderowanie matematyki/grafik. Wykonaj w realnym kernelu C, jeśli dostępny. Jeżeli niedostępny, jawnie odnotuj niewykonany test i sprawdź programy bezpośrednio GCC; nie twierdź, że kernel zweryfikowany.
- Kompiluj wszystkie programy przeznaczone do wykonania GCC C11 -Wall -Wextra -Wpedantic, przy -O0 i -O2, z właściwymi bibliotekami. Testuj adekwatne programy ASan/UBSan, w tym wycieki, jeśli dostępne. Brak raportu sanitizerów nie jest dowodem braku wszystkich UB.
- Dane: 1x1, 2x3, 3x2, 1xn, nx1; niekwadratowe macierze dla row/diag/insert; zgodność indeksowania liniowego i [][]; normalizacja danych z różnymi wartościami i stałych; 0/ujemne wymiary, przepełnienie i ograniczenia rozmiaru; poprawny plik, brak pliku, brak elementów, nieprawidłowy token. Testuj awarie alokacji deterministycznie (np. testowy wrapper malloc, bez wyczerpywania pamięci systemu), w tym awarię w środku pętli wierszy i drugiej alokacji bloku ciągłego. Sprawdź zwolnienie zasobów. Dla choinki i losowania użyj stałego ziarna w testach.
- Audyt merytoryczny: żadna wykonywana komórka nie ma znanego UB; pełne pokrycie źródeł lub świadome pominięcia; PL/EN zgodne; czytelne przykłady i rysunki; brak regresji zakresu. Nie zmieniaj historycznych PDF/TEX.
- Raport końcowy (jeden krótki dokument roboczy albo sekcja w planie): SHA bazy i końca, lista plików, tabela PASS/FAIL, testy wykonane i niewykonane, odstępstwa, decyzje mapy pokrycia, lista plików do selektywnego przeniesienia na master, instrukcja ręcznej kontroli. Nie ogłaszaj ukończenia przy obowiązkowym FAIL. Nie scalaj samodzielnie. 

Kryterium sukcesu: student potrafi wyjaśnić, skonstruować, wykorzystać i poprawnie zwolnić każdą z dwóch dynamicznych reprezentacji macierzy, rozumiejąc różnicę między tablicą, wskaźnikiem i blokiem pamięci.
