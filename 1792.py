import sys
def is_xam(o1, o2, o3, o4, l1, l2, l3):
	if (o1+o3+o4) % 2 == l2 and (o2+o3+o4) % 2 == l1 and (o1+o2+o4) % 2 == l3:
		return True
	else:
		return False

o1, o2, o3, o4, l1, l2, l3 = map(int, input().split())
if is_xam(o1, o2, o3, o4, l1, l2, l3):
	print(o1, o2, o3, o4, l1, l2, l3)
	sys.exit()

was = o1
if o1 == 1:
	o1 = 0
else:
	o1 = 1
if is_xam(o1, o2, o3, o4, l1, l2, l3):
	print(o1, o2, o3, o4, l1, l2, l3)
	sys.exit()
else:
	o1 = was

was = o2
if o2 == 1:
	o2 = 0
else:
	o2 = 1
if is_xam(o1, o2, o3, o4, l1, l2, l3):
	print(o1, o2, o3, o4, l1, l2, l3)
	sys.exit()
else:
	o2 = was

was = o3
if o3 == 1:
	o3 = 0
else:
	o3 = 1
if is_xam(o1, o2, o3, o4, l1, l2, l3):
	print(o1, o2, o3, o4, l1, l2, l3)
	sys.exit()
else:
	o3 = was

was = o4
if o4 == 1:
	o4 = 0
else:
	o4 = 1
if is_xam(o1, o2, o3, o4, l1, l2, l3):
	print(o1, o2, o3, o4, l1, l2, l3)
	sys.exit()
else:
	o4 = was

was = l1
if l1 == 1:
	l1 = 0
else:
	l1 = 1
if is_xam(o1, o2, o3, o4, l1, l2, l3):
	print(o1, o2, o3, o4, l1, l2, l3)
	sys.exit()
else:
	l1 = was

was = l2
if l2 == 1:
	l2 = 0
else:
	l2 = 1
if is_xam(o1, o2, o3, o4, l1, l2, l3):
	print(o1, o2, o3, o4, l1, l2, l3)
	sys.exit()
else:
	l2 = was

was = l3
if l3 == 1:
	l3 = 0
else:
	l3 = 1
if is_xam(o1, o2, o3, o4, l1, l2, l3):
	print(o1, o2, o3, o4, l1, l2, l3)
	sys.exit()
else:
	l3 = was
