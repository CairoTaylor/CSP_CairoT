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
    
}

    return 0;
}