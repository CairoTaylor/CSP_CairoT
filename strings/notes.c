//Cairo Taylor, Strings Notes C
#include <stdio.h>
#include <string.h>

char name[20];

int main(void){
    //printf("What is your full name?\n");
    //scanf("%s", name);
    //printf("Hello and welcome to my program, %s.", name);
    //fgets(name, 20, stdin);
    //printf("Hello, %s. \nI've been waiting for you.", name);
    char sentence[] = "The quick brown fox jumps over the lazy dog";
    printf("%lu\n", sizeof(sentence));
    printf("%d\n", strlen(sentence));
    char one[] = "Hello ";
    char two[] = "World!";
    strcat(one, two);
    printf("%s\n", one);
    two[5] = '?';
    strcat(one, two);
    printf("%s\n", one);
    return 0;
}