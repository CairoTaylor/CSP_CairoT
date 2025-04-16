// Cairo Taylor, Old Enough Project
#include <stdio.h>

int age;

int main(void){
printf("How old are you chumster?\n");
scanf("%d", &age);

if(age < 6){
    printf("Sorry, but you aren't even old enough to go to school.\n");
}else if(age >= 6 && age <15){
    printf("You are old enough to go to school, however your parents have to take you.\n");
}else if(age >= 15 && age < 16){
    printf("You are old enough to go to school and get your learners permit, but no driving on your own yet.\n");
}else if(age >= 100 && age < 120){
    printf("Wow you are very old. How exactly are you using this program?");
}else if(age >= 16 && age < 18){
    printf("You are old enough to go to school and get your drivers license, but no voting for you yet.\n");
}else if(age >= 120){
    printf("How are you still alive??");
}else{
    printf("Congratulations! You can drive and vote, and you're also out of school!\n");
}

    return 0;
}