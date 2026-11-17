# W6 — plan i kontrakt wykonawczy modernizacji

Status: **ZATWIERDZONY PLAN — DO REALIZACJI**  
Repozytorium: `sgepner/Computer-Science-1`, katalog `6/`  
Stan wyjściowy: historyczne `6/lec6.tex`, `6/Lecture 6 examples.ipynb`, programy `6/samples/`.  
Docelowy artefakt: **`6/Wykład 6.ipynb`**, polski, autonomiczny notebook do wykładu z podstaw programowania w C.  
Ten plik jest **instrukcją wykonawczą dla autonomicznego agenta**, nie materiałem dla studentów.

## 0. Polecenie uruchamiające i zakres upoważnienia

Polecenie „zmodernizuj W6 zgodnie z planem w katalogu 6” oznacza: zrealizuj wszystkie etapy opisane niżej, wykonaj lokalne testy, udokumentuj wyniki, przygotuj przegląd zmian i przedstaw rezultat do odbioru. Nie czekaj na dodatkowe potwierdzenia dla zwykłych decyzji redakcyjnych. Zachowaj możliwość eskalacji rzeczywistych konfliktów merytorycznych.

**Nie traktuj samej obecności tego planu jako upoważnienia do rozpoczęcia zmian.** Dopiero osobne polecenie użytkownika uruchamia realizację. Na dzień sporządzenia planu zmiana dotyczy wyłącznie tego pliku.

**Zakaz niezamówionych działań:** nie modernizuj W7 ani innych wykładów, nie porządkuj całego repozytorium, nie rozszerzaj zakresu o narzędzia CI, system agentowy lub migracje, nie kasuj źródeł historycznych. Nie wykonuj merge, nie wypychaj zmian na `master` bez osobnego polecenia użytkownika. Nie zmieniaj niezwiązanych plików. Własną kreatywność wykorzystuj do ulepszenia przykładów i narracji w ramach W6.

## 1. Organizacja pracy i zasady z W1–W5

1. Przed implementacją pobierz najnowszy stan repozytorium i zweryfikuj rzeczywistą gałąź bazową. Obecnie domyślną gałęzią repozytorium jest `master` (użytkownik może potocznie mówić „main”).
2. Wykonaj implementację na **osobnej gałęzi roboczej** (proponowana nazwa `feature/W6-modernizacja`), od aktualnej bazy. Nie twórz gałęzi, jeżeli polecenie użytkownika ogranicza się do audytu lub planowania.
3. Za źródło treści uznaj `6/lec6.tex`, `6/Lecture 6 examples.ipynb` i związane programy `6/samples/`. Przeglądaj też `4/Wykład 4.ipynb`, `5/Wykład 5.ipynb`, pozostałe zmodernizowane W1–W5 oraz historyczny W7 wyłącznie dla granic programu.
4. Utwórz nowy **samodzielny polski** notebook. To nie ma być dosłowne tłumaczenie slajdów ani kronika modernizacji: usuń historyczne wzmianki o dawnych wersjach, komentarze robocze, czasy przeznaczone na sekcje i metatekst redakcyjny.
5. Zachowaj styl W1–W5: pytanie lub problem → intuicja → przewidywanie wyniku → eksperyment C → interpretacja → mała samodzielna zmiana → kontrola zrozumienia.
6. Kod ma być krótki, czytelny, kompletny i dostosowany do jupyterowego kernela C, standard C11. Nie uzależniaj uruchamiania notebooka od zewnętrznych plików, jeśli można tego uniknąć.
7. Dokumentacja wdrożeniowa, pliki instrukcji agenta, robocze testy, skrypty kontrolne i raporty pozostają w gałęzi roboczej i **nie wchodzą do `master` w finalnym przeniesieniu materiałów**. Plan niniejszy jest wyjątkiem: użytkownik wyraźnie polecił przechowywać go w `6/` na gałęzi domyślnej.
8. Przy publikacji użytkownik preferuje przeniesienie wyłącznie notebooka oraz naprawdę koniecznych ilustracji/zasobów, **bez merge całej gałęzi**; finalne przeniesienie realizuj wyłącznie na wyraźne polecenie.

## 2. Cele dydaktyczne

