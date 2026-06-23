arr=[35,20,15,40]
fir=0
sec=0
for i in range(len(arr)):
    if arr[i]>fir:
        sec=fir
        fir=arr[i]
    elif arr[i]>sec and arr[i]!=fir:
        sec=arr[i]
print("sec large is :",sec)          