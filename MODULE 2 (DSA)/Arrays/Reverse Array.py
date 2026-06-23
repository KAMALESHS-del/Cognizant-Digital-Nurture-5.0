arr=[10,35,20,4,6]
rev=arr[::-1]
print(rev)
"DSA method by two pointers"
left=0
right=len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print(arr)    

