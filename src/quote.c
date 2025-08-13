#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include "quote.h"

void show_quote() {
    FILE *file = fopen("quotes.txt", "r");
    if (!file) {
        printf("Error: quotes.txt not found.\n");
        return;
    }

    char *quotes[200];
    char buffer[256];
    int count = 0;

    while (fgets(buffer, sizeof(buffer), file)) {
        buffer[strcspn(buffer, "\n")] = '\0'; // remove newline
        quotes[count] = strdup(buffer);
        count++;
    }
    fclose(file);

    if (count > 0) {
        srand(time(NULL));
        int idx = rand() % count;
        printf("\n💡 Quote: %s\n", quotes[idx]);
    }
}

