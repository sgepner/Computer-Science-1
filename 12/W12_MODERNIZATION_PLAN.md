# W12 — kontrakt wykonawczy modernizacji

Status: ZATWIERDZONY DO IMPLEMENTACJI NA GAŁĘZI ROBOCZEJ
Repozytorium: sgepner/Computer-Science-1
Gałąź: feature/W12-modernizacja
Baza: master @ a9e95d68bb5cf25e3020373ceb4b7019bc864ec9
Docelowy artefakt: `12/Wykład 12.ipynb` (Jupyter C, C11).

## 0. Organizacja pracy i upoważnienie

Realizuj autonomicznie etapy W12-INT.1–9 w istniejącym lokalnym worktree na wskazanej gałęzi. Nie twórz kolejnej gałęzi ani worktree. Sprawdź pwd, git status, git branch --show-current, git worktree list i git log; przeczytaj obowiązujące AGENTS.md i instrukcje lokalne, jeśli istnieją. Nie przełączaj gałęzi w innym worktree. Nie resetuj, nie usuwaj cudzych zmian, nie aktualizuj master, nie rebase/merge/cherry-pick bez polecenia. Jeśli gałąź lub stan drzewa jest sprzeczny z kontraktem, zatrzymaj się przed modyfikacją i zgłoś problem.

Jeśli lokalnie dostępne są Execution Control i Test Review Advance, użyj trybu ciągłego z bramkami PASS/FAIL i niezależnym przeglądem. W przeciwnym razie stosuj te same zasady ręcznie. Po każdym etapie wykonaj testy, zapisz zwięzły wynik i commit logicznego checkpointu; przy FAIL napraw etap przed przejściem dalej. Nie pytaj o zwykłe decyzje redakcyjne i techniczne. Nie wykonuj publikacji na master. Push gałęzi roboczej tylko jeśli użytkownik osobno na to zezwoli. Nie uruchamiaj ChatGPT Work.

Zakres zmian: katalog 12/; nie modernizuj W1–W11, nie reorganizuj repozytorium ani README, nie usuwaj historycznych źródeł i nie zmieniaj CI. Testy, raport i niniejszy plan pozostają na gałęzi roboczej. Preferuj jeden zwięzły raport roboczy i minimalny zestaw powtarzalnych testów, bez mnożenia dokumentacji. Po odbiorze wyłącznie notebook i potrzebne zasoby mogą zostać selektywnie przeniesione na master za odrębną zgodą użytkownika.

## 1. Źródła i styl

- 12/lec12.tex, lec12.pdf, A very nice lacture on the use of structures in C.ipynb, 12/samples/ (w tym robot.c, robot_struct.c, robot_struct2.c, robot_struct3.c, student.c, fun.c, clist.cpp).
- 11/Lecture 11 examples.ipynb: końcowe sekcje Structures, Pointers to functions, Functions and Structures są dodatkowym źródłem W12; nie zmieniaj W11.
- 6/Wykład 6.ipynb, 7/Wykład 7.ipynb, 7/W7_MODERNIZATION_PLAN.md: wzorce pedagogiczne i techniczne; przejrzyj też aktualne źródła W8–W11, nie zakładaj że ich modernizacja została ukończona.
- Porównaj PDF z TeX i sporządź mapę pokrycia wszystkich istotnych motywów: zachowaj/przebuduj/świadomie pomiń z uzasadnieniem. Historyczne pliki .c/.cpp, kopie ~ i checkpointy traktuj jako źródła, nie jako kod do automatycznego publikowania ani pretekst do sprzątania repozytorium.

