#include <stdio.h>

int main(void)
{
    int liczba = printf("ABC\n");
    if (liczba < 0) {
        fprintf(stderr, "Blad zapisu na stdout.\n");
        return 1;
    }
    printf("Pierwszy printf zapisal %d znaki.\n", liczba);
    fprintf(stderr, "To jest komunikat na stderr.\n");
    return 0;
}
