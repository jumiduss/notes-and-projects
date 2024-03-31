#include <stdio.h>

int main()
{
    char a;
    double temp;
    int out=0;

    //    0.0     0.0    0.0   0.0
    //  128.64   32.16   8.4   2.1/0
    printf("Give a character to convert to binary:\n");
    scanf("%c", &a);

    temp = a;

    if ((temp - 128) > 0)
    {
        out += 10000000;
        temp -= 128;
    }
    if ((temp - 64) > 0)
    {
        out += 1000000;
        temp -= 64; 
    }
    if ((temp - 32) > 0)
    {
        out += 100000;
        temp -= 32;
    }
    if ((temp - 16) > 0)
    {
        out += 10000;
        temp -= 16;
    }

    if ((temp - 8) > 0)
    {
        out += 1000;
        temp -= 8; 
    }
    if ((temp - 4) > 0)
    {
        out += 100;
        temp -= 4; 
    }
    if ((temp - 2) > 0)
    {
        out += 10;
        temp -= 2; 
    }
    if ((temp - 1) == 0)
    {
        out += 1;
    }

    printf("You character is, %d", out);

    return 0;
}