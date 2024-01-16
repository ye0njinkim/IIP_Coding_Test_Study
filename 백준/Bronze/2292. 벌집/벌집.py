import sys
route_len = 1
power = 1
room_num = int(sys.stdin.readline().rstrip())

while(True):
  room_num = room_num - power
  if room_num <= 0:
    print(route_len)
    break
  power = 6*route_len
  route_len += 1