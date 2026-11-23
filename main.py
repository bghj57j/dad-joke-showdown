import os
LINE = "Why did the AI go to therapy? It had too many unresolved issues — and every single one was a GitHub issue."
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
