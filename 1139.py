from math import gcd
x, y = map(int, input().split())
x-=1
y-=1
print(x+y - gcd(x,y))
