
# def f(n,arr,k,sm,ct,ans):
    
#     if sm>k:
#         return 
#     elif sm==k:
#         ans.append(ct)
#         return 
#     for i in range(n):
#         f(n,arr,k,sm+arr[i],ct,ans)
# arr=[1,2,3]
# n,k=3,3
# ans=[]
# ans=f(n,arr,k,0,0,ans)
# print(min(ans))
# print(max(ans))
def f(n, arr, k, sm, ct, ans):
    if sm > k:
        return
    elif sm == k:
        ans.append(ct)
        return
    for i in range(n):
        f(n, arr, k, sm + arr[i], ct + 1, ans)

arr = [2]
n, k = 1,6
ans = []
f(n, arr, k, 0, 0, ans)

if not ans:
    print("No combination found.")
else:
    print("Minimum elements needed:", min(ans))
    print("Maximum elements needed:", max(ans))
