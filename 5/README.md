# Wykład 5 — pętle i powtarzanie instrukcji

Aktualny materiał: [Wykład 5.ipynb](Wyk%C5%82ad%205.ipynb), po polsku, kernel **C** (`c`). Wykład prowadzi od jednorazowej decyzji z W4 przez `while`, `do…while`, `for`, granice i zasięg do pętli zagnieżdżonych, `break`/`continue` oraz zastosowań. Każdy eksperyment zaczynamy od przewidzenia wyniku. Ćwiczenia dodatkowe i liczby pierwsze są wydzielone od głównej narracji.

Komórki są osobnymi pełnymi programami C11, bez interaktywnego wejścia i zapisanych wyników. Jeśli kernel C nie jest dostępny, skopiuj komórkę do pliku `.c` i uruchom GCC. Dla matematyki dodaj `-lm` na końcu; komentarz `//%cflags:-lm` służy kernelowi C. W tym środowisku istnieje specyfikacja `c`, ale brakuje modułu `jupyter_c_kernel`; wykonanie Jupyter pozostaje do sprawdzenia na komputerze wykładowym. Testy GCC działają niezależnie od niego.

Grafiki są lokalne, w tym komiks XKCD #292 autorstwa Randalla Munroe. Animacja Fouriera ma statyczną ilustrację, więc sens przykładu nie wymaga autoplay ani internetu. Program używa N **wyrazów nieparzystych**, okresu 2L i L=1; animacja służy porównaniu jakościowemu, nie odczytywaniu wartości z programu.

## Regresja

Z katalogu głównego repozytorium:

```bash
python3 5/check_w5.py
```

Wymagania: Python 3 (biblioteka standardowa), GCC i libm. Testy wykonują po 18 programów notebooka, 12 wariantów brzegowych i 12 wejść konsolowych przy `-O0` i `-O2`, z `-std=c11 -Wall -Wextra -Werror -pedantic`. Sprawdzają stdout, stderr, statusy i zakończenie w 2 s, przewidywany wynik quizu, celowy błąd zasięgu oddzielnie oraz 45 wierszy liczbowych Fouriera przy dwóch skalach L (tolerancja bezwzględna 1e−12), nieparzystość i proste wartości analityczne. Kontrola struktury obejmuje 9 sekcji, kernel, układ narracji i lokalne ilustracje. Wyniki zmiennoprzecinkowe wydrukowane w komórce Fouriera mają tolerancję 1e−6.

Pliki wykonywalne powstają w automatycznie sprzątanym katalogu tymczasowym. Dostępny kernel C jest sprawdzany osobno; brak modułu/specyfikacji jest jawnie zgłaszany jako ograniczenie opcjonalnego testu.

## Gra „I win!” — uruchom w terminalu

```bash
gcc -std=c11 -Wall -Wextra -Werror -pedantic 5/samples/gra_w5.c -o /tmp/w5_gra
/tmp/w5_gra
printf '0\n11\n' | /tmp/w5_gra
printf 'kot\n' | /tmp/w5_gra
/tmp/w5_gra < /dev/null
```

Program czyta całe wiersze i sprawdza zakres konwersji. Kończy po 5 turach, na liczbie większej niż 10 lub przy EOF. Błędne dane i za długi wiersz zwracają status 1; zwykłe zakończenie i EOF dają 0. Nie wklejaj go do komórki notebooka oczekującej deterministycznego wyniku. Parser `fgets`/`strtol` jest osłoną wejścia; szczegóły napisów poznamy później.

## Materiały do prowadzenia zajęć

Głównym materiałem jest polski notebook `Wykład 5.ipynb`. Diagramy i animacja działają z lokalnych plików. Do demonstracji wejścia z klawiatury używaj `samples/gra_w5.c`; pozostałe przykłady podczas wykładu uruchamiaj z notebooka. Sam notebook zawiera kompletną ścieżkę pojęciową i nie wymaga znajomości poprzednich wersji tego wykładu.

Kolejność i dobór eksperymentów wynikają z przepływu narracji, nie z przypisanego czasu. Dodatkowe ćwiczenia można wykorzystać zależnie od potrzeb grupy.
