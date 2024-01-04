#User defined function
# ==> A reusable code 
#ex
#printing a trianle pattren
def triangle(num):
    k=num
    for i in range(1,k+1):

        print(" "*(k-1)+"*"*(2*i-1))
        k-=1
    print("\n\n")

def square(num):
    k=num
    for i in range (1,k+1):
        print("*"*((k)*2))


def rectangle(len,wid):
    for i in range(1,len+1):
        print("*"*wid)

k=int(input("Enter the no.of lines of polygons you want to print: "))
triangle(k)
square(k)
print("\n\n")
len1=input("Enter lenth and width of the Rectangle with comma seperated : ")
lis=len1.split(",")
print(lis)
l,w=lis
rectangle(int(l),int(w))