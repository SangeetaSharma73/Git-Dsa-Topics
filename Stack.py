#1.smaller element to it's left
arr=[7,3,4,3,2,9,6,1]
n=len(arr)
res=[-1]*n
st=[0]
for i in range(n):
    while st and arr[st[-1]]>=arr[i]:
        st.pop()
    if st:
        res[i]=arr[st[-1]]
    else:
        res[i]=-1
    st.append(i)
print(res)
#2.smaller element to it's right
arr=[7,3,4,3,2,9,6,1]
n=len(arr)
res=[-1]*n
st=[n-1]
for i in range(n-2,-1,-1):
    while st and arr[st[-1]]>=arr[i]:
        st.pop()
    if st:
        res[i]=arr[st[-1]]
    else:
        res[i]=-1
    st.append(i)
print(res)
#3.Nearest greater element to it's left
arr=[7,3,4,3,2,9,6,1]
n=len(arr)
res=[-1]*n
st=[0]
for i in range(n):
    while st and arr[st[-1]]<=arr[i]:
        st.pop()
    if st:
        res[i]=arr[st[-1]]
    else:
        res[i]=-1
    st.append(i)
print(res)
#4.Nearest greater element to it's right
arr=[7,3,4,3,2,9,6,1]
n=len(arr)
res=[-1]*n
st=[n-1]
for i in range(n-2,-1,-1):
    while st and arr[st[-1]]<=arr[i]:
        st.pop()
    if st:
        res[i]=arr[st[-1]]
    else:
        res[i]=-1
    st.append(i)
print(res)