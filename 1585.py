n = int(input())
emp = 0
lit = 0
mac = 0
for i in range(n):
	penguin = str(input())
	if "Emp" in penguin:
		emp += 1
	elif "Mac" in penguin:
		mac += 1
	elif "Lit" in penguin:
		lit += 1

if emp > mac and emp > lit:
	print("Emperor Penguin")
elif mac > emp and mac > lit:
	print("Macaroni Penguin")
elif lit > emp and lit > mac:
	print("Little Penguin")
	
