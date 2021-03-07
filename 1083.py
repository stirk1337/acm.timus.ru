s = input()
k = s.count("!")
s = int(s.replace("!", ""))

ans = 1
while s > 0:
	ans *= s
	s -= k

print(ans)