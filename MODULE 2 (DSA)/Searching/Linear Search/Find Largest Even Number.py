arr = [5, 12, 8, 21, 18]

largest = -1

for i in arr:
    if i % 2 == 0 and i > largest:
        largest = i

print(largest)