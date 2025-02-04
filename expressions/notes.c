//Cairo Taylor, Expressions notes for C
#include <stdio.h>
#include <math.h> //this is what lets us use exponents
//Integers use Int to set variable and %d to print
//Floats use Float to set variable and %f to print
//Strings use Char to set variable and %s to print
int mynum;
float percent;
int add = 4+6;
int mul = 4*6;
float div = 6/4;
int mod = 6/4;
int ex = pow(5, 2);

int main(void){
   printf("Type a number: \n");
   scanf("%d", &mynum);
   printf("Your number is %d \n", mynum);
   printf("Give me a percent as a decimal: \n");
   scanf("Your percent is %f", percent);
   printf("%d\n", add);
   printf("%d\n", mul);
   printf("%.2f\n", div);
   mul = 7*4;
   printf("%d\n", mod);
   printf("%d\n", ex);
   printf("%d\n", mul);
    return 0;
}