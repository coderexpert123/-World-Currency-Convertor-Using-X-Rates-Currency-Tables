with open('currencyData') as f:
    lines=f.readlines()
currencyDict={}
for line in lines:
    paredes=line.split("\t")
    currencyDict[paredes[0]]=paredes[1]


print(currencyDict)
amount=int(input("Enter the AMount :  "))
print("Choose  the Name of Currency that you want to convert above  amount :  \n ")
[print(item) for item in currencyDict.keys()]


currency=input("Plese choose the currecy from  Above :  \n")
print(f"{amount} INR is equal to {amount * float(currencyDict[currency])}  {currency}")
