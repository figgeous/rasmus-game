import random

def can_reach_target_brute(arr, multipliers, target):
    n = len(arr)
    results = []
    found = False

    def dfs(idx, s, path):
        nonlocal found
        if s > 5000 or found:
            return
        if idx == n:
            if s == target:
                results.append(list(path))
                found = True
            return
        # Try addition
        dfs(idx + 1, s + arr[idx], path + [(idx, s, 'add', arr[idx])])
        # Try multiplication for each multiplier
        for m in multipliers:
            dfs(idx + 1, s * m, path + [(idx, s, 'mul', m)])

    dfs(0, 0, [])
    if results:
        return True, results[0]
    else:
        return False, None

def run_brute(arr, multipliers, target):
    return can_reach_target_brute(arr, multipliers, target)

if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(81)]
    multipliers = [2, 5, 10]
    target = 5000
    found, path = run_brute(arr, multipliers, target)
    print(f"Found: {found}")
    if found:
        print("Path:", path)
