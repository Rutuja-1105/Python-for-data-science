def add(A,B):
    "Above function adds two numbers"
    return A+B 
def sub(A,B):
    "Functions substracts two numbers"
    return A-B
def multi(A,B):
    "Function multiply  two numbers"
    return A*B
def div(A,B):
    "Function divide two numbers"
    return A/B

print("select operation")
print("i.add")
print("ii.sub")
print("iii.multi")
print("iv.div")

choice=input("Enter choice(i/ii/iii/iv):")

n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))

if choice == 'i':
    print(n1,"+",n2,"=",add(n1,n2))

elif choice == 'ii':
    print(n1,"-",n2,"=",sub(n1,n2))

elif choice == 'iii':
    print(n1,"*",n2,"=",multi(n1,n2))

elif choice == 'iv':
    print(n1,"/",n2,"=",div(n1,n2))
    
else:
    print("invalid input")

