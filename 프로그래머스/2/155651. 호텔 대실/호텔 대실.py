import heapq

def solution(book_time):
    # Convert times to minutes
    for i in range(len(book_time)):
        start_h, start_m = map(int, book_time[i][0].split(":"))
        end_h, end_m = map(int, book_time[i][1].split(":"))
        book_time[i][0] = start_h * 60 + start_m
        book_time[i][1] = end_h * 60 + end_m

    # Sort bookings by start time
    book_time.sort(key=lambda x: x[0])

    # Initialize a min heap for room availability times
    room_heap = []

    # Iterate over each booking
    for start, end in book_time:
        # Clean time is 10 minutes after the end
        clean_time = end + 10

        # If there are rooms in the heap and the earliest available room is ready before the start time
        if room_heap and room_heap[0] <= start:
            heapq.heappop(room_heap)  # Use that room and remove it from the heap

        # Add the clean time of the current booking to the heap
        heapq.heappush(room_heap, clean_time)

    # The size of the heap is the number of rooms needed
    return len(room_heap)
