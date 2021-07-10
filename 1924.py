n = int(input())
ns = []
snum = 0
for j in range(n):
    ns.append(j+1)
for i in range(n):
    if i % 2 != 0:
        snum1 = snum + ns[i]
        if snum1 % 2 == 0:
            snum += ns[i]
        else:
            snum -= ns[i]
    else:
        snum1 = snum + ns[i]
        if snum1 % 2 != 0:
            snum += ns[i]
        else:
            snum -= ns[i]


if snum % 2 == 0:
    print("black")
else:
    print("grimy")
