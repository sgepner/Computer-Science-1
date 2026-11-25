# W8 — kontrakt wykonawczy modernizacji

Status: ZATWIERDZONY DO REALIZACJI NA POLECENIE STARTOWE
Repozytorium: sgepner/Computer-Science-1
Gałąź robocza: feature/W8-modernizacja
Baza: master, a9e95d68bb5cf25e3020373ceb4b7019bc864ec9
Artefakt docelowy: `8/Wykład 8.ipynb` (Jupyter, kernel c).
Ten dokument jest instrukcją dla lokalnego agenta, nie materiałem studenckim.

## 0. Uruchomienie i uprawnienia

Realizuj w lokalnym worktree już przypisanym do gałęzi feature/W8-modernizacja. Nie przełączaj głównego drzewa, nie twórz kolejnego worktree, nie resetuj ani nie usuwaj cudzych zmian. Sprawdź git status, git branch --show-current, git rev-parse HEAD oraz instrukcje AGENTS.md (także nadrzędne i lokalne, jeśli istnieją). Przy niezgodnej gałęzi lub konflikcie zatrzymaj się. Nie uruchamiaj ChatGPT Work.

Polecenie startowe prowadzącego uruchamia całą kampanię W8-INT.1–9 w trybie continuous: samodzielnie przechodź do następnej bramki po udokumentowanym PASS; przy FAIL napraw i ponów testy tego samego etapu. Przy rzeczywistym blokerze podaj dowody i zatrzymaj się. Jeśli dostępne, użyj Execution Control continuous max_workers=2 oraz Test Review Advance jako polityki weryfikacji; niezależny przegląd końcowy, jeśli możliwy. Brak tych umiejętności nie blokuje pracy: zasady są opisane tutaj.

Dozwolone są lokalne commity na gałęzi roboczej. Nie pushuj, nie wykonuj merge/cherry-pick do master bez odrębnej dyspozycji. Nie modernizuj innych wykładów. Nie zmieniaj README głównego, infrastruktury kursu, CI ani historycznych źródeł W8. Nie nadpisuj lokalnych danych użytkownika. Nie dodawaj nowych zależności produkcyjnych.

## 1. Źródła i wzorzec

