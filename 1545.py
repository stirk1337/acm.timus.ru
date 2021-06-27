n = int(input())
anime = []

for i in range(n):
	anime.append(input())

anime_imba = input()

for i in range(len(anime)):
	if anime[i][0] == anime_imba:
		print(anime[i])
