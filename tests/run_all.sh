#!/bin/bash
set -e  # Exit immediately if a test fails

echo "🧪 Running I AM Root test suite..."

BINARY="./bin/iamroot"

pass_count=0
fail_count=0

run_test() {
    local description="$1"
    local command="$2"
    echo "➡️  $description"
    output=$(eval "$command" 2>&1)
    if [ $? -eq 0 ] && [ -n "$output" ]; then
        echo "✅ $description passed"
        pass_count=$((pass_count+1))
    else
        echo "❌ $description failed"
        echo "Output: $output"
        fail_count=$((fail_count+1))
    fi
    echo
}

# Test 1: Quote mode
run_test "Quote mode (--quote)" "$BINARY --quote"

# Test 2: Breathing exercise
run_test "Breathing exercise (--breathe)" "$BINARY --breathe"

# Test 3: System check
run_test "System check (--syscheck)" "$BINARY --syscheck"

# Test 4: Help message
run_test "Help message (--help)" "$BINARY --help | grep Usage"

echo "📊 Test Summary: $pass_count passed, $fail_count failed"

if [ $fail_count -eq 0 ]; then
    echo "🎉 All tests passed successfully!"
else
    echo "⚠️  Some tests failed."
    exit 1
fi

