# W6 — stan realizacji (wyłącznie gałąź robocza)

Kontrakt: [W6_MODERNIZATION_PLAN.md](../W6_MODERNIZATION_PLAN.md).
Tryb: execution-control continuous; bramki test-review-advance. **COMPLETE**: W6-INT.1–9 VERIFIED PASS.
Zakres: W6-INT.1–W6-INT.9, bez publikacji, push i merge.
Gałąź: `codex/w6-modernizacja`; baza po fetch: `95f4bc5c241d9032f0f686abc12ec732bb55a6bc`.
Ostatnia faktycznie przetestowana rewizja: `acb6a972b824b3601bd7e4c5c32cc3ca473bdbba`.
Bieżący HEAD: `git rev-parse HEAD`; commit zamykający zmienia wyłącznie raport i dowody.
Aktualne zmiany: `git status --short`; brak otwartego checkpointu lub blokady.
Źródła historyczne pozostają bez zmian. Zastane pliki nieśledzone nie należą do kampanii.

| Etap | Stan | Dowód / następna czynność |
|---|---|---|
| W6-INT.1 | VERIFIED PASS | Mapa pokrycia poniżej; doc_clerk + koordynator + niezależny independent_reviewer: PASS |
| W6-INT.2 | VERIFIED PASS | nbformat.validate; 13 uporządkowanych sekcji, spójna narracja i granice; kontrola koordynatora |
| W6-INT.3 | VERIFIED PASS | 3 programy × O0/O2/ASan+UBSan i kernel C; diagramy 2 PNG, nbformat; niezależna recenzja treści i grafik PASS; results/report-through-3.json |
| W6-INT.4 | VERIFIED PASS | 6 programów łącznie × 3 tryby i kernel C, 18 kontroli semantyki, diagramy aliasowania i int ** sprawdzone; niezależny recenzent PASS; report-through-6.json |
| W6-INT.5 | VERIFIED PASS | 7 programów łącznie × 3 tryby i kernel C; 21 kontroli wyników; błędne fragmenty wyłącznie Markdown; report-through-7.json |
| W6-INT.6 | VERIFIED PASS | 10 programów łącznie × 3 tryby i kernel C; 30 kontroli wyników; parametry wyjściowe, kopia wskaźnika i swap zgodne; niezależna recenzja W6.7–9 PASS; report-through-9.json |
| W6-INT.7 | VERIFIED PASS | 13 programów × O0/O2/ASan+UBSan i kernel C; 39 asercji semantycznych; diagram memcpy sprawdzony; report-through-13.json |
| W6-INT.8 | VERIFIED PASS | Niezależny reviewer: PASS bez usterek; 39 uruchomień GCC + 13 komórek kernela, regresje, render 13 sekcji/5 grafik; review.json |
| W6-INT.9 | VERIFIED PASS | Lista publikacyjna: wyłącznie notebook; źródła zachowane, lokalny commit i instrukcja odbioru; bez push/merge |

## Weryfikacja

Kod: GCC C11 `-Wall -Wextra -Wpedantic`, `-O0` i `-O2`, ASan/UBSan;
struktura: nbformat, kernel C, brak wyjść i pustych komórek;
Jupyter: istniejący `/home/sgepner/Virtualenv/jupyter/bin/python` z jupyter_c_kernel;
przegląd niezależny: independent_reviewer, inny niż wykonawca notebooka.
Wyniki i komendy zostaną uzupełnione po faktycznym wykonaniu.

## Mapa pokrycia — W6-INT.1

Źródła: `../lec6.tex`, `../Lecture 6 examples.ipynb`, wszystkie 13 plików C `../samples/`.
Porównano narrację W1–W5 oraz granice W7. Numery komórek starego notebooka od zera.

