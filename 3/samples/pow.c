#include <stdio.h>
#include <math.h>

int main(void)
{
    double podstawa;
    printf("Podaj nieujemna podstawe potegi: ");
    fflush(stdout);
    if (scanf("%lf", &podstawa) != 1) {
        fprintf(stderr, "Blad: oczekiwano liczby.\n");
        return 1;
    }
    if (!isfinite(podstawa) || podstawa < 0.0) {
        fprintf(stderr, "Blad: podstawa musi byc nieujemna i skonczona.\n");
        return 1;
    }
    double kwadrat = pow(podstawa, 2.0);
    double potega = pow(podstawa, 2.31);
    if (!isfinite(kwadrat) || !isfinite(potega)) {
        fprintf(stderr, "Blad: wynik poza zakresem.\n");
        return 1;
    }
    printf("x^2=%.3f, pow(x,2.31)=%.3f\n", kwadrat, potega);
    return 0;
}
