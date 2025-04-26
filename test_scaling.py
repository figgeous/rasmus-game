import time
import random
from dp import run_dp
from brute import run_brute

def scaling_test(ns=[10, 20, 40, 80], target=5000, multipliers=[2, 5, 10]):
    print("n\tDP_time(s)\tBrute_time(s)\tDP_found\tBrute_found")
    for n in ns:
        arr = [random.randint(1, 100) for _ in range(n)]
        # DP timing
        start = time.time()
        dp_result, _ = run_dp(arr, multipliers, target)
        dp_time = time.time() - start
        # Brute timing
        start = time.time()
        brute_result, _ = run_brute(arr, multipliers, target)
        brute_time = time.time() - start
        print(f"{n}\t{dp_time:.6f}\t{brute_time:.6f}\t{dp_result}\t{brute_result}")

if __name__ == "__main__":
    scaling_test(ns=[10, 20, 40, 80], target=5000, multipliers=[2, 5, 10])
