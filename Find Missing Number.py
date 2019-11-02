print("")
def missing_number(num_list):
    return sum(range(num_list[0], num_list[-1]+1)) - sum(num_list)
ext = 0
numNo = 1
numList = []
while(ext == 0):
    num = input("Number " + str(numNo) + " in list: ")
    if(str.isdigit(str(num))):
        smallList = [num]
        numList = numList + smallList
        numNo = numNo + 1
    elif(num == ""):
        ext = 1
    else:
        print("Must be a number.")
print(missing_number(numList))
