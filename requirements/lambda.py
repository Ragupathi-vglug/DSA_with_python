# lambda argument:expresssion
square=lambda a:a*a
print(square(5))

# Using two arguments
n=lambda a,b:a+b
print(n(10,10))

# Maximum
num=lambda x,y:x if x>y else y
print(num(100,20))

students=[("Ragu",90),("pathi",80),("chelsie",99)]
print("Before ",students)
students.sort(key=lambda x:x[1])
print("After :",students)

