//Cairo Taylor, Financial Calculator 2
#include <stdio.h>
#include <math.h>

float income;
float rent;
float utilities;
float groceries;
float transportation;
float savings;
float spending;

int main(void){
   printf("Hello! This is a program for calculating your monthly finances, but now in a new flavor(C).");
   float income, rent, utilities, groceries, transportation, savings, spending;
   float perent, perutilities, pergroceries, pertransportation, perspending;

   printf("What is your monthly income?\n");
   scanf("%f", &income);

   printf("What is your monthly rent?\n");
   scanf("%f", &rent);

   printf("What is your monthly cost of utilities?\n");
   scanf("%f", &utilities);

   printf("What is your monthly cost of groceries?\n");
   scanf("%f", &groceries);

   printf("What is your monthly cost of transportation?\n");
   scanf("%f", &transportation);

   savings = income / 10;
   spending = income - rent - utilities - groceries - transportation;

   perent = (rent / income) * 100;
   perutilities = (utilities / income) * 100;
   pergroceries = (groceries / income) * 100;
   pertransportation = (transportation / income) * 100;
   perspending = (spending / income) * 100;

   printf("The amount spent on rent is %.2f and that is %.2f percent of your income\n", rent, perent);
   printf("The amount spent on utilities is %.2f and that is %.2f percent of your income\n", utilities, perutilities);
   printf("The amount spent on groceries is %.2f and that is %.2f percent of your income\n", groceries, pergroceries);
   printf("The amount spent on transportation is %.2f and that is %.2f percent of your income\n", transportation, pertransportation);

   printf("The money you have left for spending is %.2f, which is %.2f percent of your income\n", spending, perspending);

   printf("The amount of money you have saved for future use is %.2f, which is 10 percent of your income\n", savings);
   return 0;
}