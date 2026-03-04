from __future__ import annotations
import sys
import time
from pathlib import Path
from typing import List






def read_input() -> tuple[int, int, List[int]]:
    # If an input file exists under ./cache_input, use the first one.
    input_file = Path("match_input/input.in")
    lines = input_file.read_text().splitlines()



def main() -> None:
    #Main file
    k, m, requests = read_input()


if __name__ == "__main__":
    main()