Po W6 student powinien:
- rozumieć różnicę między wartością obiektu, adresem obiektu, adresem samego wskaźnika i wartością przechowywaną we wskaźniku;
- potrafić wyjaśnić `&`, `*`, `int *p`, `p = &a` i `*p = 20`;
- wiedzieć, że sam wskaźnik jest obiektem mającym własny adres;
- odczytywać i zmieniać wartości przez wskaźnik oraz rozumieć podstawy `int **`;
- wyjaśnić, dlaczego funkcja przyjmująca `int` zmienia tylko swoją kopię, a funkcja przyjmująca `int *` może zmienić obiekt wywołującego; pamiętać, że **w C wszystkie argumenty są przekazywane przez wartość — również wskaźniki**;
- zastosować wskaźniki do parametru wyjściowego i funkcji zamieniającej dwie wartości;
- znać podstawowe zagrożenia: niezainicjalizowany wskaźnik, `NULL`, dereferencja wskaźnika niepoprawnego lub wskazującego poza czas życia obiektu;
- rozumieć, że arytmetyka wskaźnika zachodzi w jednostkach rozmiaru wskazywanego typu, a nie w pojedynczych bajtach;
- rozumieć, jak rozmiar, wyrównanie i reprezentacja bajtowa ograniczają interpretację zawartości pamięci.

**Granica zakresu:** nie uczymy tu tablic ani dostępu do elementów tablic, iterowania po tablicach, dynamicznej alokacji (`malloc`/`free`) ani pełnej organizacji pamięci procesu. Tablice i ich relacja ze wskaźnikami są przedmiotem W7. W6 powinien być autonomiczny i nie wymagać od studenta znajomości W7.

## 3. Uzgodniona platforma i uproszczenia

Platforma demonstracyjna: Linux/x86-64 z GCC (typowe środowisko 64-bitowe). W tym środowisku prezentujemy `char` = 1 B, `int` = 4 B, `double` = 8 B, zwykłe wskaźniki do tych typów = 8 B. Nie podawaj tych rozmiarów jako uniwersalnych praw C; wystarczy krótki komentarz, że zależą od platformy.

Na poziomie początkującym wskaźnik opisuj jako **typ zmiennej przechowującej adres**. Podkreśl:
- rozmiar wskaźnika na naszej platformie jest taki sam dla `int *` i `double *` (8 B);
- różny jest rozmiar wskazywanego obiektu (4 B albo 8 B);
- nie myl wielkości wskaźnika z rozmiarem jego celu.

**Nie rozwijaj wykładu o osobny temat `size_t`**, o wszystkie modele danych ani o pełny przegląd egzotycznych architektur. Jeżeli trzeba wypisać `sizeof`, użyj poprawnego `%zu` i co najwyżej jednego zdania o formacie. Nie utrwalaj błędnego twierdzenia, że `sizeof` zwraca `int`.

Adresy wypisuj przez `%p`, z argumentem typu `void *` (dla wskaźników do obiektów stosuj rzutowanie `(void *)`). Nie drukuj adresów przez `%d`, `%ld` ani `%llu`. Faktyczne adresy mogą się zmieniać między uruchomieniami; numeracja na rysunkach jest schematyczna.

## 4. Struktura docelowego notebooka

