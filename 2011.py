import math
n = int(input())
st = input()
lst = []
s1 = lst.append(st.count("1"))
s2 = lst.append(st.count("2"))
s3 = lst.append(st.count("3"))
lst = sorted(lst)
if lst[0]>=1 or (lst[1]>=2 and lst[2]>=2) or (lst[1]>=1 and lst[2]>=5):
	print("Yes")
else:
	print("No")
