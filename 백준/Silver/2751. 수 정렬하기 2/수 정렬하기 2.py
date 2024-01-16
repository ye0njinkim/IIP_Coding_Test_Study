import sys

N = int(sys.stdin.readline().rstrip())

temp_list = []

for i in range(N):
  temp_list.append(int(sys.stdin.readline().rstrip()))


temp_list.sort()
for i in range(len(temp_list)):
  print(temp_list[i])