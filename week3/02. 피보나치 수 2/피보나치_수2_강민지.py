memo = [0, 1] + [0] * 90

n = int(input())

for i in range(2, n+1):
    memo[i] = memo[i-1] + memo[i-2]

print(memo[n])