| Sekcja | Tytuł roboczy | Konieczna treść |
|---|---|---|
| W6.1 | Gdzie mieszkają zmienne? | Bajty, adresy, typ, rozmiar; ilustracja pamięci; `sizeof`. Krótkie nawiązanie do W2. |
| W6.2 | Jak poznać adres? | Operator `&`, `%p`, nawiązanie do `scanf` z W3. |
| W6.3 | Czym jest wskaźnik? | Deklaracja i poprawna inicjalizacja `int *p = &a`, osobny obiekt wskaźnika, `&p`, rozmiary. |
| W6.4 | Co kryje się pod adresem? | Dereferencja `*p`; rozróżnienie `p`, `*p`, `&p`, `&a`. |
| W6.5 | Czy wskaźnik może zmienić wartość? | Przepięcie `p` między `a` i `b`, odczyt, `*p = ...`, aliasowanie. |
| W6.6 | Czy wskaźnik też ma adres? | `int **pp = &p`, `*pp`, `**pp`, bez rozwijania wielokrotnie zagnieżdżonych deklaracji. |
| W6.7 | Kiedy wskaźnik jest niebezpieczny? | `NULL`, inicjalizacja, dereferencja, zakres i czas życia; nie uruchamiaj niebezpiecznych przykładów jako zwykłych komórek. |
| W6.8 | Co przekazujemy funkcji? | Kontrast `void f(int a)` i `void f(int *a)`, argument zawsze kopiowany; powrót do W4 i `scanf`. |
| W6.9 | Jak uzyskać więcej niż jeden wynik? | Parametry wyjściowe, poprawna funkcja z dwoma wynikami, `swap(&a, &b)`; omówienie operatora przecinka w błędnie rozumianym `return x, y`. |
| W6.10 | Co oznacza `p + 1`? | Arytmetyka na wskaźnikach do **pojedynczych obiektów**, bez prezentacji tablic; `char *`, `int *`, `double *`; różnice adresów w bajtach. |
| W6.11 | Po co `void *`? | Ogólny wskaźnik do obiektu, rzutowanie do właściwego typu przed dereferencją, brak standardowej arytmetyki `void *`. |
| W6.12 | Czy w `double` zmieszczą się dwa `int`? | **Zachować eksperyment** z historycznego notebooka; omówić bajty, rozmiary, interpretację, zagrożenia i poprawny wariant `memcpy`. |
| W6.13 | Sprawdź, co rozumiesz | Krótkie przewidywania wyniku i zmian stanu pamięci, jedno samodzielne zadanie z funkcją/wskaźnikiem, podsumowanie. |

Tytuł sugerowany: **„Wykład 6 — Gdzie mieszkają zmienne? Adresy, wskaźniki i pamięć”**.

## 5. Wiążące decyzje o trudniejszych przykładach

### 5.1. Arytmetyka wskaźników — wyłącznie pojedyncze obiekty

Nie wprowadzaj tablic tylko po to, aby pokazać `p + 1`. Przykład wzorcowy:

```c
#include <stdio.h>

int main(void)
{
    int a = 10;
    int *p = &a;

    printf("p     = %p\n", (void *)p);
    printf("p + 1 = %p\n", (void *)(p + 1));
    return 0;
}
```

Arytmetyka `p + 1` dla wskaźnika do pojedynczego obiektu jest w C dozwolona: można wytworzyć wskaźnik **jeden za obiektem**, lecz **nie wolno go dereferencjonować**. Pokazuj analogicznie `char` i `double`. Zinterpretuj wyniki jako przemieszczenie o 1, 4 i 8 **bajtów**, odpowiednio 8, 32 i 64 **bity adresowanej pamięci** na omawianej platformie. Nie odejmuj liczbowo niespokrewnionych wskaźników ani nie twórz wskaźników z arbitralnych liczb typu `(int *)5` jako modelu poprawnej arytmetyki. Nie wymagaj identycznych, absolutnych adresów w testach.

### 5.2. Dwa `int` w jednym `double` — przykład obowiązkowy

Użytkownik **wyraźnie zdecydował o zachowaniu** przykładu: ma on pokazać, że 8 B `double` i 2 × 4 B `int` odpowiadają tej samej wielkości pamięci oraz że typ określa interpretację bajtów. Nie usuwaj, nie ukrywaj i nie zastępuj go samym ogólnym ostrzeżeniem.

Jednocześnie zachowaj rozróżnienie modelu pamięci od wymagań języka C:
- historyczny zapis przez `int *p = (int *)&d; *p = ...; *(p+1) = ...` nie jest poprawnym przenośnym sposobem używania obiektu `double`; narusza ograniczenia aliasingu/dostępu do obiektów, a `p+1` nie jest uprawnieniem do traktowania `double` jak tablicy dwóch `int`;
- takiego kodu **nie wykonuj jako zwykłej poprawnej komórki** i nie opieraj oczekiwanego wyniku na działaniu niezdefiniowanym;
- zachowaj historyczną ideę w **wyraźnie oznaczonym eksperymencie koncepcyjnym** (schemat, ewentualnie nieuruchamiany fragment historyczny) i zbuduj obok **działającą demonstrację zgodną z C11** za pomocą `unsigned char`/`memcpy`, która umieszcza dwa obiekty typu `int` w ośmiobajtowym buforze reprezentacji, a następnie kopiuje te bajty do obiektu `double` lub pokazuje ich reprezentację; użyj `sizeof` i jawnie sprawdź warunek rozmiaru. Nie zakładaj konkretnej liczbowej wartości wynikowego `double` ani konkretnego endianu.
- Dodatkowo można pokazać `memcpy` w odwrotnym kierunku. Cel dydaktyczny: wielkość pamięci ≠ znaczenie zawartości. Wskaż różnicę między interpretacją reprezentacji a wykonywaniem nielegalnej operacji na obiekcie.

