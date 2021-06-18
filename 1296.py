from sys import maxsize
def maxSubArraySum(a,size): 
    max_so_far = -maxsize - 1
    max_ending_here = 0  
    for i in range(0, size): 
        max_ending_here = max_ending_here + a[i] 
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
  
        if max_ending_here < 0: 
            max_ending_here = 0   
    return max_so_far 

a = []
n = int(input())
for i in range(n):
	a.append(int(input()))

if n == 0:
	print(0)
else:
	if max(a) < 0 or n == 0:
		print(0)
	else:
		print(maxSubArraySum(a, len(a)))
