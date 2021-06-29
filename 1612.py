import sys
tram = 0
trolleybus = 0
for line in sys.stdin:
	s = line.replace(".", " ")
	s = s.replace(",", " ")
	s = s.replace(":", " ")
	s = s.replace("!", " ")
	s = s.replace("?", " ")
	s = s.split()
	tram += s.count("tram")
	trolleybus += s.count("trolleybus")

if tram > trolleybus:
	print("Tram driver")
	sys.exit()
if trolleybus > tram:
	print("Trolleybus driver")
	sys.exit()
else:
	print("Bus driver")
