s2 = list(input())
s1 = list()
ready = 0
while ready == 0:
	ready = 1
	s1 = s2.copy()
	s2.clear()
	for i in range(0,len(s1)):
		s2.append(s1[i])
		if len(s2) == 1:
			continue
		if s2[len(s2)-1] == s2[len(s2)-2]:
			ready = 0
			del s2[len(s2)-1]
			del s2[len(s2)-1]


print(''.join(s2))
