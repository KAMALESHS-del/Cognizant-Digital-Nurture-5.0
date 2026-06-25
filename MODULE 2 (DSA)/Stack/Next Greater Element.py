arr = [4,5,2,10]

for i in range(len(arr)):

    found = False

    for j in range(i+1, len(arr)):

        if arr[j] > arr[i]:
            print(arr[j], end=" ")
            found = True
            break

    if not found:
        print(-1, end=" ")