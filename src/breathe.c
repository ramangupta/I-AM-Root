#include <stdio.h>
#include <unistd.h>
#include "breathe.h"

void start_breathing(int cycles) {

    for (int cycle = 0; cycle < cycles; cycle++) {
        printf("\nInhale... with 'I' \n");
        sleep(3);
        printf("Hold...\n");
        sleep(2);
        printf("Exhale...with 'AM' \n");
        sleep(3);
        printf("Hold...\n");
        sleep(2);
    }
    printf("\nBreathing session complete.\n");
}






