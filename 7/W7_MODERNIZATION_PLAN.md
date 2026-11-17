# W7 — plan i kontrakt wykonawczy modernizacji

Status: **ZATWIERDZONY PLAN — DO REALIZACJI NA ODRĘBNE POLECENIE**  
Repozytorium: `sgepner/Computer-Science-1`, gałąź bazowa `master`, katalog `7/`.  
Źródła historyczne: `7/lec7.tex`, `7/Lecture 7 Examples.ipynb`, powiązane pliki z `7/` (w tym animacje i `samples/`, o ile istnieją).  
Artefakt docelowy: **`7/Wykład 7.ipynb`**, samodzielny polski notebook w kernelu Jupyter C.  
**Ten plik jest kontraktem dla autonomicznego agenta, a nie materiałem dla studentów.**

## 0. Uruchomienie i zakres upoważnienia

Polecenie „zmodernizuj W7 zgodnie z planem w katalogu 7” uruchamia realizację etapów W7-INT.1–W7-INT.9, testy oraz raport do odbioru. Sama obecność planu na `master` **nie upoważnia** do rozpoczęcia implementacji. Agent samodzielnie rozwiązuje zwykłe problemy techniczne i redakcyjne, ale nie zmienia uzgodnionego zakresu ani nie publikuje efektów na `master`.

**Zakaz driftu:** nie modernizuj W8 lub innych wykładów, nie reorganizuj repozytorium, nie przebudowuj systemu testowego/CI ani instrukcji agentów, nie usuwaj źródeł historycznych. Nie wykonuj merge ani cherry-pick na `master` bez osobnego polecenia. Kreatywność stosuj do narracji, przykładów i grafiki W7, nie do rozszerzania zadań.

## 1. Organizacja i wzorzec W1–W6

1. Pobierz świeży `master`, zapisz bazowy SHA, sprawdź stan drzewa. Przeczytaj obowiązujące instrukcje repozytorium i katalogu, jeśli są dostępne.
2. Załóż osobną gałąź `feature/W7-modernizacja` od bieżącego `master` (o ile nie istnieje; nie nadpisuj cudzej pracy). Prace implementacyjne prowadź tylko na tej gałęzi.
3. Porównaj dokładnie `7/lec7.tex`, `7/Lecture 7 Examples.ipynb`, wszystkie zasoby W7 oraz obowiązujące polskie `1/Wykład 1.ipynb`–`6/Wykład 6.ipynb`. Szczególnie W6 stanowi granicę już wyjaśnionych pojęć: adresy, wskaźniki, rozmiary, `p+1`, wskaźniki jako argumenty.
4. Opracuj **autonomiczny wykład po polsku**, nie translację ani dziennik modernizacji. Żadnych wstawek „w starszej wersji”, odwołań do procesu redakcyjnego, rozkładu minut czy instrukcji dla agenta w materiale studenta.
5. W każdej sekcji zachowuj rytm: problem/pytanie → intuicja → przewidź wynik → eksperyment w C → interpretacja → mała zmiana samodzielna → sprawdzenie zrozumienia. Używaj prostych, motywowanych przykładów, rozsądnego humoru i konsekwentnej notacji.
6. Kod docelowy: C11, kernel `c`, krótkie kompletne przykłady; brak obowiązkowych zależności od zewnętrznych usług. Nie zostawiaj wykonanych outputów ani zbędnych metadanych.
7. Dokumenty robocze, skrypty/testy audytu, raporty i instrukcje agentowe pozostają tylko na gałęzi implementacyjnej. Publikacja końcowa — wyłącznie potrzebny notebook i jego konieczne ilustracje/zasoby, przez selektywne przeniesienie po zgodzie użytkownika, **bez merge całej gałęzi**. Ten plan jest wyraźnie zatwierdzonym wyjątkiem dopuszczonym na `master`.

## 2. Cele dydaktyczne i granice

Po wykładzie student powinien umieć:
- wyjaśnić potrzebę kolekcji danych i zadeklarować, zainicjalizować oraz indeksować jednowymiarową tablicę o stałym rozmiarze;
- zinterpretować indeksy `0..n-1`, rozmiar i położenie elementów w kolejnych komórkach pamięci;
- rozróżnić tablicę od wskaźnika, rozumieć typowe przekształcenie nazwy tablicy we wskaźnik do pierwszego elementu i zapisy `a[i]`, `*(a+i)`, `p[i]`;
- bezpiecznie iterować, sumować dane, wyznaczać średnią, minimum i maksimum;
- przekazywać tablicę do funkcji wraz z długością, rozumieć wpływ zmian elementów i znaczenie `const`;
- generować pseudolosowe dane, odróżniać ziarno od losowości, skalować wyniki do przedziału;
- wyjaśnić i zaimplementować sortowanie bąbelkowe, zilustrować przebiegi, rozumieć koszt w zależności od implementacji;
- otworzyć, sprawdzić, odczytać, zapisać i zamknąć plik tekstowy; połączyć pliki z tablicami w działający program.

