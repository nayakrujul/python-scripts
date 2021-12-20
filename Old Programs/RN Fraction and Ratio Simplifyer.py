print("")
print("Welcome to RN Fraction and Ratio simplifier")
numer = raw_input("Enter your first number: ")
denom = raw_input("Enter your second number: ")
print("")
if(str.isdigit(str(numer)) and str.isdigit(str(denom))):
    factor = 1
    while(factor <= numer and factor <= denom):
        if(numer % factor == 0 and denom % factor == 0):
            divideBy = factor
        factor = factor + 1
    newNumer = int(numer) / divideBy
    newDenom = int(denom) / divideBy
    print("The fraction " + str(numer) + "/" + str(denom) + " can be simplified to " + str(newNumer) + "/" + str(newDenom))
    print("The ratio " + str(numer) + ":" + str(denom) + " can be simplified to " + str(newNumer) + ":" + str(newDenom))
else:
    print("Must be whole numbers")
print("")
