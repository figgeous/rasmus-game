import random

def can_reach_target_with_solution(arr, multipliers, target):
    n = len(arr)
    max_s = target
    DP = [dict() for _ in range(n+1)]  # DP[i][s] = (prev_s, op, op_val)
    DP[n][target] = None  # At the end, only target is a winning state

    for i in range(n-1, -1, -1):
        for s_next in DP[i+1]:
            DP[i][target] = None
            # Case 1: s + arr[i] == s_next => s = s_next - arr[i]
            s_add = s_next - arr[i]
            if 0 <= s_add <= max_s:
                if s_add not in DP[i]:
                    DP[i][s_add] = (s_next, 'add', arr[i])
            # Case 2: s * m == s_next => s = s_next // m if divisible
            for m in multipliers:
                if s_next % m == 0:
                    s_mul = s_next // m
                    if 0 <= s_mul <= max_s:
                        if s_mul not in DP[i]:
                            DP[i][s_mul] = (s_next, 'mul', m)
    # Reconstruct path if possible
    if arr[0] in DP[0]:
        path = []
        idx = 0
        s = 0
        while idx < n:
            if DP[idx][s] is None:  # we've reached the target
                break
            prev_s, op, val = DP[idx][s]
            path.append((idx, s, op, val))
            if op == 'add':
                s = s + val
            else:  # 'mul'
                s = s * val
            idx += 1
        return True, path
    else:
        return False, None

def run_dp(arr, multipliers, target):
    possible, path = can_reach_target_with_solution(arr, multipliers, target)
    return possible, path

def main(n=81, target=5000):
    arr = [random.randint(0, 10) for _ in range(n)]
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

def can_reach_target(arr, multipliers, target):
    # Backward compatibility
    return can_reach_target_with_solution(arr, multipliers, target)[0]

if __name__ == "__main__":
    main()