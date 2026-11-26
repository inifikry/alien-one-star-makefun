"""One Star, Five Stars for the Food.

Writes a single-sentence alien tourist one-star review of Earth,
with a genuine compliment about the food, to /output/entry.txt.
Deterministic: the same sentence is written on every run.
"""

import os

SENTENCE = (
    "One star: Earth towed my saucer, my translator short-circuited "
    "on small talk, and gravity keeps stealing my snacks, but one "
    "bowl of ramen almost talked me into staying."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
