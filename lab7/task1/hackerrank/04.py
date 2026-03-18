# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

def solve():
    n = int(input())
    letters = input().split()
    k = int(input())

    all_combinations = list(combinations(letters, k))
    total_combinations = len(all_combinations)

    count_with_a = 0
    for combo in all_combinations:
        if 'a' in combo:
            count_with_a += 1

    probability = count_with_a / total_combinations
    print(f"{probability:.3f}")

solve()