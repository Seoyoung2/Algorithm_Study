# data[i] : i+!번째 포도주의 양
# Po[i] : i+1번째 포두주를까지의 최대로 마신 포도주 양
# Po[i] = max(Po[i-2], Po[i-3] + data[i-1], Po[i-4]+data[i-1]) + data[i]


from sys import stdin

t = int(stdin.readline())
data = []
for _ in range(t):
    data.append(int(stdin.readline()))

Po = []
for i in range(t):
    if i == 0:
        Po.append(data[0])
    elif i == 1:
        Po.append(data[0]+data[1])
    elif i == 2:
        Po.append(max(data[0], data[1])+data[2])
    elif i == 3:
        Po.append(max(data[0]+data[2], data[0]+data[1]) + data[3])
    else:
        Po.append(max(Po[i-2], Po[i-3] + data[i-1], Po[i-4]+data[i-1]) + data[i])

print(max(Po))
