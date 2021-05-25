def perfect(a):
    num=a
    i=1
    sum=0
    while i<a:
        if a%i==0:
            sum=sum+i
        i=i+1
    if num==sum:
        print(num,"it is perfect")
    else:
        print(num,"it is not perfect") 
n=int(input("enter the number "))         
perfect(n)             

    
    


