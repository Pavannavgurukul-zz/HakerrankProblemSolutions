a=input().split(" ")
b=input().split(" ")
A=0
B=0
for i in range(len(a)):
    num1=int(a[i])
    num2=int(b[i])
    if(num1>num2):
        A+=1
    elif(num1<num2):
        B+=1
print(A, B)

