#print_function
print("hari om")
print(2,3,4,4.5,6+6j)#no need of quotations for printing numbers,floating points and complex 
a,b,c=22,2.6,5+6j
k="sumanth"
print(a,b,c)
print("namste",a,"is an Integer")
print(a+b)#auto conversion to float
print("namste",k,"age is",a)  #==> Normal Processes
print("namste "+k+" age is "+str(a)) # ==>String concatination
print(f"namste {k} age is {a}")  #==> UsingS-Strings
print("namste {} age is {}".format(k,a)) #Formating
print("namste %s age is %d"%(k,a)) #Old %-operator method