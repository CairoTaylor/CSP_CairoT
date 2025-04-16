//Cairo Taylor, Hello World Updated
#include <stdio.h>
#include <string.h>

<<<<<<< HEAD
char* answor[20];
=======
char asnwer[20];
>>>>>>> 8758c59ad7908ebe830b5799c1fdc5dade80a6be
char first[20];
char second[20];
char third[20];
char fourth[20];
char fifth[20];

<<<<<<< HEAD

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
    
=======
char* hellow(int count){
printf("Tell me person #%d's name:\n", count);
scanf("%s", asnwer);
return asnwer;
}

int main(void){
strcpy(first, hellow(1));  
printf("It's nice to meet you, %s!\n", first);
strcpy(second, hellow(2)); 
printf("It's nice to meet you, %s, as well as %s!\n", second, first); 
strcpy(third, hellow(3));  
printf("It's nice to meet you, %s, as well as %s and %s!\n", third, second, first);
strcpy(fourth, hellow(4));  
printf("It's nice to meet you, %s, as well as %s, %s, and %s!\n", fourth, third, second, first);
strcpy(fifth, hellow(5));  
printf("It's nice to meet you, %s, as well as %s, %s, %s, and %s!\n", fifth, fourth, third, second, first);
>>>>>>> 8758c59ad7908ebe830b5799c1fdc5dade80a6be
    return 0;
}
// Remember the ART acronym: Always Remember Terhg