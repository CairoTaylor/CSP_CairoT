//cairo Taylor, Functions Notes
#include <stdio.h>

void add(int num1, int num2){
    printf("%d\n", num1+num2);
}

const char* input(char type[50], int length){
    char answer[50];
    printf("Give me a %s:\n", type);
    getStr(answer, sizeof(answer)-1);
    return answer;
}

int main(void){
   //printf("Hello World\n");
   //add(12, 9);
   input("name", 50);
   input("verb", 50);
   input("place", 50);
   printf("%s was %s until they somehow reached %s", input("name", 50), input("verb", 50), input("place", 50));
   return 0;
}