Przeczytaj 8/lec8.tex, 8/lec8.pdf, wszystkie 8/samples/*, 7/Wykład 7.ipynb, 7/W7_MODERNIZATION_PLAN.md oraz 9/lec9.tex. Obejrzyj również polskie notebooki W1–W6 jako wzorzec narracji, formatu, kodu i grafiki. Zweryfikuj zgodność PDF z TeX lokalnie; dotychczasowy audyt dotyczył źródła TeX i przykładów, nie renderu PDF. W8 nie ma istniejącego notebooka. W7 ma już 53 komórki (15 kodu) i obejmuje tablice, wskaźniki, funkcje, losowanie, bubble sort, tryby plików oraz integrację odczytu, statystyk i sortowania. W8 rozszerza zastosowania, nie powtarza tego wykładu.

Zachowaj autonomiczny polski materiał, nie tłumaczenie starych slajdów. Rytm: problem → intuicja → przewidź → eksperyment C → interpretacja → mała modyfikacja → kontrola. Pisz naturalnie, bez komentarzy o modernizacji, budżetów minut, nadmiaru sekcji czy technicznych dygresji. Zachowaj sens i humor autora. Wzory zapisuj w LaTeX Markdown jak w poprzednich notebookach. Kod C11, pełne krótkie programy z main(void), polskie objaśnienia i przede wszystkim printf zgodnie ze stylem kursu; nie wprowadzaj puts jako równoległego tematu. Diagnostyka może wykorzystywać fprintf(stderr,...) lub perror z krótkim objaśnieniem.

## 2. Cel i granice

Tytuł: „Wykład 8 — Od danych do wyników: pliki, algorytmy i eksperymenty”.

Student umie uzgodnić format danych między programami, wygenerować i zapisać dane, wczytać dane z kontrolą statusu, dobrać algorytm do problemu, analizować i sortować pomiary, zapisać wynik do odrębnego pliku oraz generować i klasyfikować punkty. Rozumie, że plik może łączyć niezależne programy i że nie zawsze potrzebuje tablicy (np. klasyfikacja punktów w locie), natomiast sortowanie i dwupassowa analiza średniej korzystają z tablicy.

Wyłącznie jednowymiarowe tablice o stałej pojemności, z odrębną liczbą aktywnych elementów. Bez malloc/free, tablic 2D, własnych parserów tekstu, struktur, plików binarnych, rozbudowanego API pozycjonowania, zaawansowanego CSV. Nie wprowadzaj zagadnień W9–W12 przedwcześnie. r/w/a przypomnij krótko; r+/w+/a+ można wymienić informacyjnie z ostrzeżeniem, bez ćwiczeń aktualizacyjnych.

## 3. Docelowa narracja

| Sekcja | Zakres i wynik |
|---|---|
| W8.1 Po co nam pliki? | Dwa niezależne programy, trwałość danych, FILE *, krótki powrót do W7. Schemat generator → plik → analizator → wynik. |
| W8.2 Uzgadniamy format | Pierwsza liczba n to liczba rekordów, nie pomiar; następnie n liczb lub n par. Typ, separator, zakres, pojemność; co gdy producent i konsument rozumieją format inaczej? |
| W8.3 Generator pomiarów | rand/srand znane z W7; stałe ziarno raz, małe ograniczone wartości, zapis nagłówka i danych. Odtwarzalne doświadczenie, bez obowiązkowego scanf z klawiatury. |
| W8.4 Analiza | Wczytanie do tablicy, suma w double, średnia, liczba poniżej/równych/powyżej; ręczny przykład oraz zmiana danych. Dwa przebiegi i dlaczego średnia musi być znana przed drugim. |
| W8.5 Sortowanie | Użyj znanego bubble sort z W7; skup się na wczytaniu, sortowaniu i zapisie do nowego pliku z tym samym formatem. Nie wyprowadzaj ponownie algorytmu. |
| W8.6 Od funkcji do punktów | x_i=x_min+i*(x_max-x_min)/(n-1), i=0..n-1, n>=2. Sinus, oba krańce, licznik całkowity, acos(-1.0), math.h, linkowanie -lm. |
| W8.7 Czy punkt należy do koła? | Odczyt par, x*x+y*y<=1.0, klasyfikacja wewnątrz/na brzegu/na zewnątrz (dla dokładnych punktów testowych), zliczenie; przetwarzanie w locie bez tablicy. |
| W8.8 Co może pójść źle? | Nieudane otwarcie, EOF vs niedopasowanie, brak pola, zły nagłówek, zbyt dużo danych, błąd zapisu. Kontrole stosowane także w wcześniejszych przykładach; tutaj celowe bezpieczne eksperymenty. |
| W8.9 Integracja i kontrola | Dwa przepływy danych, ćwiczenia modyfikacji, przewidywanie wyniku, krótkie pytania oraz naturalna granica przed W9. |

Nie wymuszaj liczby komórek. Pokazuj problem, algorytm, kod i wynik; nie rozbudowuj każdego przykładu w projekt. Dwa czytelne scenariusze są ważniejsze niż kolekcja niezwiązanych programów.

## 4. Wiążące korekty i mapa historycznych źródeł

- lec8.tex: napraw literówkę fcanf na fscanf, nie otwieraj do odczytu w trybie w, ścieżki względne zamiast windowsowych, kontrola fopen/fclose. Poprawki wdrażaj w nowym notebooku, nie edytuj historycznego TeX/PDF.
- rand.c: sprawdź n i status otwarcia/zapisu/zamknięcia; ogranicz pomiary do jawnego, małego przedziału (np. -99..99), stałe ziarno do odtwarzalności; nie obiecuj identycznej sekwencji rand między bibliotekami ani idealnej jednostajności modulo.
- avg.c: kontroluj 1<=n<=MAX_SIZE, każdą konwersję, sumę w double, liczbę danych; pokaż trzy kategorie i ich sumę n. Zero danych nie ma średniej.
- sort.c: nie używaj r+; wejście tylko r, po pełnym poprawnym odczycie oddzielny plik w. Nie doklejaj separatora i drugiej listy. Wyjście ma być ponownie wczytywalne, wejście niezmienione. Zachowaj duplikaty i liczność.
- rand.dat: historyczny plik ma nagłówek 34, wartości, separator i drugą listę; nie używaj jako czystego wzorca. Zostaw bez zmian, wyjaśnij problem na małym przykładzie.
- sin.c: brak nagłówka mimo oczekiwania circle.c; zapisz n i n par, sprawdzaj n>=2 i górną granicę dydaktyczną, korzystaj z pi=acos(-1.0), nie M_PI. Dobierz precyzję zapisu i tolerancję testów, uwzględnij przybliżenia zmiennoprzecinkowe przy krańcach. 
- circle.c: sprawdzaj n i każdą parę (fscanf zwraca 2 przy dwóch udanych konwersjach); ustal dokładny separator zgodny z generatorem. Użyj skończonych, umiarkowanych współrzędnych z określonym zakresem. Dla punktów brzegowych pokaż dokładne przykłady (1,0), (0,-1); nie obiecuj matematycznej dokładności dla dowolnych danych zmiennoprzecinkowych. Jeśli rozróżniasz trzy klasy dla ogólnych danych, jawnie omów przyjętą tolerancję lub dokładny warunek w arytmetyce maszynowej.
- sin.dat: istniejący przykład ma nagłówek 20 i pary rozdzielone przecinkiem; pozostaw historyczny plik, nowy generator i konsument muszą mieć wspólny jawny format.
- array.c: tablice 2D, świadomie poza W8, zachować w archiwalnym katalogu; nie przenosić ani zmieniać W9.
- e4.c, e5.c: przykłady pytań testowych niezwiązane z plikami; świadomie poza główną narracją, ewentualne krótkie ćwiczenie powtórkowe tylko po sprawdzeniu poprawności i treści zadania. Nie odtwarzaj brakującej treści egzaminu z domysłów.

Mapa pokrycia powinna również uwzględnić wszystkie pięć ćwiczeń i wzmiankę o pytaniach testowych z prezentacji. Zapisz decyzje w krótkiej sekcji roboczej tego dokumentu lub raporcie, nie w notebooku.

## 5. Kontrakty i bezpieczeństwo przykładów

Przyjmij dwa jawne formaty tekstowe. Pomiary: pierwszy wiersz n, potem n liczb całkowitych (np. zakres -99..99, 1..200 rekordów). Punkty: pierwszy wiersz n, potem n par x y oddzielonych białym znakiem (lub konsekwentnie przecinkiem; wybór i przykład zapisane w notebooku). Dla generatora sinusa n>=2, klasyfikator może przyjąć n>=1; limity jawne. Nie mieszaj formatów. Dane testowe ogranicz do bezpiecznych pól liczbowych. Przy niezaufanych/nieograniczonych tokenach sama kontrola wyniku fscanf nie wystarcza do ochrony przed przepełnieniem konwersji; wykorzystaj prostą ograniczoną szerokość i kontrolę granicy tokenu na wzór W7 lub jawnie ograniczony format i odpowiednio bezpieczny odczyt. Nie zamieniaj tego w rozbudowany parser; jasno nazwij granice walidacji, nie obiecuj pełnej walidacji dowolnego tekstu. Jeśli format dopuszcza białe znaki, nie twierdź, że fscanf automatycznie egzekwuje fizyczne wiersze. Dodatkowe rekordy/niedozwolone tokeny odrzuć w przykładzie ścisłego formatu albo jawnie opisz, że są ignorowane; preferowany ścisły format dla obu przepływów. Nie używaj wzorca while(!feof(file)). Nie wykorzystuj wartości z nieudanej lub częściowej konwersji.

Każde fopen sprawdzaj przed użyciem; sprawdzaj fprintf<0 i fclose!=0, rozróżniaj koniec wejścia i błąd strumienia w odpowiednich miejscach. Zawsze zamykaj otwarty strumień na ścieżkach błędu; po fclose nie korzystaj z niego. Nie otwieraj wyniku do zapisu przed walidacją wejścia. Pamiętaj, że po błędzie może pozostać stary wynik albo niepełny nowy plik — nie nazywaj go sukcesem. Nie wymagaj atomowego zapisu ani zaawansowanego API.

## 6. Zasoby i środowisko

Docelowo 8/Wykład 8.ipynb oraz minimalne 8/w8_dane/ (pomiary.txt, punkty.txt, opcjonalny krótki README dla studenta). Odtwarzalne generatory i wyniki używają osobnych nazw w8_demo_*.txt. Nigdy nie nadpisują wzorców ani historycznych samples. Dane wejściowe dostępne z czystego checkoutu; jeżeli ćwiczenie wymaga wygenerowania danych, jawnie wskaż komórkę przygotowującą i zapewnij także prosty wzorzec do samodzielnego uruchomienia analizatora. Notebook działa z katalogu 8/, wyjaśnij ścieżki względne. Każda komórka C jest samodzielnym programem, zależności plikowe jawne; brak zależności od wcześniej zdefiniowanych funkcji w innych komórkach. Math: //%ldflags:-lm dla kernela C zgodnie z W7. Grafika opcjonalna: mały schemat przepływu i wykres punktów/koła tylko jeśli pomagają; bez nowych zależności. Nie dodawaj wygenerowanych plików do publikacji. Zachowaj historyczne pliki bez zmian.

## 7. Bramki wykonawcze

| Etap | Zadanie | PASS |
|---|---|---|
| W8-INT.1 | Inwentaryzacja TeX/PDF, samples, W7/W9, instrukcje i mapa pokrycia | Każdy istotny motyw ma decyzję i powód, baza i worktree ustalone |
| W8-INT.2 | Szkielet notebooka W8.1–9 | Prawidłowy JSON/kernel c, spójna polska narracja, brak metakomentarzy |
| W8-INT.3 | Format, dane, generator pomiarów | Odtwarzalny zapis, jawne granice, generator zgodny z kontraktem |
| W8-INT.4 | Analiza i sortowanie | Ręczny wynik, testy zakresu, duplikatów i osobnego pliku, wejście niezmienione |
| W8-INT.5 | Generowanie punktów | n rekordów i nagłówek, krańce, poprawne wartości sinusa z tolerancją, n>=2 |
| W8-INT.6 | Klasyfikacja punktów | Zgodność formatu, przypadki wewnątrz/brzeg/zewnątrz, odczyt par i poprawne liczności |
| W8-INT.7 | Błędy i ćwiczenia | Kontrolowane błędy, kompletne zadania i interpretacje, brak niebezpiecznych wykonywalnych przykładów |
| W8-INT.8 | Audyt końcowy | Weryfikacja techniczna, dydaktyczna, zasobów i zakresu według §8 |
| W8-INT.9 | Raport i selekcja publikacji | Dokładna lista plików, SHA, dowody, ograniczenia, brak zmian poza W8 i brak merge |

Aktualizuj krótką tabelę stanu poniżej; nie twórz osobnych plików CURRENT/ROADMAP/DECISIONS, jeśli repo nie wymaga. Po każdej bramce zapisz polecenia i rezultaty, napraw FAIL przed przejściem dalej. Możesz robić lokalne atomowe commity. Nie deklaruj PASS bez dowodu; jeśli kernel niedostępny, odnotuj to jako ograniczenie, wykonaj testy GCC, nie deklaruj pełnego odbioru kernela. Obowiązkowy FAIL blokuje zamknięcie.

## 8. Testy i odbiór

- Sprawdź JSON, nbformat (jeśli dostępny), kernelspec.name=c, brak przypadkowych outputów i execution_count, względne linki, brak zbędnych metadanych, czytelność Markdown/LaTeX. Obejrzyj notebook w Jupyter lub renderze, jeśli dostępny.
- Wyodrębnij kompletne programy C i kompiluj GCC -std=c11 -Wall -Wextra -Wpedantic -O0 i -O2, z -lm tam gdzie potrzebne. Uruchom w izolowanym katalogu tymczasowym z kopią danych i kontrolą kodu wyjścia, timeoutem. Adekwatne ASan/UBSan dla dostępu do tablic, jeśli środowisko pozwala. Nie uruchamiaj UB jako przykładu; błędne fragmenty wyłącznie do analizy w Markdown.
- Testuj poprawny plik, brak pliku, zły nagłówek, n=0, n<0, n=1, pojemność i pojemność+1, niepełne rekordy, niedopasowanie, dodatkowe dane zgodnie z kontraktem. Sprawdź granice pola liczbowego i statusy przy błędzie zapisu/otwarcia; nie niszcz danych użytkownika. Testuj realne pliki wyjściowe, nie tylko stdout.
- Statystyka: np. 3,9,5,-1,4,4 daje sumę 24, średnią 4, po 2 poniżej/równe/powyżej. Jedna wartość oraz wszystkie równe. Sort: rosnące, malejące, duplikaty, jeden element; porównaj ze wzorcem i sprawdź, że oryginalny plik nie zmienił się. Random: powtarzalność w tym samym środowisku dla stałego ziarna, liczność i zakres, bez hardkodowania bibliotecznej sekwencji.
- Sinus: n=9, x=0,pi/2,pi,3pi/2,2pi na odpowiednich indeksach i y bliskie 0,1,0,-1,0. n=1 odrzucane przez generator. Zweryfikuj liczbę par i ponowny odczyt. Klasyfikacja: (0,0),(1,0),(0,-1),(2,0) oraz punkty ujemne; przypadki niepełnej pary, suma kategorii n. Dobierz tolerancję z precyzji pliku, udokumentuj.
- Wykonaj notebook w rzeczywistym kernelu C od czystego checkoutu, jeśli dostępny; nie instaluj nieuzgodnionych zależności systemowych. Uczciwie rozróżnij pełne uruchomienie od ekstrakcji GCC. Sprawdź ponowne uruchomienie generatorów i brak nadpisania wzorców. Usuń artefakty testowe z drzewa publikacji.
- Audyt dydaktyczny: zgodność z W7, bez przedwczesnego W9, wszystkie pięć historycznych przykładów, sensowna motywacja, przewidywanie i interpretacja, jasny format plików, poprawność matematyczna i C. Przegląd diff względem bazy, brak zmian poza dozwolonym zakresem. Nie powtarzaj całego kursu w testach.

## 9. Zakończenie i przekazanie

Raport końcowy: tryb, gałąź, bazowy SHA, końcowy SHA, faktycznie testowany SHA, status drzewa, wszystkie W8-INT.1–9 i dowody PASS/FAIL, mapa pokrycia, ograniczenia środowiska, lista plików zmienionych i dokładna lista plików przeznaczonych do selektywnego przeniesienia na master, instrukcja ręcznej kontroli. Zachowaj dokumentację agentową i ewentualne testy wyłącznie w gałęzi roboczej. Bez publikacji na master, bez merge, bez push bez osobnej zgody. Nie usuwaj historycznych źródeł. Zakończ COMPLETE wyłącznie po spełnieniu wszystkich obowiązkowych bramek, inaczej BLOCKED z konkretnym powodem.

## 10. Stan roboczy (aktualizuje wykonawca)

Aktywny etap: W8-INT.1. Status: NOT STARTED. Nie wykonano testów implementacyjnych. Po każdym etapie aktualizuj zwięzły stan oraz dowody w tym miejscu lub jednym istniejącym raporcie roboczym.

| Etap | Stan |
|---|---|
| W8-INT.1 | NOT STARTED |
| W8-INT.2 | NOT STARTED |
| W8-INT.3 | NOT STARTED |
| W8-INT.4 | NOT STARTED |
| W8-INT.5 | NOT STARTED |
| W8-INT.6 | NOT STARTED |
| W8-INT.7 | NOT STARTED |
| W8-INT.8 | NOT STARTED |
| W8-INT.9 | NOT STARTED |
