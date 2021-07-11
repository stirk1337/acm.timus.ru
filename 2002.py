logins = []
passwords = []
answer = []
logged = []

n = int(input())
for i in range(n):
	no_user = 'fail: no such user'
	command = input().split()
	if command[0] == "register":
		if command[1] in logins:
			answer.append('fail: user already exists')
		else:
			logins.append(command[1])
			passwords.append(command[2])
			answer.append('success: new user added')


	if command[0] == 'login':
		for i in range(len(logins)):
			if logins[i] == command[1]:
				no_user = 'fail: incorrect password'
				if passwords[i] == command[2]:
					if command[1] in logged:
						no_user = 'fail: already logged in'
					else:
						no_user = 0
						answer.append('success: user logged in')
						logged.append(command[1])
		if no_user == 0:
			pass
		else:
			answer.append(no_user)

	if command[0] == 'logout':
		if command[1] in logins:
			if command[1] in logged:
				logged.remove(command[1])
				answer.append('success: user logged out')
			else:
				answer.append('fail: already logged out')	
		else:
			answer.append('fail: no such user')
			
for i in answer:
	print(i)

"""
register vasya 12
register vasya 12
login kekich 13
login vasya 13
login vasya 12
login vasya 12
logout kekich
register watafak 100
logout watafak
logout vasya
"""
