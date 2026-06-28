# Function to perform Merge Sort
def merge_sort(arr):

    # If the array has 0 or 1 element, it is already sorted
    if len(arr) > 1:

        # Find the middle index
        mid = len(arr) // 2

        # Divide the array into left and right halves
        left = arr[:mid]
        right = arr[mid:]

        # Recursively sort the left half
        merge_sort(left)

        # Recursively sort the right half
        merge_sort(right)

        # Initialize pointers
        i = 0   # Left array index
        j = 0   # Right array index
        k = 0   # Original array index

        # Compare elements and merge them
        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        # Copy remaining elements from left array
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy remaining elements from right array
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr = [5, 3, 8, 4, 2]

print("Original:", arr)

merge_sort(arr)

print("Sorted :", arr)
