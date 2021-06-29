s = input().split()

l1 = int(s[0])
l2 = int(s[1])
n1 = int(s[2])
n2 = int(s[3])

print(abs((n2-n1) * (l1 + 2 * l2) - l1))
