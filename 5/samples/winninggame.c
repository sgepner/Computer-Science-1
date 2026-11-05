#include <stdio.h>

int main()
{
    while(1)
    {  
        int uv = 0;
        printf("Give me a value that is not greater than 10\n");
        scanf("%d", &uv);
        int aiv = uv + 1;
        if(uv > 10)
        {
            printf("You cheat, I win!!\n");
            break;
        }
        printf("My is greater I win!!\n");
        printf("%d %d\n", uv, aiv);
    }
}
