#include <stdio.h>

int main()
{
    int a=1;
    int b=1;
    printf("Enter a number to print to (n):\n");
    scanf("%d", &a);

    // printf("%d ", b);
    for (int i=1; i <= a; i++)
    {
        b = i;
        for (int j=1; j<i; j++)
        {
            b = i + (b * 10);
        }
        printf("%d \n", b);
    }
}