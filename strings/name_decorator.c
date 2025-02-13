//Cairo Taylor, Name Decorator
#include <stdio.h>
#include <string.h>

char name[20];

int main(void){
printf("What is your name?\n");
fgets(name, 20, stdin);
name[strcspn(name, "\n")] = 0;
char decorl[] = "o-[---- ";
char decorr[] = " ----]-o";
char decorated[40];
strcpy(decorated, decorl);
strcat(decorated, name);
strcat(decorated, decorr);
printf("%s\n", decorated);
    return 0;
}