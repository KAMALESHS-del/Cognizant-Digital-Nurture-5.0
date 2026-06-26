arr = [2, 5, 2, 7, 2, 2]
target = 2

count = 0

for i in arr:
    if i == target:
        count += 1
        break

print(count)