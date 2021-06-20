n, m = map(int, input().split())
y1, x1 = map(int, input().split())
y2, x2 = map(int ,input().split())
used = []
for i in range(n):
	used.append([])
for i in range(n):
	for j in range(m):
		used[i].append(0)
x1-=1
y1-=1
x2-=1
y2-=1
x, y = 0, 0
ans = 0
triggerfirst = 0
triggertwo = 0
go = "right"
while(True):
	if x == x1 and y == y1:
		if triggertwo == 1:
			print(ans)
			break
		triggerfirst = 1
	if x == x2 and y == y2:
		if triggerfirst == 1:
			print(ans)
			break
		triggertwo = 1
	if triggerfirst == 1 or triggertwo == 1:
		ans+=1
	if go == "right":
		if x+1 < m:
			if used[y][x+1] == 0:
				used[y][x]=1
				x+=1
			else:
				used[y][x] = 1
				go = "down"
				y+=1
		else:
			used[y][x] = 1
			go = "down"
			y+=1
		continue	
	if go == "down":
		if(y+1 < n):
			if (used[y+1][x] == 0):
				used[y][x] = 1
				y+=1
			else:
				used[y][x] = 1
				go = "left"
				x-=1
		else:
			used[y][x] = 1
			go = "left"
			x-=1
		continue
	if go == "left":
		if(x-1 >= 0):
			if(used[y][x-1] == 0):
				used[y][x] = 1
				x-=1
			else:
				used[y][x] = 1
				go = "up"
				y-=1
		else:
			used[y][x] = 1
			go = "up"
			y-=1
		continue
	if go == "up":
		if(y-1 >= 0):
			if(used[y-1][x] == 0):
				used[y][x] = 1
				y-=1
			else:
				used[y][x] = 1
				go = "right"
				x+=1
		else:
			used[y][x] = 1
			go = "right"
			x+=1
		continue

