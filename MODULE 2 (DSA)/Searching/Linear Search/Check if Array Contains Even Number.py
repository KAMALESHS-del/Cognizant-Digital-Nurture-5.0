arr = [1, 5, 7, 10]

found = False

for i in arr:
    if i % 2 == 0:
        found = True
        break

if found:
    print("Even number exists")
else:
    print("No even numbers")