a=int(input("enter a number:"))
b=int(input("enter a number:"))

print("entr + for addtion")
print("entr - for subraction")
print("entr * for multiplication")
print("entr / for division")
print("entr ^ for Exponentiation ")
print("entr // for floor division")
print("entr %  for floor division")

c=str(input("enter the operation:"))



if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
elif c=="^":
    print(a**b)
elif c=="//":
    print(a//b)
elif c=="%":
    print(a%b)
else:
    print("cannot run this operation")

