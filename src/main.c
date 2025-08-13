#include <stdio.h>
#include <string.h>
#include "breathe.h"
#include "quote.h"
#include "timer.h"
#include "syscheck.h"

void print_logo() {
    printf("\033[1;32m"); // Green color
    printf("      _    ____    _    ____   ____   ___   ___  _   _ \n");
    printf("     / \\  |  _ \\  / \\  |  _ \\ / ___| |_ _| / _ \\| \\ | |\n");
    printf("    / _ \\ | | | |/ _ \\ | |_) | |  _   | | | | | |  \\| |\n");
    printf("   / ___ \\| |_| / ___ \\|  _ <| |_| |  | | | |_| | |\\  |\n");
    printf("  /_/   \\_\\____/_/   \\_\\_| \\_\\\\____| |___| \\___/|_| \\_|\n");
    printf("\033[0m"); // Reset color
    printf("Root yourself in calm. Grow your system. 🪴\n");
    printf("--------------------------------------------------------\n");
}

void print_menu() {
    printf("\n=== I AM Root Menu ===\n");
    printf("1. Breathing Exercise\n");
    printf("2. Daily Quote\n");
    printf("3. Focus Timer\n");
    printf("4. System Health Check\n");
    printf("q. Quit\n");
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
        } else if (strcmp(argv[1], "--help") == 0) {
            printf("Usage: %s [--quote | --breathe | --syscheck | --help]\n", argv[0]);
            return 0;
        }
    }

    // Default interactive mode
    printf("Welcome to I AM Root interactive mode.\n\n");
    print_logo();
    char choice[10];

    while (1) {
        print_menu();
        printf("Enter choice: ");
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
        } else if (strcmp(choice, "q") == 0) {
            printf("Goodbye, Root!\n");
            break;
        } else {
            printf("Invalid choice. Try again.\n");
        }
    }

    return 0;
}
