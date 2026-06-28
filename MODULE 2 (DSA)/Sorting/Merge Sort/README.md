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


"Algorithm"

Start.
If the array has 0 or 1 element, return because it is already sorted.
Find the middle index of the array.
Divide the array into two halves:
Left half
Right half
Recursively apply Merge Sort to the left half.
Recursively apply Merge Sort to the right half.
Merge the two sorted halves:
Compare the first element of both halves.
Copy the smaller element into the original array.
Move the pointer of the copied element.
Repeat until one half is exhausted.
Copy any remaining elements from the left half.
Copy any remaining elements from the right half.
Return the sorted array.
Stop.