Polski notebook jest autonomicznym wykładem, nie tłumaczeniem ani dziennikiem modernizacji. Tytuł: „Wykład 12 — Od zmiennych do własnych typów danych. Struktury w C”. Stosuj rytm problem → intuicja → przewidź → eksperyment → interpretacja → zmień → pytania. Krótkie niezależne kompletne programy, konsekwentna terminologia, humor tam, gdzie naturalny, formatowanie matematyczne LaTeX, grafiki po polsku zgodne z W6–W7. Bez rozkładu minut, komentarzy o modernizacji, niepotrzebnych dygresji. Preferuj printf. Wykład kończy kurs i łączy już poznane funkcje, wskaźniki, tablice, napisy i pamięć dynamiczną. Nie wprowadzaj OOP, C++, drzew, list dwukierunkowych, generycznych kontenerów.

## 2. Narracja i wymagania

### W12.1 — Gdy sześć tablic nie wystarcza
Oryginalny problem robotów: nazwa, pozycja, prędkość i przyspieszenie; równoległe tablice x,y,vx,vy,ax,ay oraz nazwy. Wyjaśnij zależność wspólnego indeksu. Pokaż mały działający przykład z poprawnym indeksowaniem i inicjalizacją zamiast błędnych operacji na całych tablicach z robot.c. Funkcje grupują działanie, struktury grupują dane. Porównaj równoległe tablice z tablicą struktur, bez optymalizacji wydajnościowej.

### W12.2 — Tworzymy własny typ
struct Robot, pola char name[50], double x,y,vx,vy; ax,ay w rozwinięciu, jeśli potrzebne. Definicja typu a deklaracja obiektu; inicjalizacja pozycyjna i z nazwanymi polami; kilka niezależnych obiektów; struktura a tablica; typedef jako alias, nie odrębny typ. Przypisanie całej struktury zgodnego typu kopiuje także pola tablicowe; osobno tablicy char nie można przypisać literału po deklaracji. Jeśli struktura zawiera wskaźnik, kopiowany jest adres, nie wskazywane dane. Przykład student z oryginału jako krótkie ćwiczenie alternatywne. Wystarczająca pojemność napisów i terminator, bez powtarzania całego W11.

### W12.3 — Dostęp do pól
r.x, p->x, równoważność (*p).x; p = &r; diagram obiekt i wskaźnik. Pomylenie operatorów, brak nawiasów i NULL jako zadania do analizy, nigdy jako wykonywalny błędny kod. Wykorzystaj wiedzę W6 o adresie i dereferencji.

### W12.4 — Struktura w pamięci
sizeof struktury, pól i wskaźnika; kolejność pól, możliwe przerwy wewnętrzne i końcowe (padding), rozmiar zależny od platformy; ilustruj np. prostym char/double/int i rzeczywistym pomiarem sizeof/offsetof, z podpisem platformy. Nie obiecuj konkretnego layoutu wszystkim implementacjom. Nie porównuj struktur przez memcmp i nie czytaj niezainicjalizowanych bajtów. Bez rozbudowanego ABI; sizeof drukuj %zu, adres obiektu %p z (void *).

### W12.5 — Struktury i funkcje
Porównaj dwie osobno nazwane funkcje (C nie obsługuje przeciążania): move_copy(struct Robot r,double dt) i move_robot(struct Robot *r,double dt); pokaż stan przed i po. Wskaźnik też jest przekazywany przez wartość. print_robot(const struct Robot *r) do odczytu; const nie jest potrzebne przy modyfikowaniu. Nie używaj zmiennych globalnych bez potrzeby. Opcjonalnie krótki przykład zwracania struktury.

### W12.6 — Flota robotów
Mała tablica zainicjalizowanych robotów, iteracja, wywołanie funkcji aktualizującej położenia x += vx*dt, y += vy*dt. Deterministyczne dane i wyniki; przyspieszenie jako proste rozwinięcie, bez złożonej fizyki. Krótkie przypomnienie dynamicznej tablicy struktur z malloc(n * sizeof *p), sprawdzeniem alokacji, inicjalizacją i free; stosuj małe dodatnie rozmiary lub jawnie waliduj rozmiar wejściowy i możliwość przepełnienia. Nie powtarzaj W10.

