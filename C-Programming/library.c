#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_BOOKS 100
#define MAX_TITLE 100
#define MAX_AUTHOR 100

void addBook();
void deleteBook();
void searchForBook();
void listAllBooks();

typedef struct {
    int id;
    char title[MAX_TITLE];
    char author[MAX_AUTHOR];
} Book;

Book library[MAX_BOOKS];

int numBooks = 0;

int main() {

    int choice, c;

    while(1) {
        printf("\n*** Simple Library Management System ***\n");
        printf("1. Add book\n");
        printf("2. Delete book\n");
        printf("3. Search for book\n");
        printf("4. List all books\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        // Clear input buffer
        while ((c = getchar()) != '\n' && c != EOF);

        switch(choice) {
            case 1:
                addBook();
                break;
            case 2:
                deleteBook();
                break;
            case 3:
                searchForBook();
                break;
            case 4:
                listAllBooks();
                break;
            case 5:
                printf("Exiting the program.\n");
                return 0;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }
}

void addBook() {
    if(numBooks >= MAX_BOOKS) {
        printf("Library is full. Cannot add more books.\n");
        return;
    }

    printf("Enter book ID: ");
    scanf("%d%*c", &library[numBooks].id); // *c to remove whitespace
    printf("Enter book title: ");
    fgets(library[numBooks].title, MAX_TITLE, stdin);
    library[numBooks].title[strcspn(library[numBooks].title, "\n")] = 0; // Removes the newline character at the end if any
    printf("Enter author name: ");
    fgets(library[numBooks].author, MAX_AUTHOR, stdin);
    library[numBooks].author[strcspn(library[numBooks].author, "\n")] = 0; // Removes the newline character at the end if any

    numBooks++;
    printf("Book added successfully.\n");
}


void deleteBook() {
    int id, i, found = 0;

    printf("Enter book ID to delete: ");
    scanf("%d", &id);

    for(i = 0; i < numBooks; i++) {
        if(library[i].id == id) {
            found = 1;
            break;
        }
    }

    if(found) {
        // Shift all books one position up from the index `i`
        for(int j = i; j < numBooks - 1; j++) {
            library[j] = library[j + 1];
        }
        numBooks--; // Decrease the total number of books as one is deleted
        printf("Book deleted successfully.\n");
    } else {
        printf("Book not found with ID: %d\n", id);
    }
}

void searchForBook() {
    char searchTitle[MAX_TITLE];
    printf("Enter book title to search for: ");
    fgets(searchTitle, MAX_TITLE, stdin);
    searchTitle[strcspn(searchTitle, "\n")] = 0; // Removes the newline character at the end if any

    for(int i = 0; i < numBooks; i++) {
        if(strcmp(library[i].title, searchTitle) == 0) { // Use strcmp since comparing strings
            printf("Book Found:\n");
            printf("Book ID: %d\nTitle: %s\nAuthor: %s\n", library[i].id, library[i].title, library[i].author);
            return;
        }
    }
    printf("Book not found.\n");
}


void listAllBooks() {
    for(int i = 0; i < numBooks; i++) {
        printf("Book ID: %d - Title: %s - Author: %s\n", library[i].id, library[i].title, library[i].author);
    }
}