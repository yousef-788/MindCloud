from itertools import product  # Try all possible choices

# Get K and M within the valid range
while True:
    K, M = map(int, input("Enter K and M: ").split())
    if 1 <= K <= 7 and 1 <= M <= 1000:
        break
    print("Error: 1 ≤ K ≤ 7 and 1 ≤ M ≤ 1000")

lists = []
# Read each list and make sure it follows the rules
for i in range(K):
    while True:
        data = list(map(int, input(f"Enter list {i+1}: ").split()))
        Ni, elements = data[0], data[1:]
        if 1 <= Ni <= 7 and len(elements) == Ni and all(1 <= abs(x) <= 10**9 for x in elements):
            lists.append(elements)
            break
        print(f"Error in list {i+1}: invalid size or element values")

max_value = 0
# Check every combination and keep the highest result
for combination in product(*lists):
    S = sum(x**2 for x in combination) % M
    max_value = max(max_value, S)

print(max_value)
