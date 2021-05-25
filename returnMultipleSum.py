def number(a):
    limit=1
    sum=0
    while limit<=m:
        if limit%3==0 or limit%5==0:
            print(limit)
            sum=sum+limit
        limit=limit+1
    return(sum)
m=int(input("enter the number")) 
s=number(m)   
print(s)   