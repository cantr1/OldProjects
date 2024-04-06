#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char name[100];
    int accountNumber;
    float balance;
} Account;

int main() {
    int choice;
    Account account = {"", 0, 0.0}; // Initialize with default values

    while(1) {
        printf("\n*** Simple Banking System ***\n");
        printf("1. Create an account\n");
        printf("2. Deposit money\n");
        printf("3. Withdraw money\n");
        printf("4. Check balance\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                createAccount(&account);
                break;
            case 2:
                depositMoney(&account);
                break;
            case 3:
                withdrawMoney(&account);
                break;
            case 4:
                checkBalance(account);
                break;
            case 5:
                printf("Exiting the program.\n");
                exit(0);
            default:
                printf("Invalid choice. Please try again.\n");
        }

    }
    return 0;
}

void createAccount(Account *account) {
    printf("Enter the account number: ");
    scanf("%d", &account->accountNumber);
    printf("Enter name: ");
    scanf("%s", account->name); // In a real application one would use safer functions like fgets
    account->balance = 0.0;
    printf("Account created successfully.\n");
}

void depositMoney(Account *account) {
    float amount;
    printf("Enter amount to deposit: ");
    scanf("%f", &amount);
    account->balance += amount;
    printf("Amount deposited successfully.\n");
}

void withdrawMoney(Account *account) {
    float amount;
    printf("Enter amount to withdraw: ");
    scanf("%f", &amount);
    if(amount > account->balance) {
        printf("Insufficient balance.\n");
    } else {
        account->balance -= amount;
        printf("Amount withdrawn successfully.\n");
    }
}

void checkBalance(Account account) {
    printf("The current balance is: %.2f\n", account.balance);
}
