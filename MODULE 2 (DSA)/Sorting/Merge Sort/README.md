Merge Sort is a Divide and Conquer algorithm.

It works in 2 steps:

Divide the array into two halves until each subarray has one element.
Merge the subarrays back together in sorted order.
Example

Array:

[5, 3, 8, 4, 2]
Divide
          [5,3,8,4,2]
            /      \
       [5,3]      [8,4,2]
       /   \       /    \
     [5]  [3]   [8]   [4,2]
                        /  \
                      [4]  [2]

Now every array has only one element.

Merge
[5] + [3]   → [3,5]

[4] + [2]   → [2,4]

[8] + [2,4] → [2,4,8]

[3,5] + [2,4,8]

↓

[2,3,4,5,8]




## Algorithm

1. Start.
2. If the array contains **0 or 1 element**, it is already sorted. Return the array.
3. Find the middle index of the array.
4. Divide the array into two halves:
   - Left Half
   - Right Half
5. Recursively apply Merge Sort to the left half.
6. Recursively apply Merge Sort to the right half.
7. Merge the two sorted halves:
   - Compare the first elements of both halves.
   - Copy the smaller element into the original array.
   - Move the corresponding pointer.
   - Repeat until one half is exhausted.
8. Copy any remaining elements from the left half.
9. Copy any remaining elements from the right half.
10. Return the sorted array.
11. Stop.


