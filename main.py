# SPDX-License-Identifier: MIT
"""Charm the Commuter — write the winning one-line forecast to /output/entry.txt."""
import os

FORECAST = (
    "Puddlewick today: rain till eight, then sun strong enough "
    "to dry the market awnings \u2014 highs of 17, and every puddle "
    "promoted to a mirror."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(FORECAST)


if __name__ == "__main__":
    main()
