arr = [4, 8, 5, 8, 8]
target = 8

last = -1

for i in range(len(arr)):
    if arr[i] == target:
        last = i

print(last)