#include <stdio.h>

int main(void)
{
    int liczba;
    double x;
    printf("Podaj int oraz double (np. 7 2.5): ");
    fflush(stdout); /* pokaz pytanie przed oczekiwaniem na dane */

    int wynik = scanf("%d %lf", &liczba, &x);
    printf("scanf zwrocil %d\n", wynik);

    if (wynik == EOF) {
        printf("Koniec wejscia (EOF).\n");
        return 1;
    }
    if (wynik >= 1) {
        printf("Pierwsze pole: %d\n", liczba);
    }
    if (wynik == 2) {
        printf("Drugie pole: %.2f\n", x);
        return 0;
    }
    printf("Nie udalo sie przypisac dwoch pol.\n");
    return 1;
}
