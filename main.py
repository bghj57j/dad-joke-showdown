# Writes the one dad joke to /output/entry.txt, deterministically.
# No network, no randomness: every run writes the same bytes.
# A clean Q&A dad joke: the calendar wants more dates.
# Second attempt: the first line was a tech pun, not a table joke.
import os
LINE = "Why did the calendar break up with the clock? It needed more dates."
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)  # same output on every run; entry is 70 chars, gate allows 200
