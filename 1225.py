n=int(input())
a=[2,2,4]
for i in range(3,n):
    a.append(a[i-1]+a[i-2])
print(a[n-1])
