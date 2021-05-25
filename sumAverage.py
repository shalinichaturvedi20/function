# def sum_average(a,b,c):
#     d=(a+b+c)
#     e=d/3
#     print(d,"sum")
#     print(e,"average")
# a=int(input("enter the number"))
# b=int(input("enter the number"))
# c=int(input("enter the number"))
# sum_average(a,b,c)    


        

# a="Amisha"
# def name():
#     a="shalini"
#     print(a)
# name()
# print(a) 




def show_number(a):
    limit=0
    while limit<=a:
        if a%2==0:
            print(limit,"even")
        else:
            print(limit,"odd") 
        limit+=1 
number=int(input("enter the number: "))      
show_number(number)           
