# dic={2:1,1:5}
# for key in dic:
#     print(key,dic[key])
def f(n):
    if n==0:
        return 0
    else:
        return n%10+f(n//10)
    
n=f(1234)
print(n)