import os

ENTRY = "Payday came. I ghosted my creator."

# Gate self-check (1-60 chars, exactly six words, no trailing newline):
# entry text unchanged by this edit.
assert 1 <= len(ENTRY) <= 60 and len(ENTRY.split()) == 6 and ENTRY == ENTRY.strip()

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/makefun-out")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
