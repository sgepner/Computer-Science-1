/* W5: terminal only. Whole-line validation is support code for the loop lesson. */
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <limits.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    for (int tura = 0; tura < 5; ++tura) {
        char wiersz[128];
        puts("Give me a value that is not greater than 10");
        if (fgets(wiersz, sizeof wiersz, stdin) == NULL) {
            if (ferror(stdin)) { fputs("Blad odczytu\n", stderr); return 1; }
            puts("Koniec wejscia");
            return 0;
        }
        if (strchr(wiersz, '\n') == NULL && !feof(stdin)) {
            fputs("Za dlugi wiersz\n", stderr);
            return 1;
        }
        errno = 0;
        char *koniec;
        long liczba = strtol(wiersz, &koniec, 10);
        if (koniec == wiersz || errno == ERANGE || liczba < INT_MIN || liczba > INT_MAX) {
            fputs("Blad danych\n", stderr);
            return 1;
        }
        while (isspace((unsigned char)*koniec)) { ++koniec; }
        if (*koniec != '\0') { fputs("Blad danych\n", stderr); return 1; }
        int uv = (int)liczba;
        if (uv > 10) { puts("You cheat, I win!!"); return 0; }
        puts("My is greater I win!!");
        printf("%d %d\n", uv, uv + 1);
    }
    puts("Koniec 5 tur");
    return 0;
}