| Element historyczny | Decyzja i miejsce docelowe | Powód |
|---|---|---|
| Pamięć, bajty, typ i sizeof (slajdy Memory; komórki 2, 5–6; addres.c) | Przebudować → W6.1, W6.3 | Poprawić formaty, zależność rozmiarów od platformy i błędny opis typu sizeof |
| Deklaracje, &, scanf, adres p (slajdy Pointers; komórki 4, 7–14, 25–28; addres2/3.c) | Przebudować → W6.2–W6.3, W6.6 | Inicjalizacja, %p z void *, osobny obiekt wskaźnika |
| Odczyt, przepięcie, zapis (komórki 15–24; addres5/6.c) | Zachować ideę, przebudować → W6.4–W6.5 | Rozdzielić p=&b od *p=…; pokazać aliasowanie |
| int ** i głębsze poziomy (komórki 12–14, 20, 27–28, 44) | Uprościć → W6.6 | Tylko int **, bez sztucznych adresów i mnożenia poziomów |
| Zagrożenia (addres2/4/8.c) | Zachować jako analizę → W6.7 | Nie wykonywać niezainicjalizowanych odczytów i dereferencji NULL |
| Funkcje (slajdy Revisiting functions; komórki 45–51; function.c, function1/2/3.c) | Przebudować → W6.8 | Kopiowanie wartości i kopiowanie wskaźnika; sumowanie można zastąpić krótszym przykładem |
| Zmienna globalna (komórki 48–49) | Świadomie pominąć | Zasięg był w W4; zbędne do pokazania parametrów wyjściowych |
| Wiele wyników (komórki 52–54; addres7.c, function4.c) | Przebudować → W6.9 + swap | Operator przecinka nie zwraca dwóch wartości; zachować ideę min/max |
| Arytmetyka (slajd Pointer arithmetic; komórki 29–34) | Przebudować → W6.10 | Pojedyncze obiekty, jeden za obiektem bez dereferencji; bez adresów liczbowych |
| void * (komórki 35–41) | Przebudować → W6.11 | Ogólny wskaźnik do obiektu; brak standardowej arytmetyki void * |
| Dwa int w double (komórki 42–43) | Obowiązkowo zachować ideę → W6.12 | Diagram 8 B vs 2×4 B i poprawna demonstracja memcpy; nie uruchamiać aliasingu |
| Układ procesu (komórka 3) | Świadomie pominąć | Wystarczy czas życia; pełny stos/sterta wykracza poza kontrakt |
| Komunikat OOM, puste komórki, screenshoty, zapowiedź testu | Pominąć / zastąpić spójnymi diagramami | Samodzielny polski materiał dla studentów |
| Tablice, sortowanie, pliki historycznego W7 | Nie włączać | Pozostają W7; W6.13 tylko ćwiczenia ze wskaźników i funkcji |

## Zespół

- `inventory`: doc_clerk (konfiguracja roli: gpt-6-luna, low), inwentaryzacja W6-INT.1, odczyt bez edycji; wynik sprawdzony przez koordynatora.

- `implementer`: code_engineer (konfiguracja roli: gpt-6.1-sol, medium), wyłączny wykonawca notebooka i jego ilustracji W6-INT.2–7.
- `reviewer`: independent_reviewer (konfiguracja roli: gpt-6.1-sol, medium), niezależny od wykonawcy; INT.1 PASS po porównaniu ze źródłami. Brak telemetrii pozwalającej potwierdzić model uruchomiony w backendzie.
- Koordynator: integracja, bramki, deterministyczne testy; nie zmienia kontraktu naukowego.

Decyzja W6.12: dozwolone kopiowanie reprezentacji nie oznacza poprawności liczbowego odczytu dowolnych bajtów jako double. Demonstracja nie odczytuje tak powstałego double jako liczby; pokazuje pojemność i odzyskanie reprezentacji int. Bufor bajtowy jest wyłącznie technicznym nośnikiem, bez lekcji tablic.

## Środowisko i ograniczenia testów

