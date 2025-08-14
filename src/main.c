#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "breathe.h"
#include "quote.h"
#include "timer.h"
#include "syscheck.h"

void print_logo() {
    printf("\033[1;32m"); // Green color
    printf("  ___   ___   _   _    _    ____  _____ _____ \n");
    printf(" |_ _| / _ \\ | \\ | |  / \\  |  _ \\| ____|_   _|\n");
    printf("  | | | | | ||  \\| | / _ \\ | |_) |  _|   | |  \n");
    printf("  | | | |_| || |\\  |/ ___ \\|  _ <| |___  | |  \n");
    printf(" |___| \\___/ |_| \\_/_/   \\_\\_| \\_\\_____| |_|  \n");
    printf("                                              \n");
    printf("      Root yourself in calm. Grow your system. 🪴\n");
    printf("          🌱\n");
    printf("         🌿 🌿\n");
    printf("       🌿   🌿   🌿\n");
    printf("      Stay focused. 🚀\n");
    printf("\033[0m"); // Reset color
    printf("--------------------------------------------------------\n");
}

void print_menu() {
    printf("\033[1;32m"); // Green color for menu
    printf("\n=== I AM Root Menu ===\n");
    printf("1. Breathing Exercise\n");
    printf("2. Daily Quote\n");
    printf("3. Focus Timer\n");
    printf("4. System Health Check\n");
    printf("5. Read a Free Motivational Story\n");
    printf("6. Read a Premium Motivational Story\n");
    printf("q. Quit\n");
    printf("\033[0m"); // Reset color
}

int main(int argc, char *argv[]) {
    
    if (argc > 1) {
        if (strcmp(argv[1], "--quote") == 0) {
            show_quote();
            return 0;
        } else if (strcmp(argv[1], "--breathe") == 0) {
            start_breathing(1);
            return 0;
        } else if (strcmp(argv[1], "--syscheck") == 0) {
            check_system_health();
            return 0;
        } else if (strcmp(argv[1], "--stories") == 0) {
            return 0;
        } else if (strcmp(argv[1], "--help") == 0) {
            printf("Usage: %s [--quote | --breathe | --syscheck | --stories | --help]\n", argv[0]);
            return 0;
        }
    }

    // Default interactive mode
    
    char choice[10];

    while (1) {
        system("clear"); // clear terminal for a fresh menu

        printf("Welcome to I AM Root interactive mode.\n\n");
        print_logo();
        print_menu();
        printf("Enter your choice: ");
        scanf("%s", choice);

        if (strcmp(choice, "1") == 0) {
            start_breathing(4);
        } else if (strcmp(choice, "2") == 0) {
            show_quote();
        } else if (strcmp(choice, "3") == 0) {
            int minutes;
            printf("Enter focus duration in minutes: ");
            scanf("%d", &minutes);
            start_timer(minutes);
        } else if (strcmp(choice, "4") == 0) {
            check_system_health();
        } else if (strcmp(choice, "5") == 0) {
            system("python3 src/stories.py");
        } else if (strcmp(choice, "6") == 0) {
            system("python3 src/stories.py --premium");
        } else if (strcmp(choice, "q") == 0) {
            printf("Goodbye, Stay with I AM!\n");
            break;
        } else {
            printf("Invalid choice. Try again.\n");
        }
    }

    return 0;
}
