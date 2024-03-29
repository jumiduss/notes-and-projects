#include <stdio.h>

int main()
{
    // Section 6
    // printf("  *\n");
    // printf(" ***\n");
    // printf("*****\n");

    // Section 7
    // printf("%d",3+5);
    // return 0;

    // Section 8
    // printf("%d\n",2021-30);

    // Section 9
    // // Part 1
    // int num;
    // num = 10;
    // scanf("%d", &num);
    // printf("num is %d \n", num);
    // return 0;

    // // Part 2
    // float height;
    // float width;

    // printf("Enter your rectangle's height:\n");
    // scanf("%f", &height);

    // printf("Enter your rectangle's width:\n");
    // scanf("%f", &width);

    // printf("The perimeter of your rectangle is: %f", (height*2)+(width*2));

    // // Part 3 
    // int num1=5, num2=2;
    // double result;
    // result = num1 / num2;
    // printf("%lf\n",result); 

    // // Part 4
    // int a,b,c;
    // printf("Enter your first grade:\n");
    // scanf("%d",&a);
    // printf("\nEnter your second grade:\n");
    // scanf("%d",&b);
    // printf("\nEnter your third grade:\n");
    // scanf("%d",&c);
    // double average = (a + b + (double)c) / 3;
    // printf("\nYour exact grade point average is: %lf\n", average);

    // // Part 5
    // double user_temp, fahrenheit;
    // printf("Enter your temperature in celcius:\n");
    // scanf("%lf",&user_temp);
    // fahrenheit = (user_temp*1.8) + 32;
    // printf("Your temp is: %lf", fahrenheit);

    // // Part 6
    // double a=10,b=20,temp;
    // printf("Before a = %lf\n",a);
    // printf("Before b = %lf\n",b);

    // temp = a;
    // a = b;
    // b = temp;

    // printf("After a = %lf\n",a);
    // printf("After b = %lf\n",b);

    // Section 10
    // // Part 1
    // int a_1,n,d;

    // printf("With the arithmatic sequence: a_n = a_1 + (n-1) * d):\n");

    // printf("Give the first term of the series (a_1)\n");
    // scanf("%d",&a_1);

    // printf("Give the integer value to return (n)\n");
    // scanf("%d", &n);

    // printf("Give the step of the sequence (d)\n");
    // scanf("%d", &d);

    // int a_n = a_1 + ( (n - 1) * d );

    // printf("Your value of a_n is: %d\n", a_n);

    // // Part 2
    // int a_1, a_n, n;
    // double solution;
    // printf("With the sum of an arithmatic sequence: s_n = (a_1 + a_n) * (n / 2):\n");

    // printf("Give the value of the first term in the series (a_1)\n");
    // scanf("%d", &a_1);

    // printf("Give the value of the last term in the series (a_n)\n");
    // scanf("%d", &a_n);

    // printf("Give the index of the term to return (n)\n");
    // scanf("%d", &n);

    // solution = (a_1 + a_n) * (n / 2.0);

    // printf("The sum of the arithmatic sequence is: %lf\n", solution);
    
    // Part 3
    double wage,hours,salary;
    
    printf("Provide your hourly wage:\n");
    scanf("%lf", &wage);

    printf("Provide the number of hours worked:\n");
    scanf("%lf",&hours);

    salary = wage * hours;
    printf("Your monthly salary is: %lf \n",salary);
    
    return 0;
}
