#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "breathe.h"
#include "quote.h"
#include "timer.h"
#include "syscheck.h"

// Colors
#define GREEN   "\033[1;32m"
#define CYAN    "\033[1;36m"
#define YELLOW  "\033[1;33m"
#define RESET   "\033[0m"

// Clear screen
void clear_screen() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

void print_logo() {
    printf(GREEN);
    printf(GREEN);
    printf("============================================================\n");
    printf("   ██╗ █████╗ ███╗   ███╗    ██████╗  ██████╗  ██████╗ ████████╗\n");
    printf("   ██║██╔══██╗████╗ ████║    ██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝\n");
    printf("   ██║███████║██╔████╔██║    ██████╔╝██║   ██║██║   ██║   ██║   \n");
    printf("   ██║██╔══██║██║╚██╔╝██║    ██╔\\═══╝ ██║   ██║██║   ██║   ██║   \n");
    printf("   ██║██║  ██║██║ ╚═╝ ██║    ██║ \\   ╚██████╔╝╚██████╔╝   ██║   \n");
    printf("   ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝    ╚═╝  \\   ╚═════╝  ╚═════╝    ╚═╝   \n");
    printf(RESET);
    printf(YELLOW);
    printf("\n   🌱  Root yourself in calm. Grow your system. 🌱\n");
    printf("============================================================\n");
    printf("\n🪴 I AM is the root of all. There is nothing else to know 🪴\n\n");
    printf("                       🌱\n");
    printf("                     🌿 🌿\n");
    printf("                  🌿   🌿   🌿\n");
    printf("                 Stay focused. 🚀\n\n");
    printf("============================================================\n" RESET);
}

void print_menu() {
    printf(CYAN "\n=================== I AM Root Menu ==================\n" RESET);
    printf(YELLOW "[1]" RESET " 🌬️  Breathing Exercise\n");
    printf(YELLOW "[2]" RESET " 💬  Daily Quote\n");
    printf(YELLOW "[3]" RESET " ⏳  Focus Timer\n");
    printf(YELLOW "[4]" RESET " 🩺  System Health Check\n");
    printf(YELLOW "[5]" RESET " 📖  Free Motivational Story\n");
    printf(YELLOW "[6]" RESET " 🌟  Premium Motivational Story\n");
    printf(YELLOW "[q]" RESET " 🚪  Quit\n");
}

void clear_input_buffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF) {}
}

void wait_for_enter() {
    printf("\nPress Enter to continue...");
    clear_input_buffer();
    getchar();
}

void reading_animation(int seconds) {
    printf(YELLOW "\n Get Ready to focus on I AM ...\n" RESET);
    for (int i = seconds; i > 0; i--) {
        printf("\rStarting in %d second(s)... ", i);
        fflush(stdout);
        sleep(1);
    }
    printf("\n\n");
}

int main(int argc, char *argv[]) {
    if (argc > 1) {
        if (strcmp(argv[1], "--quote") == 0) {
            show_quote();
            return 0;
        } else if (strcmp(argv[1], "--breathe") == 0) {
            start_breathing(10);
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

    char choice[10];
    while (1) {
        clear_screen();
        printf(YELLOW "Welcome to I AM Root interactive mode.\n\n" RESET);
        print_logo();
        print_menu();
        printf(YELLOW "Enter your choice: " RESET);
        scanf("%s", choice);
        clear_input_buffer();

        if (strcmp(choice, "1") == 0) {
            reading_animation(2);
            system("python3 src/breathing_visual_audio.py");
            wait_for_enter();
        } else if (strcmp(choice, "2") == 0) {
            reading_animation(2);
            show_quote();
            wait_for_enter();
        } else if (strcmp(choice, "3") == 0) {
            int minutes;
            printf("Enter focus duration in minutes: ");
            scanf("%d", &minutes);
            clear_input_buffer();
            start_timer(minutes);
            wait_for_enter();
        } else if (strcmp(choice, "4") == 0) {
            check_system_health();
            wait_for_enter();
        } else if (strcmp(choice, "5") == 0) {
            reading_animation(2);
            system("python3 src/stories.py");
            wait_for_enter();
        } else if (strcmp(choice, "6") == 0) {
            reading_animation(2);
            system("python3 src/stories.py --premium");
            wait_for_enter();
        } else if (strcmp(choice, "q") == 0) {
            printf(GREEN "Goodbye, Stay with I AM! 🌱\n" RESET);
            break;
        } else {
            printf(YELLOW "Invalid choice. Try again.\n" RESET);
            wait_for_enter();
        }
    }
    return 0;
}
