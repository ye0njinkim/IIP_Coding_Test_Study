import sys
num_list = []
N = int(sys.stdin.readline())
for i in range(N):
    num_list.append(int(sys.stdin.readline()))
dp = [0] * N

for i in range(N):
    if i == 0:
        dp[i] = num_list[i]
    elif i == 1:
        dp[i] = num_list[i-1] + num_list[i]
    elif i == 2:
        dp[i] = max(num_list[i-1] + num_list[i], num_list[i-2] + num_list[i])
    else:
        dp[i] = max(dp[i-2] + num_list[i], dp[i-3] + num_list[i-1] + num_list[i])

print(dp[N-1])