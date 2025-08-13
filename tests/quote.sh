#!/bin/bash
set -e
OUTPUT=$(./bin/iamroot --quote)
if [[ "$OUTPUT" != "" ]]; then
    echo "✅ quote.sh: Quote output found"
else
    echo "❌ quote.sh: No quote output"
    exit 1
fi

