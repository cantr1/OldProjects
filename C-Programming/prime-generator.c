#include <stdio.h>
#include <math.h>
#include <stdbool.h>

bool is_prime(int number) {
    if (number < 2) return false;
    for (int i = 2; i <= sqrt(number); i++) {
        if (number % i == 0) return false;
    }
    return true;
}

void print_primes_and_lines(int start, int end) {
    for (int number = start; number <= end; number++) {
        if (is_prime(number)) {
            for (int i = 0; i < number; i++) {
                printf("-");
            }
            printf("\n");
            printf("%d is a Prime Number\n", number);
            printf("\n"); // Create space after printing a prime number
        } 
    }
}

int main() {
    printf("Prime Number Generator\n");
    printf("_____________________________\n");
    print_primes_and_lines(1, 25);
    return 0;
}