Nie rozszerzaj tego o kompletny wykład o strict aliasing, IEEE 754 ani standardowe reguły effective type.

### 5.3. `void *`, wskaźniki wielopoziomowe i bezpieczeństwo

Pokaż proste `void *p = &a` i `*(int *)p`. Nie ucz arytmetyki na `void *` jako standardowego C (GCC może ją udostępniać jako rozszerzenie). `int **` ma służyć wyjaśnieniu, że wskaźnik jest samodzielnym obiektem, nie komplikowaniu składni. Nie pokazuj dereferencji `NULL`, adresów liczbowych, przekroczenia zakresu ani obiektu po zakończeniu czasu życia jako uruchamianego eksperymentu.

### 5.4. Funkcje i `scanf`

Przykłady z `fun(int)`, `fun(int *)`, `swap` i dwoma parametrami wyjściowymi mają być logicznie połączone: w C przekazanie `&a` oznacza przekazanie **wartości wskaźnika**, dzięki czemu funkcja dociera do oryginalnego obiektu; nie nazywaj tego osobnym mechanizmem „przekazywania przez referencję” w C. Zwróć uwagę, że `return x, y;` nie zwraca dwóch wartości, lecz wynik prawego operandu operatora przecinka.

## 6. Ilustracje i materiały historyczne

W `lec6.tex` znajdują się liczne diagramy TikZ pokazujące bajty pamięci, adresy, wartości zmiennych oraz strzałki wskaźników. **Można i należy je modernizować**, jeżeli poprawia to czytelność lub spójność; nie trzeba konserwować nieczytelnych detali oryginału.

Wymagany wspólny język wizualny:
- schematyczne, podpisane adresy;
- oddzielne oznaczenie obiektu i wskaźnika;
- wyraźne rozróżnienie zawartości wskaźnika od adresu samego wskaźnika;
- pokazanie zmiany `p = &b` osobno od `*p = ...`;
- jeden diagram 8-bajtowej komórki `double` kontra dwie 4-bajtowe reprezentacje `int`;
- zmiana barwy lub obramowania obiektu przy modyfikacji, spójna legenda i czytelne podpisy po polsku.

Weryfikuj ścieżki zasobów. Nie zostawiaj w docelowym notebooku niedostępnych linków do screenshotów, pustych komórek, artefaktów wyjścia ani obrazów niezwiązanych z narracją. Jeśli grafiki wymagają osobnych plików, przechowuj wyłącznie zasoby potrzebne do wyświetlenia wykładu.

## 7. Etapy wykonawcze i bramki

| Etap | Zadanie | Warunek ukończenia |
|---|---|---|
| W6-INT.1 | Inwentaryzacja `lec6.tex`, starego notebooka, programów `samples`; krótka mapa pokrycia | Każdy ważny element ma decyzję „zachować/przebudować/świadomie pominąć” i powód. |
| W6-INT.2 | Szkielet `Wykład 6.ipynb`, narracja, granice zakresu | Sekcje W6.1–W6.13 spójne i niezależne od historycznych źródeł. |
| W6-INT.3 | Pamięć, adresy i deklaracje (W6.1–W6.3) | Działające C11, spójne grafiki, pytania kontrolne. |
| W6-INT.4 | Dereferencja, przepinanie, `int **` (W6.4–W6.6) | Widoczna różnica między adresem, wskaźnikiem i wskazywaną wartością. |
| W6-INT.5 | Bezpieczeństwo wskaźników (W6.7) | Żadnego niezamierzonego UB w wykonywanych komórkach. |
| W6-INT.6 | Wskaźniki i funkcje (W6.8–W6.9) | Poprawne `swap`, parametry wyjściowe, zrozumiała semantyka przekazywania przez wartość. |
| W6-INT.7 | Arytmetyka, `void *`, dwa `int` w `double`, podsumowanie (W6.10–W6.13) | Bez tablic, z eksperymentem pamięciowym, działającym `memcpy`, bez niedozwolonej dereferencji. |
| W6-INT.8 | Audyt merytoryczny, techniczny, dydaktyczny, wizualny | Spełnione kontrole z §8, udokumentowane odstępstwa. |
| W6-INT.9 | Przegląd i przygotowanie do publikacji | Lista dokładnie tych plików, które muszą trafić do `master`; bez merge i bez publikacji bez decyzji użytkownika. |

