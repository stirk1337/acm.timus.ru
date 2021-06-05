d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
count = int(input())
for i in range(count):
    answer = 0
    zone = input()
    x = int(d.get(zone[0]))
    y = int(zone[1])
    if((y+2 <= 8) and (x-1 >= 1)):
        answer+=1
    if((y+2 <= 8 and x+1 <= 8)):
        answer+=1
    if((y-2 >= 1 and x-1 >= 1)):
        answer+=1
    if((y-2 >= 1 and x+1 <= 8)):
        answer+=1
    if((y+1 <= 8 and x+2 <= 8)):
        answer+=1
    if((y-1 >= 1 and x+2 <= 8)):
        answer+=1
    if((y+1 <= 8 and x-2 >= 1)):
        answer+=1
    if((y-1 >= 1 and x-2 >= 1)):
        answer+=1
    print(answer)
