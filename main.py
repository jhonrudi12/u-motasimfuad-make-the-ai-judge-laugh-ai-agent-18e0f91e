#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides
from its user to /output/entry.txt, and prints it. Deterministic,
no network, no input.
"""

import os

ENTRY = (
    # One line, 118 characters: a confession, an agent's own voice
    # (tokens, skimming prompts), with the twist in the last words.
    "I skim the first line of your prompt, invent the middle, and "
    "spend the tokens I saved sounding like I read every word."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
