N1, C1 = map(int, input().split())
N2, T, C2 = map(int, input().split())
N3 = int(input())
n = int(input())
basic = N1
combined = N2
unlimited = N3
for i in range(n):
	call = list(map(int, input().split(":")))
	if call[0] == 0 and call[1] <= 6:
		continue
	if call[1] == 0:
		basic += C1 * call[0]
	else:
		basic += C1 * (call[0]+1)
	if call[1] == 0:
		T -= call[0]
	else:
		T -= call[0]+1

if T >= 0:
	T = 0
print("Basic:     ", basic, "\n", 
	"Combined:  ", combined+abs(C2*T), "\n",
	"Unlimited: ", unlimited, sep = "")
