n=int(input())
for i in range(n):
    r=int(input())
    if(r>37):
        a=r//5
        b=r%5
        if(b>2):
            r=(a+1)*5
            print(r)
        else:
            print(r)
    else:
        print(r)