**Granice:** nie wprowadzaj dynamicznej alokacji `malloc/free`, tablic 2D, rozwiniętych łańcuchów znakowych ani zaawansowanego API plikowego. W8 pogłębia przetwarzanie plików. Wskaźniki do funkcji z końca historycznego notebooka to **opcjonalna ciekawostka** (ewentualnie krótki dodatek), nie obowiązkowy cel W7. Nie powtarzaj całego W6.

## 3. Docelowa narracja notebooka

Tytuł sugerowany: **„Wykład 7 — Gdy jedna zmienna nie wystarcza: tablice i praca z danymi”**.

| Sekcja | Motyw | Zakres konieczny |
|---|---|---|
| W7.1 | Po co nam tablice? | 100 pomiarów a 100 zmiennych; deklaracja `int tab[5]`, inicjalizacja, typ i pojemność. |
| W7.2 | Tablica w pamięci | Ciągłość, schemat adresów, `sizeof(tab)`, `sizeof(tab[0])`, połączenie z W6; rysunek z indeksami i bajtami. |
| W7.3 | Czy tablica jest wskaźnikiem? | Dokładne rozróżnienie tablicy od wskaźnika, `tab`, `&tab[0]`, `tab[i]`, `*(tab+i)`, `int *p=tab`, ograniczenia konwersji, `sizeof`. Ciekawostka `2[tab]` wyłącznie z ostrzeżeniem o nieczytelności. |
| W7.4 | Tablice i pętle | Poprawne granice, wypełnianie, odczyt, suma, średnia, min/max; wyjście poza zakres = niezdefiniowane zachowanie, niekoniecznie awaria. |
| W7.5 | Tablica jako argument funkcji | `fill(double a[], int n)`, `print(const double *a, int n)`, `average`; długość i pojemność, zanik informacji o pełnym rozmiarze w parametrze, modyfikacje widoczne w wywołującym. |
| W7.6 | Skąd brać przykładowe dane? | `rand`, `RAND_MAX`, `srand`, `time`, stałe ziarno dla testów, `(double)rand()/RAND_MAX`, skalowanie i przesunięcie. |
| W7.7 | Jak sortować? | Bubble sort, zamiana sąsiadów, kolejne przebiegi, animacja lub równoważny diagram, wariant z flagą zamian, koszt `O(n²)` i możliwe `O(n)` tylko w wersji z wcześniejszym stopem. |
| W7.8 | Jak zapisać wyniki? | `FILE *`, `fopen` w trybach `r/w/a` (pozostałe tylko informacyjnie), `fprintf`, `fscanf`, `fclose`, błędy `NULL` i nieudany odczyt, bezpieczne ścieżki. |
| W7.9 | Od danych do wyniku | Program integracyjny: odczyt danych → statystyki → sortowanie → zapis wyniku. Krótkie pytania kontrolne, zadania do samodzielnej modyfikacji. |

Nie ograniczaj się do sztywnej liczby komórek; priorytetem jest czytelny ciąg wykładowy bez nadmiernego rozdrobnienia.

## 4. Wiążące korekty merytoryczne

