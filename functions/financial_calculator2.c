//Cairo Taylor, Financial Calculator 2
#include <stdio.h>
#include <math.h>

float type;
float income;
float rent;
float utilities;
float groceries;
float transportation;
float savings;
float spending;
float pertype;

float info(income, amount, type){
   pertype = amount/income*100;
   printf("You spend $%f on %s, which is %f% of your monthly income", amount, type, pertype);
   return amount;
}

int main(void){
   printf("Hello! This is a program for calculating your monthly finances, but now in a new flavor(C).");
   info(income, rent, "rent");
   return 0;
}