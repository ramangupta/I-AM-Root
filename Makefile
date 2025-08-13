CC = gcc
CFLAGS = -Iinclude -Wall

SRC = src/main.c src/breathe.c src/quote.c src/timer.c src/syscheck.c
OBJ = $(SRC:.c=.o)

all: iamroot

iamroot: $(OBJ)
	$(CC) $(CFLAGS) -o iamroot $(OBJ)

clean:
	rm -f src/*.o iamroot
