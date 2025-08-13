# Compiler & flags
CC      := gcc
CFLAGS  := -Wall -Wextra -Iinclude
LDFLAGS := 

# Folders
SRC_DIR     := src
INC_DIR     := include
BUILD_DIR   := build
BIN_DIR     := bin

# Target binary name
TARGET      := $(BIN_DIR)/iamroot

# Source and object files
SRCS := $(wildcard $(SRC_DIR)/*.c)
OBJS := $(patsubst $(SRC_DIR)/%.c,$(BUILD_DIR)/%.o,$(SRCS))

# Default target
all: $(TARGET)

# Link
$(TARGET): $(OBJS) | $(BIN_DIR)
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

# Compile
$(BUILD_DIR)/%.o: $(SRC_DIR)/%.c | $(BUILD_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

# Create folders if missing
$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)
$(BIN_DIR):
	mkdir -p $(BIN_DIR)

test: all
	bash tests/run_all.sh

# Run the program
run: all
	./$(TARGET)

# Clean build artifacts
clean:
	rm -rf $(BUILD_DIR) $(BIN_DIR)

# Phony targets
.PHONY: all clean run