### W12.7 — Funkcja jako argument
Zachowaj historyczny motyw wskaźników do funkcji jako krótki obowiązkowy rozdział. Zacznij od prostego dopasowanego typu i wywołania, np. double (*f)(double). Następnie pochodna numeryczna (f(x+h)-f(x))/h; wyjaśnij przybliżenie, h dodatnie, sensowny wybór i kontrolę wyniku względem znanej pochodnej. Wykorzystaj dwa różne zgodnie typowane argumenty funkcji; math.h i -lm jeśli potrzebne (w kernelu C zgodna dyrektywa). Zabezpiecz h=0 i NULL albo wyraźnie określ i spełnij warunki wstępne. Nie drukuj wskaźników do funkcji przez %p ani nie konwertuj ich do void*. Zachowaj krótki przykład pola void (*print)(const struct Robot *) i poprawnej inicjalizacji przed wywołaniem; jawne przekazanie obiektu, nie metoda C++ i nie OOP. Historyczny integrator bez return nie może być wzorem poprawnego kodu.

### W12.8 — Lista jednokierunkowa
Zachowaj jako obowiązkowe zwieńczenie kursu. Wyjaśnij różnicę od dynamicznej tablicy: osobno alokowane węzły, nieciągłe położenie możliwe, brak bezpośredniego indeksowania; dodanie po znanym węźle O(1), znalezienie i-tego O(n). Zacznij od struct Node { int value; struct Node *next; }; samoodwołanie przez wskaźnik, head i NULL. Pusta lista → pierwszy węzeł → dodanie na początku → iteracja → dodanie po węźle → usunięcie (głowa, środek, koniec) → zwolnienie całej listy. Użyj konsekwentnie jednego mechanizmu zmiany head: rekomendowane Node **head (lub zwracanie nowej głowy, jeśli lepiej dydaktycznie), wyjaśnij relację do W6. Nie komplikuj API; operacje proste, warunki wstępne jasne. Kontroluj malloc przed dereferencją, inicjalizuj value i next, przy błędzie alokacji zachowaj dotychczasową listę, zwalniaj każdy węzeł raz, nie korzystaj po free, ustaw head na NULL po oczyszczeniu. Przykład listy w historycznym notebooku ma rozbieżność alloc_node/node_alloc, niepoprawne &n1 i niezainicjalizowane pola; clist.cpp ma m.in. brak zwrotu find_last dla pustej listy, brak kontroli malloc i końcowego zwolnienia. Przebuduj w C11, nie kopiuj mechanicznie.
Zilustruj dodanie i usunięcie krok po kroku, pokazując zachowanie starego next, aktualizację połączenia przed free, zmianę head. Diagramy muszą odzwierciedlać kolejność instrukcji.

### W12.9 — Program integracyjny
Mała flota robotów: inicjalizacja, aktualizacja, wypisanie stanu. Opcjonalne rozwinięcie: lista robotów zamiast int; nie wymuszaj powtórzenia całej implementacji listy. Zakończ krótkimi zadaniami: przewidź, znajdź błąd, zmień program. Nie buduj menu, dużej symulacji ani dodatkowych bibliotek.

## 3. Grafiki
Minimum cztery czytelne diagramy: równoległe tablice kontra tablica struktur; obiekt i wskaźnik (kropka/strzałka); rzeczywisty lub jawnie umowny layout z paddingiem; lista z krokami wstawiania/usuwania. Preferuj statyczne sekwencje lub proste animacje tylko gdy rzeczywiście pomocne. Używaj osadzonych attachments notebooka lub niewielkich lokalnych zasobów zgodnie z W6–W7, bez absolutnych ścieżek, z polskimi podpisami. Weryfikuj render i zgodność z kodem.

## 4. Checkpointy

