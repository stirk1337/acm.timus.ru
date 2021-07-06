def bin_Search(arr, val):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if val < arr[mid]:
            high = mid - 1
        elif val > arr[mid]:
            low = mid + 1
        else:
            return True
    else:
           return False


aa = int(input())
aArr = list(map(int, input().split()))
b = int(input())
bArr = list(map(int, input().split()))
c = int(input())
cArr = list(map(int, input().split()))

aArr.sort()
bArr.sort()
cArr.sort()
cnt = 0

for i in aArr:
    s = bin_Search(bArr, i)
    if s == True:
        s1 = bin_Search(cArr, i)
        if s1 == True:
            cnt += 1


print(cnt)
