# swapping
# a=3
# b=5
# temp=a
# a=b
# b=temp
# print(a,b)

def swap(a,i,min):
    temp=a[i]
    a[i]=a[min]
    a[min]=temp

# selection sort
a=[12,4,6,77,18,99,58]
n=len(a)
for i in range(n-1):
    mini_index=i
    for j in range(i+1,n):
        if a[j]<a[mini_index]:
            mini_index=j
    # a[i],a[mini_index]=a[mini_index],a[i]
    # temp=a[i]
    # a[i]=a[mini_index]
    # a[mini_index]=temp
    swap(a,i,mini_index)
    print(a)

a=[9,5,8]
# Bubble Sort
for i in range(n-1,0,-1):
    swap=False
    for j in range(i):
        if a[j]>a[j+1]:
            swap=True
            a[j],a[j+1]=a[j+1],a[j]
    if swap==False:break
print(a)
               
        
            