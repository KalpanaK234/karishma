# karishma
#Program to find Amount of Electric Bill consumed 
a = int(input("Enter the units consumed:"))
if (a<=50):
    b=a*0.5
elif (a<=150):
    b=a*0.75
elif (a<=250):
    b=a*1.20
else:
    b=a*2.0
c=b*0.4
d=b+c
print("Total Amount of Electricity bill consumed is:",d)
    
