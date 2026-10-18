#include <stdio.h>
#include <math.h>

int main(void)
{
    double kat;
    printf("Podaj kat w radianach: ");
    fflush(stdout);
    if (scanf("%lf", &kat) != 1) {
        fprintf(stderr, "Blad: oczekiwano liczby.\n");
        return 1;
    }
    if (!isfinite(kat)) {
        fprintf(stderr, "Blad: kat musi byc skonczony.\n");
        return 1;
    }
    printf("sin(%.2f)=%.6f\n", kat, sin(kat));
    printf("cos(%.2f)=%.6f\n", kat, cos(kat));
    return 0;
}
