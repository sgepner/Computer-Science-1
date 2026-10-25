# W2 — materiały pomocnicze (wersja robocza)

Materiały do samodzielnego powtórzenia reprezentacji liczb. Uzupełniają [Wykład 2](../Wyk%C5%82ad%202.ipynb), ale nie zastępują wykładu ani nie są zadaniem na ocenę.

| Plik | Zawartość |
|:-----|:----------|
| [Notebook: Od liczby dziesiętnej do bitów](W2_Pomocniczy_Konwersje_Bity_IEEE754.ipynb) | Zapisy pozycyjne, liczby całkowite i ułamki, dzielenie i mnożenie przez 2, rozwinięcie 0.1, porównanie 0.123687 oraz 1.123687, normalizacja IEEE 754 i U2. |
| [Ściąga A4 (PDF)](W2_Sciaga_A4_System_Dwojkowy_IEEE754.pdf) | Jednostronicowy schemat tych samych konwersji, do wydruku lub zamieszczenia w Teams. |

**Jak korzystać z notebooka:** przeczytaj przykład, spróbuj go samodzielnie przeliczyć i dopiero potem sprawdź wynik. Komórki wykonawcze są w **C11**, zgodne z kernelem C używanym na przedmiocie. Pętle w pomocniczych programach można na razie traktować jak gotowy kalkulator — ich składnię poznamy w kolejnym wykładzie.

**Ważna intuicja:** jedynka będąca częścią całkowitą liczby w zwykłym zapisie binarnym nie jest tym samym, co *ukryta jedynka* znormalizowanej liczby IEEE 754. Dla liczb podnormalnych (pole wykładnika E = 0) ukrytej jedynki **nie ma**, niezależnie od tego, czy część ułamkowa F jest zerowa.

**Weryfikacja robocza:** notebook poprawny strukturalnie (14 komórek, w tym 3 C); programy skompilowane i uruchomione przy GCC C11 z `-O0` i `-O2` (6/6 PASS). PDF zweryfikowany jako jedna strona A4. Materiały mogą być jeszcze poprawiane po uwagach studentów.

**Zakres:** pliki robocze uzupełniające W2. Główny notebook wykładowy i materiały historyczne nie są zmieniane przy ich dodawaniu.
