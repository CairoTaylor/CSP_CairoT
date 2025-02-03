//Cairo Taylor, Expressions notes for C
#include <stdio.h>
//Integers use Int to set variable and %d to print
//Floats use Float to set variable and %f to print
//Strings use Char to set variable and %s to print
int mynum;
float percent;

int main(void){
   printf("Type a number: \n");
   scanf("%d", &mynum);
   printf("Your number is %d \n", mynum);
   printf("Give me a percent as a decimal: \n");
   scanf("Your percent is %f", percent);
    return 0;
}