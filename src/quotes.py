# src/quotes.py
import random

quotes = [
    "🌱 Be present, be calm, be you.",
    "🌟 Growth begins with a single breath.",
    "💫 Focus on what matters most.",
    "🌿 Inner peace is the root of strength.",
]

def show_quote():
    print("\n" + random.choice(quotes) + "\n")
