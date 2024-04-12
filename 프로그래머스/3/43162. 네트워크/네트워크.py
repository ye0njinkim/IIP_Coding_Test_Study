def solution(n, computers):
    answer = 0
    visited = [0]*n
    stack = []
    
    for j in range(n):
        if visited[j] == 0:
            answer += 1
            stack.append(j)
            visited[j] = 1

        while stack:
            k = stack.pop()
            for i in range (n):
                if visited[i] == 0 and computers[k][i] == 1:
                    stack.append(i)
                    visited[i] = 1
    
    return answer