Kontroluj ukończenie każdego etapu przed następnym; popraw niedociągnięcia w ramach etapu zamiast mnożyć pliki robocze i poboczne zadania. Nie odtwarzaj niepotrzebnej dokumentacji modernizacyjnej w `README.md`.

## 8. Odbiór techniczny i dydaktyczny

**Kod:**
- notebook jest prawidłowym JSON `ipynb`, ma kernel C, nie zawiera pustych wykonywalnych komórek, przypadkowych wyników z poprzednich uruchomień ani niepotrzebnych metadanych;
- wszystkie przewidziane do uruchamiania przykłady kompilują się jako C11 pod GCC z `-Wall -Wextra -Wpedantic` i pracują poprawnie w `-O0` i `-O2`;
- dla stosownych przykładów wykonaj kontrole AddressSanitizer/UndefinedBehaviorSanitizer; nie sugeruj, że sanitizery wykrywają wszystkie błędy;
- uruchom właściwe komórki również w docelowym kernelu Jupyter C, jeśli środowisko jest dostępne; w przeciwnym razie jasno odnotuj, że wykonano tylko kompilację zewnętrzną;
- nie zależ od sztywnych adresów, konkretnego ASLR, kolejności bajtów ani przypadkowego wyniku UB; nie pozostawiaj niezgodnych specyfikatorów `printf`.

**Dydaktyka:**
- każda sekcja wprowadza tylko niezbędne nowe pojęcia i utrwala je eksperymentem;
- pytania „przewidź–uruchom–zmień” mają jednoznaczne kryteria odpowiedzi;
- przykład dwóch `int` i `double` jest zachowany oraz technicznie uczciwie objaśniony;
- arytmetyka wskaźników jest pokazana bez tablic i bez czytania za pojedynczym obiektem;
- grafiki przedstawiają to samo co kod; nie wywołuj zbyt wcześnie szczegółowych koncepcji W7;
- krótka mapa pokrycia porównuje nowy notebook z angielskim notebookiem i `lec6.tex`. Udokumentuj świadome pominięcia, bez wymagania kopiowania błędnych przykładów.

**Raport końcowy agenta:** podaj aktualną gałąź i SHA, wykaz zmienionych plików, listę etapów PASS/FAIL, zakres testów (w tym czego nie uruchomiono), znane ograniczenia oraz instrukcję ręcznej kontroli dla prowadzącego. Nie ogłaszaj ukończenia, jeśli któraś obowiązkowa bramka nie została zaliczona; zamiast tego wskaż konkretny problem i napraw go w granicach zakresu.

## 9. Bezwzględne ograniczenia dla autonomicznego wykonawcy

- **Nie usuwaj historycznego przykładu** z dwoma `int` w `double`; zmodernizuj go w bezpieczny i poznawczo użyteczny sposób.
- **Nie wprowadzaj tablic ani wyprzedzającego wykładu W7** do demonstracji `p + 1`.
- **Nie rozbudowuj dygresji o `size_t`**, różne ABI i niestandardowe platformy.
- **Nie traktuj poprawnego rzutowania typu jako gwarancji poprawności adresu czy dereferencji.**
- **Nie przenoś instrukcji agentowych/testów i zapisków roboczych do finalnego notebooka lub README.**
- **Nie publikuj wyników na `master` bez zgody użytkownika** po wykonaniu modernizacji.
- Nie wykonuj działań wykraczających poza modernizację W6 pod pretekstem „usprawnienia repozytorium”.

---

**Punkt końcowy:** student ma potrafić prześledzić stan pamięci po każdej instrukcji, poprawnie korzystać z prostych wskaźników i przekazywać adresy do funkcji — a jednocześnie rozumieć, dlaczego eksperyment z dwoma `int` w obszarze rozmiaru `double` dobrze pokazuje reprezentację pamięci, lecz nie jest wzorcem bezpiecznego pisania kodu C.
