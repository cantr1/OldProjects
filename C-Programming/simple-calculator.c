#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("Welcome to my simple calculator!\n");
    printf("Current Abilities: +,-,*,/ of single digit numbers\n");

    int firstNumber;
    char operation;
    int secondNumber;

    printf("First Number: ");
    scanf("%d", &firstNumber); 
    printf("What Operation: (+, -, *, /): ");
    scanf(" %c", &operation); // space before %c to skip any whitespace characters
    printf("Second Number: ");
    scanf("%d", &secondNumber);

    if (operation == '+') {
        printf("%d %c %d = %d\n", firstNumber, operation, secondNumber, firstNumber + secondNumber);
    } else if (operation == '-') {
        printf("%d %c %d = %d\n", firstNumber, operation, secondNumber, firstNumber - secondNumber);
    } else if (operation == '*') {
        printf("%d %c %d = %d\n", firstNumber, operation, secondNumber, firstNumber * secondNumber);
    } else if (operation == '/') {
        // check to prevent division by zero
        if (secondNumber != 0) {
            printf("%d %c %d = %d\n", firstNumber, operation, secondNumber, firstNumber / secondNumber);
        } else {
            printf("Error: Division by zero is not allowed.\n");
        }
    } else {
        printf("Invalid operation.\n");
    }

    return 0;
}
