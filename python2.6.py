a=59#int
b=45.66 #flaot
c=56+8j #complex
d="sumanth" #string
e="3883"
f,g="35.46","5+7j"
#Conversion of ithers to int
print(int(b)," ==> ",type(int(b)))
"""print(int(c)," ==> ",type(int(c))) # Value Error
we can't convefrt like this but we can seperate the following as below
"""
print(c.real," ==> ",type(c.real))
print(c.imag," ==> ",type(c.imag))
"""print(int(d)," ==> ",type(int(d))) # Value Error
We can't do this also
But when the string is pure NUMBER with out text thwn we can do this
This is only for Integers
"""
print(int(e)," ==> ",type(int(e)))

#converting strom others to float
print(float(a)," ==> ",type(float(a)))
print(float(f)," ==> ",type(float(f))) #ge is not possible because the sytring is in pure inteer form

#conversion of others to complex
print(complex(a)," ==> ",type(complex(a)))
print(complex(b)," ==> ",type(complex(b)))
print(complex(g)," ==> ",type(complex(g)))

# conversion to strings possible all ways

print(str(a)," ==> ",type(str(a)))
print(str(b)," ==> ",type(str(b)))
print(str(c)," ==> ",type(str(c)))


