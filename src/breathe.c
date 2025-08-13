#include <stdio.h>
#include <unistd.h>
#include "breathe.h"

void start_breathing(int seconds) {
    for (int cycle = 0; cycle < 3; cycle++) {
        printf("\nInhale... with "I" \n");
        sleep(seconds);
        printf("Hold...\n");
        sleep(seconds);
        printf("Exhale...with "AM" \n");
        sleep(seconds);
        printf("Hold...\n");
        sleep(seconds);
    }
    printf("\nBreathing session complete.\n");
}






