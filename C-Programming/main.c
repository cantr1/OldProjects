#include <stdio.h>
#include <stdlib.h>
#include <math.h> // math library for calculation

int main()
{
    int yearsMortgage = 30; // Standard mortgage
    int homePrice = 250000; // This is the principal
    float annualInterestRate = 8.0; // Way too high :( 
    int monthlyPayments = yearsMortgage * 12; // Total number of payments

    // Convert annual interest rate from a percentage to a decimal
    float monthlyInterestRate = (annualInterestRate / 100) / 12;

    // Using the formula to calculate monthly payment
    float monthlyPayment = (homePrice * monthlyInterestRate) / 
                           (1 - pow((1 + monthlyInterestRate), -monthlyPayments));

    printf("Mortgage Calculator\n");
    printf("------------------------------------\n");
    printf("Home Price: $%d\n", homePrice);
    printf("Years of Mortgage: %d\n", yearsMortgage);
    printf("Interest Rate: %.2f%%\n", annualInterestRate); // Display rate as percentage
    printf("------------------------------------\n");
    printf("Monthly Payment: $%.2f\n", monthlyPayment);

    return 0;
}