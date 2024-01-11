arr=[2,4,6,8,10]
target=5
l=0
r=len(arr)-1
while l<r:
    mid=l+(r-l)//2
    if arr[mid]<target:
        l=mid+1
    else:
        r=mid
if arr[l]==target:
    print(l)
else:
    print(-1)
