# Cairo Taylor, Financial Calculator Updated

#include <stdio.h>
float income, rent, utilities, groceries, transport, savings, used, expenses;

float input(char type[], float var){
    printf("what is your monthly %s?:\n", type);
    scanf("%f", &var);
    return var;
}

void percent(char type[], int ammount){
    int per = ammount/income * 100;

    printf("your %s is %d% of your income.\n", type, per);
}
    
int main(void){
    
    printf("This calculator will find out all of your expenses for you.\n");
    income = input("income", income);
    rent = input("rent", rent);
    utilities = input("utilities", utilities);
    groceries = input("groceries", groceries);
    transport = input("transportation", transport);
    
    savings = income *.2;
    expenses = rent + utilities + groceries + transport;
    used = income - expenses - savings;
    
    printf("you make %.2f\n", income);
    printf("so, your expenses are $%.2f\n", expenses);
    printf("and your savings are $%.2f\n", savings);
    printf("as well your spending money is $%.2f\n", used);

    percent("rent", rent);
    percent("utilities", utilities);
    percent("groceries", groceries);
    percent("transportation", transport);
    percent("savings", savings); 
    percent("expenses", expenses);
    percent("spending", used);   
    return 0;
}
