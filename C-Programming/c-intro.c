#include <stdio.h>
#include <stdlib.h>

int main()
{
    char name[] = "Kelly";
    int timeProgramming = 2;
    printf("Hello world!\n");
    printf("My name is %s\n", name);
    printf("I have been programming for %d years.\n", timeProgramming);
    printf("This is my first program in C\n");

    char username[20];
    printf("What is your name? ");
    scanf("%s", username); // can use the function 'fgets()' instead
    printf("Hello %s\n", username);


    return 0;
}