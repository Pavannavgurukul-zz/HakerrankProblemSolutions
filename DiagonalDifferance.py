#Program to find the diffrence of a squer metrics digonals.
n = int(input())
arr = []
def digonal(arr):
    a=0
    b=0
    for i in range(len(arr)):
        a+=arr[i][i]
        b+=arr[i][(len(arr)-1)-i]
    print(abs(a-b))
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
digonal(arr)

