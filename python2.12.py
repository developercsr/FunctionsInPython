#default parametrs
def main():
    #Lets tahke the exampke o calcularing reactangle
    l=input("Enter the length and width for the reactangle seperated with commas : ")
    length,width=(l.split(","))
    rectangle(int(length),int(width))
    rectangle1(int(length))
    rectangle1(int(length),int(width))
    # Here we passe only one element but there is no Error 
    #Because we already have an default value of width=1 there
    #If we given a width tehn it will consider that argument else this will just use deafult value

def rectangle1(length,width=1):#This is having with the deafault parameter width as 1
    print("The area of the rectangle is ",length*width)
def rectangle(length,width):
    print("The area of the recatngle is ",length*width)
if __name__=="__main__":
    main()

