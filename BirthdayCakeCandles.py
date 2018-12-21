n=input()
arr= list(map(int, input().rstrip().split()))
a=(max(arr))
count=0
for i in arr:
    if(i==a):
        count+=1
print(count)