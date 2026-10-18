#include <stdio.h>

int main(void)
{
    int a;
    double b;

    printf("Podaj liczbe calkowita i rzeczywista (np. 7 2.5): ");
    fflush(stdout);
    int wynik = scanf("%d %lf", &a, &b);
    if (wynik != 2) {
        if (wynik == EOF) {
            fprintf(stderr, "Blad: koniec wejscia przed pierwszym polem (EOF).\n");
        } else {
            fprintf(stderr, "Blad: przypisano tylko %d z 2 pol.\n", wynik);
        }
        return 1;
    }

    printf("a=%d, b=%.2f\n", a, b);
    return 0;
}
