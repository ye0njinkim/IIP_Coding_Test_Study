import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline()
answer = 0

test = 'IO'*N + 'I'

for i in range(len(S)-(N*2 + 1)):
    if S[i] == 'O':
        continue
    else:
        if S[i:i+N*2+1] == test:
            answer += 1

print(answer)