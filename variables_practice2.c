#include <stdio.h>

char name[] = "Cairo";
char schoolname[] = "UCAS";
int num1 = 6;
int year = 2025;
int num2 = 536;
char eye[] = "blue-green";
char brkfst[] = "toast";
int age = 14;
char color[] = "aquamarine";
char subject[] = "biology";
int main(void){
    printf("Hello, my name is %s. ", name);
    printf("I go to %s for school. ", schoolname);
    printf("A number from 1 to 10 I picked is %d. ", num1);
    printf("This year is %d. ", year);
    printf("Another number I pick, this time from 100 to 1000 is %d. ", num2);
    printf("My eyes are a %s color. ", eye); 
    printf("I like %s for breakfast. ", brkfst);
    printf("I am %d years old. ", age);
    printf("My favorite color is %s. ", color);
    printf("My favorite school subject is %s. ", subject);
    return 0;
}