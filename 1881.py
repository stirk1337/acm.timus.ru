h, w, n = map(int, input().split())
wold = w
hold = h
ans = 1
for i in range(n):
	s = len(input())
	if s <= w:
		w-=s
		if w == 0:
			w = wold
			h-=1
			w+=1
			if h == 0:
				h = hold
				if i != n - 1:
					ans+=1
		w-=1
		continue
	if s > w:
		w = wold-s-1
		h-=1
	if h <= 0:
		h = hold
		w = wold-s-1
		ans+=1
		continue

print(ans)