1. **Tablica nie jest wskaźnikiem.** W wielu wyrażeniach konwertuje się na wskaźnik do pierwszego elementu; wyjątki omów na niezbędnym poziomie (`sizeof`, operator `&` na całej tablicy). Rozróżnij `sizeof(tab)` i `sizeof(p)` oraz utratę informacji o rozmiarze w parametrze funkcji. Nie utożsamiaj `&tab` z `&tab[0]` co do typu, choć wskazują ten sam początek pamięci.
2. Nie twierdź, że `int tab[n]` jest bezwzględnie niepoprawne w C: VLA istnieją w odpowiednich wersjach/implementacjach. W programie kursu świadomie używamy tablic o **stałym rozmiarze**; `#define MAX_SIZE 50` może służyć ograniczeniu pojemności. Rozróżnij stałą pojemność tablicy od liczby aktywnie używanych elementów `n`.
3. Dostęp poza zakresem (np. `tab[3]` przy `int tab[3]`) to **undefined behavior**, nie gwarantowany błąd wykonania. Nie uruchamiaj przykładów UB jako normalnych komórek. Można zamieścić je do analizy „znajdź błąd” bez wykonania.
4. Nie kopiuj z oryginalnego W7 kodu `int *p=(int *)&a` na `double` do modyfikacji bajtów: zagadnienie reprezentacji było już ostrożnie opracowane w W6. Tu arytmetyka wskaźników odbywa się **wewnątrz rzeczywistych tablic**.
5. `sizeof` zwraca `size_t`; stosuj `%zu`, bez osobnego wykładu o `size_t`. Adresy: `%p` i `(void *)`. Rozmiary `int`/ `double` podawaj jako typowe dla demonstracyjnego Linux/GCC, nie aksjomaty standardu.
6. Dla `n=0` nie dziel przez zero; odczyty i zapisy nie mogą przekroczyć pojemności. Czytanie elementów niezainicjalizowanych jest błędem, nawet jeśli pamięć wydaje się zawierać „jakąś liczbę”.
7. `rand` zwraca pseudolosową liczbę z `[0,RAND_MAX]`. Ziarno ustaw **raz** przed generowaniem sekwencji; stałe ziarno daje odtwarzalne przykłady. `time(NULL)` nie gwarantuje różnej sekwencji dla startów w tej samej sekundzie; pseudolosowość to nie kryptografia. Dla skalowania wyjaśnij końce przedziału i rodzaj aproksymacji; nie udawaj idealnie równomiernego rozkładu.
8. Bubble sort bez optymalizacji w oryginalnym kodzie wykonuje `O(n²)` porównań również dla już posortowanych danych. Najlepszy `O(n)` osiąga wariant z flagą braku zamian.
9. `fopen` może zwrócić `NULL`; sprawdzaj przed użyciem. `fscanf` sprawdzaj po liczbie udanych konwersji, a nie tylko liczbie wykonanych wywołań. Przy zapisie kontroluj ważne błędy i wynik `fclose` tam, gdzie decyduje o kompletności danych. Tryb `w` usuwa starą zawartość. Testowe pliki trzymaj w jasno wskazanym katalogu testowym, nie nadpisuj danych użytkownika.
10. Oryginalne przykłady adresów wskaźników do funkcji przez `void *` oraz `%p` nie są przenośnym wzorcem standardowego C dla wskaźników do funkcji. Jeśli dołączasz bonus, pokaż **poprawnie typowany wskaźnik do funkcji i wywołanie**, bez niedozwolonych konwersji jako podstawy kodu.

## 5. Zachowanie oryginalnych przykładów i granica z W8

Wykonaj mapę pokrycia każdego ważnego elementu historycznego LaTeX i notebooka, z decyzją **zachowaj / przebuduj / świadomie pomiń** i powodem. W szczególności uwzględnij:
- deklaracje i indeksowanie tablic, diagramy pamięci, relację tablicy i wskaźnika, dziwne `2[tab]`;
- przekazywanie tablic do funkcji, pojemność `MAX_SIZE`, `rand/srand/time`, skalowanie losowych `double`;
- animację i implementację bubble sort;
- `FILE *`, `fopen/fclose`, `fprintf/fscanf`, porównanie `printf` i `fprintf`, tryby `r/w/a`;
- ćwiczenia: punkty `sin(x)` do wykresu, punkty wewnątrz okręgu, generowanie liczb i średnia + zliczanie powyżej/poniżej, wczytanie-sortowanie-zapis;
- bonus: wskaźniki do funkcji — opcjonalny, z prawidłowym C.

Nie wymagaj, by wszystkie te ćwiczenia stały się rozbudowanymi działami obowiązkowymi. Przykład integracyjny powinien spinać kluczowe pojęcia, a pozostałe mogą być krótkimi zadaniami do wykonania. W8 pozostaje osobnym wykładem o przetwarzaniu danych z plików.

## 6. Grafika, zasoby, środowisko

- Zachowaj i w razie potrzeby zmodernizuj schematy TikZ z `lec7.tex`, szczególnie ciągły układ elementów, indeksy, adresy oraz tablica vs wskaźnik. Preferuj czytelne podpisy po polsku i spójną legendę zgodną z W6. Można zastąpić rysunek nowym, jeżeli jest dydaktycznie lepszy.
- Wyszukaj `movie.gif`, `something-*` i inne materiały do sortowania; nie pozostawiaj martwych odwołań. Jeśli animacja wymaga nieproporcjonalnie dużych zasobów, zastąp ją prostą sekwencją kroków/rysunków. Nie kopiuj setek klatek bez potrzeby.
- Nie pozostawiaj absolutnych ścieżek z komputera autora ani zależności od pliku, który nie jest dostępny w repo. Dla operacji na plikach zapewnij jawny, powtarzalny etap utworzenia danych albo mały plik wejściowy dołączony do wykładu.
- Materiały studenckie nie zawierają agentowych procedur testowych ani metadanych wdrożeniowych.

## 7. Bramki implementacyjne