| ID | Zadanie | Warunek PASS |
|---|---|---|
| W12-INT.1 | Inwentaryzacja, źródła, mapa pokrycia | Wszystkie ważne motywy i granica W11/W12 ujęte |
| W12-INT.2 | Szkielet polskiego notebooka | Samodzielna narracja W12.1–9, brak metakomentarzy |
| W12-INT.3 | W12.1–4, typy, dostęp, pamięć | Poprawne C11, testy kopii i dostępu, zgodne schematy |
| W12-INT.4 | W12.5–6, funkcje i flota | Testy kopii vs wskaźnik, przewidywalna aktualizacja, dynamiczna tablica |
| W12-INT.5 | W12.7, wskaźniki do funkcji | Dwa zgodne argumenty, dokładność pochodnej, poprawne pole funkcyjne |
| W12-INT.6 | W12.8, lista | Pusta/jeden/wiele, wstawianie/usuwanie, alokacja, pełne zwolnienie |
| W12-INT.7 | W12.9 i grafiki | Program integracyjny działa, wszystkie diagramy czytelne |
| W12-INT.8 | Audyt techniczny i dydaktyczny | Obowiązkowe kontrole PASS; niezależny przegląd jeśli dostępny |
| W12-INT.9 | Raport i odbiór | SHA, testy, odstępstwa, lista plików do publikacji, czyste drzewo |

## 5. Testy i odbiór
- Walidacja nbformat, kernelspec.name=c, kompletne samodzielne komórki C11, execution_count=null, outputs=[], bez pustych komórek wykonywalnych.
- Wyodrębnij każdą wykonywalną komórkę, kompiluj GCC -std=c11 -Wall -Wextra -Wpedantic przy -O0 i -O2; popraw ostrzeżenia. Obsłuż dyrektywy kernela i -lm. Uruchom z limitem czasu i sprawdź oczekiwane wyniki. Błędne przykłady wyłącznie w Markdown jako analiza. Nie zależ od poprzedniej komórki ani zewnętrznej usługi.
- Testuj ASan/UBSan i wykrywanie wycieków tam, gdzie dostępne (w szczególności lista i dynamiczna tablica). Sanitizery nie zastępują audytu. Dla listy sprawdź pustą, jeden i wiele elementów, kolejność po operacjach, usunięcie głowy/środka/końca, niedostępny węzeł zgodnie z kontraktem, oczyszczenie pustej i niepustej listy; test błędu alokacji przez kontrolowaną symulację w harnessie, nie przez wymuszanie OOM. Zdefiniuj semantykę operacji na NULL. Nie wymagaj sztucznie skomplikowanego API tylko dla testów.
- Testuj pola i kopię struktury (w tym napis), zgodność p->x z (*p).x, różnicę pass-by-value vs wskaźnik, deterministyczne położenia floty, dwa przypadki pochodnej ze stosowną tolerancją; rozmiarów i adresów nie porównuj z twardo zakodowanymi stałymi platformowymi.
- Uruchom notebook w rzeczywistym kernelu C, jeżeli dostępny; sprawdź render Markdown, LaTeX, attachments i linków. Jeżeli środowisko niedostępne, podaj dokładnie niewykonane testy i zakres zastępczej weryfikacji; nie deklaruj nieuzyskanego PASS.
- Sprawdź zakres git diff względem bazy: bez zmian poza 12/, bez zmian historycznych materiałów i README, bez tymczasowych plików w finalnych artefaktach.
- Raport końcowy: bazowy i końcowy SHA, gałąź, stan worktree, status każdego checkpointu, polecenia testowe i wyniki, ograniczenia środowiska, mapa pokrycia, odstępstwa, dokładna lista notebooka i koniecznych assets do selektywnej publikacji, krótka instrukcja ręcznej kontroli. Nie ogłaszaj ukończenia przy obowiązkowym FAIL.

Kryterium sukcesu: student potrafi zaprojektować typ strukturalny, wykorzystać go w tablicy i funkcjach, zrozumieć prostą funkcję przekazywaną jako argument oraz prześledzić budowę i bezpieczną modyfikację dynamicznej listy jednokierunkowej. 
