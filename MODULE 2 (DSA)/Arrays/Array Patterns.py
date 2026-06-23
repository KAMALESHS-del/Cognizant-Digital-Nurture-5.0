"Pattern 1: Traversal"
arr = [1,2,3,4,5]

for i in (arr):
    print(i)

"Pattern 2: Find Maximum"
max=arr[0]
for num in range(len(arr)):
    if arr[num]>max:
        max =arr[num]
print("max element is:",max)  


"Pattern 3: Find Minimum"
min=arr[0]
for i in arr:
    if i<min:
        min=i
print("min elemnet is:",min)     

"Pattern 4: Sum of Array"
sum=0
for i in arr:
    sum+=i
print("arr sum is:",sum) 

"Pattern 5: Count Elements"
count=0
for i in arr:
    if i % 2 == 0:
        count += 1
print("total elements in arr:",count)    