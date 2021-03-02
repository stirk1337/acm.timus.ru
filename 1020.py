from math import pi, sqrt
x = []
y = []
P = 0
N, R = map(float, input().split())
N = int(N)

for i in range(N):
	xinput, yinput = map(float, input().split())
	x.append(xinput)
	y.append(yinput)

for i in range(N-1):
	ab = sqrt(((x[i+1]-x[i])**2)+(y[i+1]-y[i])**2)
	P += ab

P += sqrt(((x[0]-x[N-1])**2)+(y[0]-y[N-1])**2)
S = 2 * R * pi

print(round(P+S,2))