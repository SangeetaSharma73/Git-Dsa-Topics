# def f(n):
#     if n==0:return -1
#     else:
#         print(n)
#         f(n-1)
    
    
# ans=f(4)
# print(ans)
# def f(n):
#     if n==0:return -1
#     else:
#         f(n-1)
#         print(n)
#     return    
# ans=f(4)
# print(ans)
# def f(x,y):
#     if (x==1 or y==1):return 1
#     if (x==y):return x
#     if (x>y):return f(x-y,y)
#     if (y>x):return f(x,y-x)

# ans=f(15,255)
# print(ans)

# def gcd(a,b):
#     if b%a==0:
#         return a
#     else:
#         return gcd(b%a,a)
# a=gcd(122,16)
# print(a)
# def a(n):
#     if n==0:
#         return 
#     else:
#         a(n-1)
#         print(n)
#         return 
# ans=a(3)
# print(ans)
# def f(n):
#     x=1
#     if n==1:
#         return x
#     for k in range(1,n):
#         x=x+f(k)*f(n-k)
#     return x
# ans=f(5)
# print(ans)
# def f(n):
#     if n==0:
#         return 1
#     elif n<0:
#         return 0
#     else:
#         return f(n-1)+f(n-2)
# ans=f(4)
# print(ans)
# def f(k,n,arr):
#     if k==0:return 1
#     if k<0:return 0
#     count=0
#     for i in range(n):
#         count+=f(k-arr[i],n,arr)
#     return count
# ans=f(39,3,[8,10,2])
# print(ans)
# def f(n):
#     if n == 0:
#         return 10
#     if n == 1:
#         return 10
#     if n == 2:
#         return -19
#     if n > 2 and n % 2 == 0 and n % 3 == 0:
#         return n // 6 + (f(n - 1) + f(n - 3))
#     elif n > 2 and n % 2 == 0:
#         return n // 2 - (f(n - 1) + f(n - 2))
#     elif n > 2 and n % 3 == 0:
#         return n // 3 + (f(n - 1) + f(n - 2))  # Change n-3 to n-2
#     else:
#         return f(n - 1)
# ans = f(7)
# print(ans)

# def f(x,n,i,sm):
#     if i>n:
#         return sm
#     def factorial(n):
#         if n==1:
#             return 1
#         else:
#             return n*factorial(n-1)
#     sm+=x**i//factorial(i)
#     return f(x,n,i+1,sm)
# ans=f(5,1,1,1.0)
# print(ans)

# def fun(n): 
  
#     if n==0:
#         return 1
#     c=0
#     c+=fun(n-1)
#     return c
# # Driver code 
# ans=fun(4) 
# print(ans)
def f(n):
    if n==0:
        return 1
    if n<0:return 0
    return f()