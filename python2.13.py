#asssert statement : Assert statemenst is used fot vheckin the logical expression true or false
#If it is true then only the proram proceeds if false then it will give an AssertionError
#This is used in exception handling
def main():
    a=int(input("Enter a number : "))
    try:
        assert a%2==0
        print(a," is an even number")
    except:
        AssertionError()
def AssertionError():
    print("The number you have entered is an odd number thats why the assertion is failed")
    print("Please Enter an Even Number")
    
if __name__ == "__main__":
    main()