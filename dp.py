import random

def can_reach_target_with_solution(arr, multipliers, target):
    n = len(arr)
    DP = [dict() for _ in range(n+1)]
    DP[n][target] = None

    # Build backwards, allowing an early-exit injection of the target
    for i in range(n-1, -1, -1):
        # “If you can reach the target from i+1, you can also just stop at i.”
        if target in DP[i+1]:
            DP[i][target] = None

        for s_next in DP[i+1]:
            # Case A: addition
            s_add = s_next - arr[i]
            if s_add >= 0:
                DP[i].setdefault(s_add, (s_next, 'add', arr[i]))

            # Case B: multiplication—but *skip* this at i==0!
            if i > 0:
                for m in multipliers:
                    if s_next % m == 0:
                        s_mul = s_next // m
                        DP[i].setdefault(s_mul, (s_next, 'mul', m))

    # If you never marked s=0 as “good” at layer 0, there is no valid path
    if 0 not in DP[0]:
        return False, None

    # Reconstruct: start at s=0 and stop as soon as we hit a None (the early-exit flag)
    path = []
    s, i = 0, 0
    while i < n and DP[i][s] is not None:
        next_s, op, val = DP[i][s]
        path.append((i, s, op, val))
        s, i = next_s, i + 1

    return True, path

def run_dp(arr, multipliers, target, limit=None):
    if limit is not None:
        arr = arr[:limit]
    possible, path = can_reach_target_with_solution(arr, multipliers, target)
    return possible, path

def main(n=81, target=5000):
    arr = [random.randint(0, 100) for _ in range(n)]

    multipliers = [2, 5, 10]
    print(f"Array: {arr}")
    print(f"Target: {target}")
    possible, path = can_reach_target_with_solution(arr, multipliers, target)
    print(f"Is it possible to reach exactly {target}? {'Yes' if possible else 'No'}")
    if possible:
        print("Solution path:")
        s = 0
        for idx, prev_s, op, val in path:
            if op == 'add':
                print(f"Step {idx}: s = {s} + {val} -> {s+val}")
                s = s + val
            else:
                print(f"Step {idx}: s = {s} * {val} -> {s*val}")
                s = s * val

if __name__ == "__main__":
    main()