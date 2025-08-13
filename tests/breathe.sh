#!/bin/bash
set -e
OUTPUT=$(./bin/iamroot --breathe)
if [[ "$OUTPUT" == *"Inhale"* && "$OUTPUT" == *"Exhale"* ]]; then
    echo "✅ breathe.sh: Breathing prompts found"
else
    echo "❌ breathe.sh: Breathing prompts missing"
    exit 1
fi

