import heapq

def solution(book_time):
    for i in range(len(book_time)):
        start_h, start_m = map(int, book_time[i][0].split(":"))
        end_h, end_m = map(int, book_time[i][1].split(":"))
        book_time[i][0] = start_h * 60 + start_m
        book_time[i][1] = end_h * 60 + end_m

    book_time.sort(key=lambda x: x[0])

    room_heap = []

    for start, end in book_time:
        clean_time = end + 10

        if room_heap and room_heap[0] <= start:
            heapq.heappop(room_heap)

        heapq.heappush(room_heap, clean_time)

    return len(room_heap)
