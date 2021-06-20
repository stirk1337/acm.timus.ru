import sys
s = list(input())

for i in range(len(s)):
	s[i] = ord(s[i]) - ord('a')
old = s.copy()

if len(s) == 1:
	s[0] = s[0] - 5
	if s[0] < 0:
		s[0]+=26
	print(chr(ord('a') + s[0]))
	sys.exit()

s[0] -= 5

if s[0] < 0:
	s[0] += 26

s[1] = s[1] - old[0]
if s[1] < 0:
	s[1] += 26
	old[1] = s[1] + old[0]

for i in range(2, len(s)):
	s[i] = s[i] - old[i-1]
	while s[i] < 0:
		s[i] += 26
		old[i] = s[i] + old[i-1]

for i in range(len(s)):
	print(chr(ord('a') + s[i]), end  = "")
