"""
This script attempts to find the highest possible target value that can be achieved
using a sequence of operations (addition and multiplication by 2, 5, or 10) on a random array.

Process:
- Generates a random array of integers.
- Uses a fast pre-check (target_or_highest_alternative) to estimate the highest reachable value.
- Iteratively checks, using dynamic programming (run_dp), if the target or lower values can be reached.
- Prints the solution path if found.

Functions:
- target_or_highest_alternative(arr, target):
    Estimates the highest value that can be reached with the allowed operations, not exceeding target.
- main(n=81, target=5000):
    Main routine to run the search and print the result.
"""

import random
from dp import run_dp


def target_or_highest_alternative(arr, target):
    s = 0
    for e in arr:
        s = max(s + e, s * 10)
    return min(s, target)


def main(n=80, target=5000):
    arr = [random.randint(0, 100) for _ in range(n)]

    multipliers = [2, 5, 10]
    current_target = target_or_highest_alternative(arr, target)

    while current_target >= 0:
        possible, path = run_dp(arr, multipliers, current_target, limit=16)

        if not possible:
            possible, path = run_dp(arr, multipliers, target)  # try again with no limit

        if possible:
            print(f"Highest possible target: {current_target}")
            print("Solution path:")
            s = 0
            for idx, prev_s, op, val in path:
                if op == 'add':
                    print(f"Step {idx}: s = {s} + {val} -> {s+val}")
                    s = s + val
                else:
                    print(f"Step {idx}: s = {s} * {val} -> {s*val}")
                    s = s * val
            break
        current_target -= 1
    else:
        print("No possible target found.")

if __name__ == "__main__":
    main()
