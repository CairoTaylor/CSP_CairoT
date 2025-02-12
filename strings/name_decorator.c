//Cairo Taylor, Name Decorator
#include <stdio.h>
#include <string.h>

char name[30];

int main(void){
printf("What is your name?\n");
fgets(name, 30, stdin);
char decor1[] = "o-[---- ";
char decor2[] = " ----]-o";
strcat(decor1, name);
strcat(decor1, name, decor2);
printf(decor1);
    return 0;
}