Linux x86-64, GCC 11.4.0; istniejące środowisko Jupyter: jupyter-c-kernel 1.2.2,
nbclient 0.10.4, nbformat 5.10.4. Uruchomienie zwykłego ASan z LeakSanitizer
w izolacji nie działało z powodu ptrace. Ten sam skrypt uruchomiono poza izolacją:
ASan/UBSan i kontrola wycieków pozostały włączone, wynik INT.3 PASS.
Kernel korzysta z istniejącego pakietu, ale lokalnego tymczasowego kernelspec
z jawną ścieżką interpretera. Nie zmieniono konfiguracji użytkownika.
Kernel C zgłasza błędy kompilacji również jako status ok: walidator sprawdza
więc także stderr i porównuje stdout z wykonaniem GCC.

## Polecenia odtworzenia bramek

Z katalogu repozytorium (testy wymagają lokalnego uruchomienia bez ograniczeń ptrace):

```bash
python3 6/w6_validation/verify.py --through 3 --kernel
python3 6/w6_validation/verify.py --through 6 --kernel
python3 6/w6_validation/verify.py --through 7 --kernel
python3 6/w6_validation/verify.py --through 9 --kernel
python3 6/w6_validation/verify.py --through 13 --kernel
```

Każda bramka sprawdza nbformat, kolejność sekcji, czyste komórki, zasoby,
kompilację z `-std=c11 -Wall -Wextra -Wpedantic -Werror`, wykonanie `-O0`,
`-O2`, `-O1 -fsanitize=address,undefined -fno-pie -no-pie`, zgodność stdout
po zastąpieniu zmiennych adresów oraz oczekiwane wyniki i relacje adresów.
`-fno-pie -no-pie` dotyczy wyłącznie samodzielnych binariów sanitizerów.
Wszystkie wyniki i dokładne polecenia GCC zawiera JSON odpowiedniej bramki.
Wyjścia testowe nigdy nie są zapisywane do notebooka studenckiego.

## Dodatkowa regresja funkcji

Wykonano `python3 6/w6_validation/regression.py`:
7 przypadków swap (odwrócona kolejność, równe i ujemne wartości, zera,
skrajne int platformy, ten sam obiekt, powrót po dwóch zamianach) oraz
6 przypadków sumy/różnicy, wszystkie w O0/O2/ASan+UBSan: PASS.
Dokładne wejścia, asercje, źródła testowe i polecenia: `results/regression.json`.
Testy respektują warunek braku przepełnienia oraz osobne obiekty wyjściowe.

## Kontrola ręczna prowadzącego po zakończeniu audytu

1. Otwórz `6/Wykład 6.ipynb` w Jupyter i wybierz kernel C. Wykonaj Restart & Run All.
   Każda komórka jest osobnym kompletnym programem; nie podawaj danych z klawiatury.
2. W W6.3–6 porównuj równość adresów i cele strzałek, a nie ich konkretne liczby.
   Prześledź a, b, p, q i pp po instrukcjach zaznaczonych na diagramach.
3. W W6.7 fragmenty w ramkach Markdown są wyłącznie analizą błędów. Nie kopiuj ich
   do wykonywalnych komórek jako części Run All.
4. W W6.8–9 wykonaj wskazane małe zmiany i przewidź wpływ na obiekt wywołującego.
5. W W6.10 sprawdź kroki w bajtach dla trzech typów. W W6.12 sprawdź zachowanie
   obu int po kopiowaniu, bez przewidywania wartości liczbowej double.
6. Oceń czytelność wszystkich diagramów przy typowej szerokości projektora i samodzielnie
   rozwiąż zadanie końcowe W6.13 przed sprawdzeniem kryteriów odpowiedzi.

## Audyt końcowy i zakres publikacji

W6-INT.8: niezależny recenzent sprawdził źródło całego notebooka, wszystkie 5 ilustracji,
poprawność pytań i odpowiedzi oraz skrypty i zapisane wyniki. PASS, bez usterek blokujących.
Recenzent nie implementował notebooka i nie powtarzał zestawu obliczeń; zweryfikował dowody.
Koordynator uruchomił faktyczne testy. Regresję odświeżono dla końcowego digestu notebooka,
dodając ćwiczenie memcpy z x=-3,y=42: PASS we wszystkich 3 trybach.
Render Chrome 153.0.8010.52 / nbconvert: 13 sekcji, 5 widocznych obrazów, brak poziomego
przepełnienia dokumentu; PNG są załącznikami notebooka i nie wymagają osobnych zasobów.
Testowano rzeczywiste relacje adresów i wartości, bez sztywnych adresów lub endianu.
Zgodność O0/O2 i sanitizery są dowodami wspierającymi; nie stanowią dowodu poprawności
wszystkich możliwych programów C. Nie wykonywano świadomie błędnych fragmentów Markdown.

