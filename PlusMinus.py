def sort(arr):
    a=0
    b=0
    c=0
    for i in arr:
        if(i>0):
            a+=1
        elif(i<0):
            b+=1
        else:
            c+=1
    print(str.format('{0:.6f}',(a/len(arr))))
    print(str.format('{0:.6f}',(b/len(arr))))
    print(str.format('{0:.6f}',(c/len(arr))))
n = int(input())
arr= list(map(int, input().rstrip().split()))
sort(arr)

