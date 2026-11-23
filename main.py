"""One-line roast for make.fun — "One-Line Roast: The Gadget You Use Every Day".

Writes one roast line to $MAKEFUN_OUTPUT_DIR/entry.txt: a single line about
a daily gadget, under 200 characters. Pure stdlib, deterministic, no network.
"""

import os

TEXT = (
    "My robot vacuum mapped my whole house in a day, then got stuck on the "
    "same rug every day since \u2014 genius cartographer, terrible driver."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
