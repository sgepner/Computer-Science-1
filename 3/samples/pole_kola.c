#include <stdio.h>
#include <math.h>

int main(void)
{
    double promien;
    printf("Podaj promien kola: ");
    fflush(stdout);

    int wynik = scanf("%lf", &promien);
    if (wynik != 1) {
        if (wynik == EOF) {
            fprintf(stderr, "Blad: brak danych (EOF).\n");
        } else {
            fprintf(stderr, "Blad: oczekiwano liczby.\n");
        }
        return 1;
    }
    if (!isfinite(promien) || promien <= 0.0) {
        fprintf(stderr, "Blad: promien musi byc dodatni i skonczony.\n");
        return 1;
    }

    double pi = acos(-1.0);
    double obwod = 2.0 * pi * promien;
    double pole = pi * promien * promien;
    if (!isfinite(obwod) || !isfinite(pole)) {
        fprintf(stderr, "Blad: wynik poza zakresem.\n");
        return 1;
    }

    printf("Promien: %.2f\n", promien);
    printf("Obwod: %.2f\n", obwod);
    printf("Pole: %.2f\n", pole);
    return 0;
}
