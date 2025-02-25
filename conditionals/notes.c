// Cairo Taylor, Conditionals Notes
#include <stdio.h>
#include <string.h>

char name[20];
int num = 7;


int main(void){
    printf("What is your name?\n");
    scanf("%s", name);
   if(strcmp(name, "Terhg") ==0 ){
    printf("Hello, sir king of the universe.\n");
   }else{
    printf("Hello, you weakling named '%s'. Welcome to your worst nightmare.\n", name);
   }

if(num > 5 && num < 10){
    if(num == 7){
        printf("%d is an unlucky number!\n", num);
    }else{
    printf("%d is a small single digit number\n", num);
    }
}else if(num > 10){
    printf("%d is not a single digit number.\n", num);
}else{
    printf("%d is a large single digit number.\n", num);
}
    return 0;
}