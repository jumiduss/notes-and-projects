#include <stdio.h>

// Find the most efficient way to get the min max of three numbers

int main()
{
    int a=10,b=11,c=12,biggest,middle,smallest;
    // // My Solution
    // if (a>b)
    // {
    //     if (a>c)
    //     {
    //         biggest = a;
    //         if (b>c)
    //         {
    //             middle = b;
    //             smallest = c;
    //         }
    //         else
    //         {
    //             middle = c;
    //             smallest = b;
    //         }
    //     }
    //     else
    //     {
    //         biggest = c;
    //         middle = a;
    //         smallest = b;
    //     }
    // }
    // else
    //     if (b>c)
    //     {
    //         biggest = b;
    //         if (a>c)
    //         {
    //             middle = a;
    //             smallest = c;
    //         }
    //         else
    //         {
    //             middle = c;
    //             smallest = a;
    //         }
    //     }
    //     else
    //         biggest = c;
    //         middle = b;
    //         smallest = a;

    // Instructor Solution
    biggest = a;
    smallest = b;
    if (a < b)
    {
        biggest = b;
        smallest = a;
    }
    if (c < smallest)
    {
        middle = smallest;
        smallest=c;
    }
    if (c > biggest)
    {
        middle = biggest;
        biggest = c;
    }
    printf("biggest = %d \nmiddle = %d \nsmallest = %d\n", biggest,middle,smallest);
}