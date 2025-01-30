#include <stdio.h>

char name[] = "Cairo";
int num = 14;
float pi = 3.141592;

int main(void){
    printf("Hello %s\n", name);
    printf("%d\n", num);
    printf("%f\n", pi);
    printf("How are you doing today, %s? \n", name);
    printf("Hello, my name is %s, I am %d years old, and my favorite number is %f. \n", name, num, pi)
    return 0;
}