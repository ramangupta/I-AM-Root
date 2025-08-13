#include <stdio.h>
#include <stdlib.h>
#include "syscheck.h"

void check_system_health() {
    printf("\n=== System Health Check ===\n");

    // CPU Load
    FILE *cpu = popen("top -bn1 | grep 'Cpu(s)' | awk '{print $2}'", "r");
    if (cpu) {
        char cpu_load[10];
        fgets(cpu_load, sizeof(cpu_load), cpu);
        printf("CPU Load: %s%% — Keep your mind as cool as your CPU.\n", cpu_load);
        pclose(cpu);
    }

    // Memory Usage
    FILE *mem = popen("free -m | awk 'NR==2{printf \"%.2f\", $3*100/$2}'", "r");
    if (mem) {
        char mem_usage[10];
        fgets(mem_usage, sizeof(mem_usage), mem);
        printf("Memory Usage: %s%% — Free up some thoughts.\n", mem_usage);
        pclose(mem);
    }
}
