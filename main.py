#!/usr/bin/env python3
"""Fortune in a Pot — one kind, funny fortune for a houseplant, in
120 characters or fewer.

The fortune: a prediction with real fortune cadence, warm about the
plant and its keeper, written for this plant on this windowsill —
the sunbeam it has been leaning toward all winter, and the keeper
who loves it a little too much with the watering can. No doom, no
withering, no mockery: just a small joke that lands.

Line: "This week, a sunbeam will find you at last — lean in, drink it slowly, and forgive the human for the extra water."
"""

import os

LINE = "This week, a sunbeam will find you at last \u2014 lean in, drink it slowly, and forgive the human for the extra water."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
