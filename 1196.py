import sys
ll = set()
for i in range(int(sys.stdin.readline())):
    ll.add(sys.stdin.readline())
n = 0
for j in range(int(sys.stdin.readline())):
    if sys.stdin.readline() in ll:
        n += 1
print(n)
