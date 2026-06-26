arr = [10, 15, 7, 18, 3]

smallest = None

for i in arr:
    if i % 2 != 0:
        if smallest is None or i < smallest:
            smallest = i

print(smallest)