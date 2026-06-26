# Constant time
a=[10,20,30,40,50]
print(a[2])

# Linear time
a=[1,2,3,4,5,6,6,67,7,71,72,4]
for i in a:
    print(i)

# Quadratic time
for i in range(3):
    for j in range(3):
        print(i,j)


a=int(input("Enter the number: "))
for i in range(a+1):
    p=1
    for i in range(i):
        print(p,end="")
        p+=1
    print("")

