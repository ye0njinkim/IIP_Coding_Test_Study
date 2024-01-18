import heapq

def solution(n, k, enemy):
    temp = []
    temp_sum = 0
    temp_num = 0
    temp_sum_list = []
    for i in range(len(enemy)):
        heapq.heappush(temp, enemy[i])
        if i+1 <= k:
            continue
        else:
            n -= heapq.heappop(temp)
            if n < 0:
                return i
    answer = len(enemy)
    return answer