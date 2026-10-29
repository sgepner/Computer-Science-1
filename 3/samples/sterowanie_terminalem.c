#include <stdio.h>

int main(void)
{
    printf("ABCDE\rZ\n");   /* powrot na poczatek wiersza */
    printf("ABCDE\b!\n");  /* cofniecie o jedna pozycje */
    printf("A\vB\n");      /* tabulator pionowy */
    printf("apostrof: %c\n", '\'');
    return 0;
}
