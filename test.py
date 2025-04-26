import time
import random
from dp import run_dp
from brute import run_brute

# Test parameters
def performance_test(n=81, target=5000, multipliers=[2, 5, 10], runs=5):
    dp_times = []
    brute_times = []
    dp_results = []
    brute_results = []
    for i in range(runs):
        arr = [random.randint(1, 100) for _ in range(n)]
        # DP timing
        start = time.time()
        dp_result, dp_path = run_dp(arr, multipliers, target)
        dp_time = time.time() - start
        dp_times.append(dp_time)
        dp_results.append(dp_result)
        # Brute timing
        start = time.time()
        brute_result, brute_path = run_brute(arr, multipliers, target)
        brute_time = time.time() - start
        brute_times.append(brute_time)
        brute_results.append(brute_result)
        # Optionally print on first run
        if i == 0 and n <= 12:
            print(f"Test array (size={n}): {arr}")
            print(f"Multipliers: {multipliers}, Target: {target}\n")
            print(f"DP: Found={dp_result}, Time={dp_time:.6f}s")
            print(f"Brute: Found={brute_result}, Time={brute_time:.6f}s")
            if dp_result:
                print("DP Path:", dp_path)
            if brute_result:
                print("Brute Path:", brute_path)
    print(f"\nAveraged over {runs} runs:")
    print(f"DP:   Avg Time = {sum(dp_times)/runs:.6f}s, Found in {sum(dp_results)}/{runs} runs")
    print(f"Brute:Avg Time = {sum(brute_times)/runs:.6f}s, Found in {sum(brute_results)}/{runs} runs")

if __name__ == "__main__":
    # Use small n for brute force to avoid long runtimes
    performance_test(n=81, target=5000, multipliers=[2, 5, 10], runs=10)
