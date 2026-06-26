arr = [2, 5, 2, 7, 5, 9, 2]
uni=[]
for i in arr:
    if i not in uni:
        uni.append(i)
print(uni)