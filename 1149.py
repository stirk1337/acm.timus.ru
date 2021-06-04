def A(n):
	A = "sin(1"
	for i in range(2, n+1):
		if i % 2 == 0:
			A += "-sin("+str(i)
		else:
			A += "+sin("+str(i)
	A+= ")" * n
	return A

n = int(input())
nold = n
ans = ""
for i in range(1,n+1):
	ans+=A(i)+"+" +str(n)+")"
	n-=1
print(("("*(nold-1))+ans[:len(ans)-1])
