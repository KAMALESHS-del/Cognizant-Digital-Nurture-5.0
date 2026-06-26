"Linear Search is a searching algorithm that checks each element one by one until the target element is found or the array ends."


arr = [10, 20, 30, 40, 50]
target = 30

for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at index:", i)
        break

"""When do we use Linear Search?
✅ Array is unsorted.
✅ Small amount of data.
✅ Easy to implement."""


"""Practice Question

Write a linear search program for:

arr = [12, 18, 25, 30, 45]
target = 18

Expected output:

Found at index: 1"""

def lin(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            print("Found at index:",i)
            found=True
            break

arr = [12, 18, 25, 30, 45]
target = 18
found = False
if not found:
    print("not found")
