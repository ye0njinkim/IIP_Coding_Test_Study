import sys
a = [0] * 10001

N = int(sys.stdin.readline().rstrip())
for i in range(N):
    a[int(sys.stdin.readline().rstrip())] += 1
for i in range(len(a)):
    for j in range(a[i]):
        print(i)