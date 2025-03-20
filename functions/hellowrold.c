//Cairo Taylor, Hello World Updated
#include <stdio.h>
#include <string.h>

char* answor[20];
char first[20];
char second[20];
char third[20];
char fourth[20];
char fifth[20];


char* input(char count[50]) {
    char answor[50];
    printf("What is person #%s's name?\n", count);
    scanf("%s", answor);
    return answor;
}

int main(void) {
    strcpy(first, input("1"));
    strcpy(second, input("2"));
    strcpy(third, input("3"));
    strcpy(fourth, input("4"));
    strcpy(fifth, input("5"));
    
    printf("Hello, %s!\n", first);
    printf("Hello, %s!\n", second);
    printf("Hello, %s!\n", third);
    printf("Hello, %s!\n", fourth);
    printf("Hello, %s!\n", fifth);
    
    return 0;
}