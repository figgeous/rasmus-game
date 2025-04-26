import time
import random
from dp import run_dp
from brute import run_brute

# Test parameters
def performance_test(n=81, target=5000, multipliers=[2, 5, 10]):
    arr = [random.randint(1, 100) for _ in range(n)]
    print(f"Test array (size={n}): {arr}")
    print(f"Multipliers: {multipliers}, Target: {target}\n")

    # DP timing
    start = time.time()
    dp_result, dp_path = run_dp(arr, multipliers, target)
    dp_time = time.time() - start
    print(f"DP: Found={dp_result}, Time={dp_time:.6f}s")

    # Brute timing
    start = time.time()
    brute_result, brute_path = run_brute(arr, multipliers, target)
    brute_time = time.time() - start
    print(f"Brute: Found={brute_result}, Time={brute_time:.6f}s")

    # Optionally, print solution path for small n
    if n <= 12:
        if dp_result:
            print("DP Path:", dp_path)
        if brute_result:
            print("Brute Path:", brute_path)

if __name__ == "__main__":
    # Use small n for brute force to avoid long runtimes
    performance_test(n=12, target=5000, multipliers=[2, 5, 10])
