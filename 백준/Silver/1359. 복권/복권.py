import sys
from itertools import combinations

input_data = sys.stdin.readline().rstrip().split()

a = int(input_data[0])
b = int(input_data[1])
c = int(input_data[2])

user_case = len(list(combinations(range(a), b)))
answer_case = len(list(combinations(range(a), b)))

denominator = user_case * answer_case

numerator = 0
for i in range(c, b+1):
    numerator += len(list(combinations(range(b), i))) * len(list(combinations(range(a-b), b-i)))

numerator *= user_case

print(numerator / denominator)
