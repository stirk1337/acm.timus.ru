n, k = [int(x) for x in input().split()]
if (n <= k):
    print(2)
else:
    if ((n * 2) % k == 0):
        print(int(n * 2 / k))
    else:
        print(int(n * 2 / k + 1))
