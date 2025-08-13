#!/bin/bash
set -e
OUTPUT=$(./bin/iamroot)
if [[ "$OUTPUT" == *"Root"* ]]; then
    echo "✅ basic.sh: Root string found"
else
    echo "❌ basic.sh: Root string NOT found"
    exit 1
fi

