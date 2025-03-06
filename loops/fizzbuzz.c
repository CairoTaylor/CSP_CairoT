// Cairo Taylor, FizzBuzz
#include <stdio.h>

int x = 1;
int main(void){
   while(x <= 50){
    if(x % 5 == 0 && x % 3 == 0){
    printf("FizzBuzz\n");
   }else if(x % 5 == 0){
    printf("Buzz\n");
   }else if(x % 3 == 0){
    printf("Fizz\n");
   }else{
    printf("%d\n", x);
   }
   x++;
   }
    return 0;
}