num = int(input())
arr = []
for i in range(num):
    temp_arr = input().split(' ')
    arr.append(temp_arr)
string = ''
for i in range(num):
        k = i
        j = 0
        while k >= 0:
                string += (arr[k][j] + ' ')
                k -= 1
                j += 1
for i in range(1,num,1):
        k = num - 1
        j = i
        while j != num:
                string += (arr[k][j] + ' ')
                k -= 1
                j += 1
print(string)