| Etap | Zadanie | Warunek PASS |
|---|---|---|
| W7-INT.1 | Inwentaryzacja źródeł, assets, W6 i W8 oraz mapa pokrycia | Każdy istotny motyw otrzymał decyzję i powód; brak ukrytej regresji zakresu |
| W7-INT.2 | Szkielet polskiego `Wykład 7.ipynb` | W7.1–W7.9 tworzą samodzielną narrację bez meta-komentarzy |
| W7-INT.3 | Tablice, pamięć i wskaźniki (W7.1–W7.3) | Technicznie poprawne rozróżnienie tablic/wskaźników, grafiki zgodne z kodem |
| W7-INT.4 | Pętle i funkcje (W7.4–W7.5) | Poprawne granice, rozmiary, `const`, testy wartości i zmian tablicy |
| W7-INT.5 | Pseudolosowość (W7.6) | Deterministyczny scenariusz testowy, jasne przeskalowanie |
| W7-INT.6 | Sortowanie (W7.7) | Porównanie przebiegów, scenariusze narożne, zgodna analiza złożoności |
| W7-INT.7 | Pliki i program integracyjny (W7.8–W7.9) | Sprawdzanie błędów, uruchomienie od danych wejściowych do pliku wynikowego |
| W7-INT.8 | Audyt kodu, notebooka, treści i zasobów | Wszystkie obowiązkowe kontrole z §8 PASS lub udokumentowany blokujący FAIL |
| W7-INT.9 | Raport i lista plików do publikacji | Przegląd różnic, instrukcja kontroli prowadzącego, zero nieautoryzowanych zmian na `master` |

Nie rozpoczynaj kolejnego etapu przy istotnym FAIL poprzedniego; najpierw napraw w obrębie ustalonego zakresu. Unikaj mnożenia dokumentów kontrolnych i nie dopisuj postępów modernizacji do głównego README.

## 8. Odbiór

**Testy techniczne:**
- notebook jest prawidłowym JSON `.ipynb` z `kernelspec.name=c`; brak przypadkowych outputów, niepotrzebnych metadanych i pustych wykonywalnych komórek;
- sprawdzenie komórek C11 przez GCC z `-Wall -Wextra -Wpedantic`, w `-O0` i `-O2`; dla programów z odczytem pamięci i sortowaniem, adekwatne ASan/UBSan; sanitizery nie dają pełnej gwarancji;
- wykonanie w rzeczywistym kernelu C, jeśli dostępny; jeśli nie, raport uczciwie wymienia testy niezrealizowane;
- testy: mała tablica, jeden element, `n=0` tam gdzie logicznie dozwolone; sortowanie rosnące/malejące/równe/duplikaty; powtarzalne losowanie przy stałym ziarnie;
- pliki: poprawne wejście, brak pliku, dane nieprawidłowe, zbyt duże `n`, koniec pliku, bezpieczne lokalizacje zapisu;
- względne zasoby i grafiki renderują się w notebooku, nie ma martwych linków ani zależności wyłącznie od historii wykonania.

**Audyt dydaktyczny:**
- każdy fragment uczy konkretnego pojęcia, nie tylko demonstruje kod;
- zgodność ze zmodernizowanym W6, brak założeń o znajomości W8;
- żaden kod przeznaczony do uruchomienia nie wykonuje UB, nie czyta niezainicjalizowanej pamięci, nie otwiera niezabezpieczonego `NULL`;
- przejrzysta mapa pokrycia historycznych źródeł i uzasadnione pominięcia;
- wszystkie schematy odpowiadają rzeczywistej semantyce i kodowi.

**Raport końcowy:** gałąź, bazowy i końcowy SHA, lista zmienionych plików, W7-INT.1–W7-INT.9 PASS/FAIL, zakres wykonanych i pominiętych testów, odstępstwa, wyniki przeglądu dydaktycznego, dokładna lista plików do przeniesienia na `master`, instrukcja ręcznej kontroli. **Nie ogłaszaj ukończenia przy obowiązkowym FAIL.**

## 9. Ograniczenia bezwzględne

- Nie zmieniaj zakresu W7 w kierunku pełnego kursu o plikach, pamięci dynamicznej, tablicach wielowymiarowych lub funkcjach wskaźnikowych.
- Nie ucz, że tablica „jest wskaźnikiem”, a błędny indeks „na pewno powoduje segfault”.
- Nie przenoś demonstracji dwóch `int` w `double` z W6 jako poprawnego przykładu indeksowania tablic.
- Nie pozostawiaj bez kontroli `fopen`, `fscanf`, zakresów tablic ani pojemności wejścia.
- Nie przenoś do finalnego notebooka instrukcji agentowych, zapisków o modernizacji, budżetu czasu ani niezatwierdzonych zmian innych wykładów.
- Nie wykonuj merge i nie publikuj implementacji na `master` bez odrębnej dyspozycji użytkownika.

---

**Kryterium sukcesu:** student potrafi przejść od pojedynczej zmiennej i wskaźnika z W6 do bezpiecznego przetwarzania całej tablicy, zrozumieć prosty algorytm sortowania i przenieść dane między pamięcią programu a plikiem — bez znajomości W8.
