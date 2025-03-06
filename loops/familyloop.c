// Cairo Taylor, Family Loop
#include <stdio.h>


int main(void){
 char siblings[][20] = {"Billy", "Jennifer", "Jason" ,"James", "John"};
    int mlength = sizeof(siblings) / sizeof(siblings[0]);
    int m = 0;
    while(m < mlength){
        printf("Hello, %s Biggerstaff!\n", siblings[m]);
        m++;
    }

    return 0;
}