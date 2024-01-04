import math
def main():
    print("1.square"," "*7,"2.Recatngle"," "*7,"3.Traingle")
    print("4.circle"," "*7,"5.semicircle"," "*7,"6.Nothing")    
    num = int(input("select the polygon to which you would like to find area"))
    selection(num)

def selection(k):
    if k==1:
        square()
    if k==2:
        rect()
    if k==3:
        tri()
    if k==4:
        cir()
    if k==5:
        semi()
    if k==6:
        print("You are selected to exit this program")
        exit()

def square():
    side=int(input("Enter The side of the square : "))
    print("Area Of The Square is ",side*side ,"sq.units")
def rect():
    l=input("Enter the length and width of the rectangle seperated with commas : " )
    length,width=l.split(",")
    print("Area of the rectangle is ",int(length)*int(width)," sq.units")

def tri():
    l=input("Enter the hight and base of the triangle seperated with commas : " )
    height,base=l.split(",")
    print("Area of the rectangle is ",(int(height)*int(base))/2," sq.units")
def cir():
    l=float(input("Enter the radius of the circle : " ))
    print("Area of the circle is ",math.pi*l*l," sq.units")
def semi():
    l=float(input("Enter the radius of the semi circle : " ))
    print("Area of the semi circle is ",(math.pi*l*l)/2," sq.units")
if __name__== "__main__":
    main()