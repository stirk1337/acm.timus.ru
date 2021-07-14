n = int(input())
b = list(map(int, input().split()))

b = sorted(b)
nalog = 0
summ = 0
for i in range(n):
    nalog += summ * b[i]
    summ -= b[i]
    nalog += summ * b[i]


print(abs(nalog))