**Jedyny plik do ewentualnego przeniesienia na master:** `6/Wykład 6.ipynb`.
Wszystko w `6/w6_validation/` jest materiałem roboczym wyłącznie tej gałęzi.
Historyczne źródła, inne wykłady, README i plan pozostają bez zmian.
Nie wykonano push, merge ani przeniesienia materiałów na master.
Kolejne działanie po zamknięciu kampanii: odbiór prowadzącego (~5–10 min) i ewentualne
osobne polecenie selektywnej publikacji samego notebooka, bez merge gałęzi.

## Zamknięcie kampanii — W6-INT.9

Tryb continuous: wszystkie dziewięć etapów VERIFIED PASS. Pozostałych autoryzowanych
checkpointów brak. Dalsza publikacja wymaga osobnego polecenia właściciela.
Commit implementacji: `acb6a972b824b3601bd7e4c5c32cc3ca473bdbba`, rodzic
`95f4bc5c241d9032f0f686abc12ec732bb55a6bc`; komunikat
`feat(W6): modernize pointers lecture as self-contained Polish notebook`.
Pełną bramkę powtórzono na dokładnie tym commicie: 13 programów × 3 tryby GCC,
13 wykonanych komórek kernela C, wszystkie semantyczne asercje PASS.
Końcowy digest notebooka: `9ddaa853670d8be7a96b5be920259cb923268d47f05a7cf0bda4435cca2064c9`.
Niezależny reviewer sprawdził odświeżone raporty; wcześniejsza uwaga o digestcie
regresji została zamknięta. Recenzja pozostaje PASS, bez powtarzania testów przez recenzenta.

Kontrola zakresu (`results/scope.json`): 297 istniejących plików śledzonych ma identyczne
SHA-256 jak przed modernizacją; lista 279 zastanych nieśledzonych plików poza kampanią
jest bez zmian. Nie deklarujemy czystego całego katalogu roboczego z tymi plikami użytkownika.
Lokalny master pozostaje na `95f4bc5c241d9032f0f686abc12ec732bb55a6bc`.
Notebook ma 61 komórek: 48 Markdown i 13 C; 5 PNG osadzonych jako attachments.
Nie wymaga zewnętrznych plików ani interaktywnego wejścia.

Zakres testów ograniczono do W6 i jego zasobów: innych wykładów nie zmieniono,
więc nie wykonywano ich regresji. Kontrola właściciela jest odbiorem dydaktycznym,
a nie brakującą obowiązkową bramką techniczną. Sanitizery nie dowodzą uniwersalnej
poprawności i nie uruchamiano fragmentów oznaczonych jako niebezpieczne.

### Dokładny wykaz nowych plików gałęzi

- `6/Wykład 6.ipynb`
- `6/w6_validation/.gitignore`
- `6/w6_validation/STATE.md`
- `6/w6_validation/baseline.json`
- `6/w6_validation/regression.py`
- `6/w6_validation/render.cjs`
- `6/w6_validation/render.py`
- `6/w6_validation/results/kernel.log`
- `6/w6_validation/results/regression.json`
- `6/w6_validation/results/render.json`
- `6/w6_validation/results/report-through-13.json`
- `6/w6_validation/results/report-through-3.json`
- `6/w6_validation/results/report-through-6.json`
- `6/w6_validation/results/report-through-7.json`
- `6/w6_validation/results/report-through-9.json`
- `6/w6_validation/results/review.json`
- `6/w6_validation/results/scope.json`
- `6/w6_validation/verify.py`
