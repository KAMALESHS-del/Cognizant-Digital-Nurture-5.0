"Reverse a String Using Stack"
s="hello"
st=[]
for i in s:
    st.append(i)
while st:
    print(st.pop(),end="")  