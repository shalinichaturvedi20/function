
def check_number_list(a,b):
    i=0
    while i<len(a):
        s=a[i]
        j=b[i]
        if s%2==0 and j%2==0:
            print("both are even")
        else:
            print("both are not even")
        i=i+1
a=[2, 6, 18, 10, 3, 75]
b=[6, 19, 24, 12, 3, 8]
check_number_list(a,b)





