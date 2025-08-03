#Right angled triangle
print("Half pyramid pattern of stars(*):")
n=int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(i+1):
        print("* ",end="")
    print()

#ACTIVITY 2

rows=int(input("Enter the number of rows: "))
n=1

print("Floyd's triangle:")

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(n,end=" ")
        n=n+1
    print()

#ACTIVITY 3

rowsize=int(input("Enter the number of rows: "))
if rowsize%2==0:
    halfdiamrow=int(rowsize/2)
else:
    halfdiamrow=int(rowsize/2)+1

space=halfdiamrow-1

for i in range(1,halfdiamrow+1):
    for j in range(1,space+1):
        print(end=" ")
    space=space-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
        num=num+1
    print()
space=1
#lower triangle
for i in range(1,halfdiamrow):
    for j in range(1,space+1):
        print(end=" ")
    space=space+1
    num=1
    for j in range(1,2*(halfdiamrow-i)):
        print(end=str(num))
        num=num+1
    print()
