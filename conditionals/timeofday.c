// Cairo Taylor, Time of Day
#include <stdio.h>
#include <time.h>

int main(void){
    time_t seconds;
    seconds = time(NULL);
    time_t rawtime;
    struct tm * timeinfo;
    time(&rawtime);
    timeinfo = localtime(&rawtime);
    time_t now = time(NULL);
    struct tm * tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour;

if(hour == 12){
    printf("It's noontime!");
}else if(hour >= 2 && hour < 6){
    printf("Dawn is upon you! You sure do get up early!");
}else if(hour >= 6 && hour < 12){
    printf("Good Morning!");
}else if(hour >= 12 && hour < 20){
    printf("Good evening!");
}else if(hour >= 20 && hour < 22){
    printf("It's getting late!");
}else{
    printf("Go to sleep, it's nighttime.");
}
    return 0;
}