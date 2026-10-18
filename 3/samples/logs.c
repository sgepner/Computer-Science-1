#include <stdio.h>
#include <math.h>

int main(void)
{
    double x;
    printf("Podaj dodatnia liczbe: ");
    fflush(stdout);
    if (scanf("%lf", &x) != 1) {
        fprintf(stderr, "Blad: oczekiwano liczby.\n");
        return 1;
    }
    if (!isfinite(x) || x <= 0.0) {
        fprintf(stderr, "Blad: argument logarytmu musi byc dodatni i skonczony.\n");
        return 1;
    }
    printf("log(%.2f)=%.6f\n", x, log(x));
    printf("log10(%.2f)=%.6f\n", x, log10(x));
    return 0;
}
