#include <stdio.h>
#include <unistd.h>
#include "timer.h"

void start_timer(int minutes) {
    int seconds = minutes * 60;
    printf("\nFocus timer started for %d minutes...\n", minutes);
    sleep(seconds);
    printf("\nTime's up! Stay rooted.\n");
}
