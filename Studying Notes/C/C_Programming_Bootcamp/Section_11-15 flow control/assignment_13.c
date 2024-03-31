#include <stdio.h>

int main()
{
    int a,b,c;
    // Part 1
    printf("Give first int\n");
    scanf("%d", &a);
    printf("Give second int:\n");
    scanf("%d", &b);
    // Part 2
    printf("Give third int:\n");
    scanf("%d", &c);

    if (a==b && b==c)
        printf("EQUAL\n");
    else 
        printf("NOT EQUAL\n");
    
    // Part 3
    int d,p1,p2,p3;
    printf("Give 3 digit number:\n");
    scanf("%d",&d);
    p1 = d%10;
    p2 = (d / 10) % 10;
    p3 = (d / 100) % 10;

    if (p1 > p2 && p2 > p3)
        printf("ASCENDING");
    else
        printf("NOT ASCENDING");

    // Part 4
    int num;
    printf("Give a number:\n");
    scanf("%d", &num);
    if (num > 0)
        printf("1");

    else if (num < 0)
        printf("-1");
    
    else
        printf("0");

    return 0;
}