print("")
filename = input("Filename: ")
ext = 0
while(ext == 0):
    line = input("")
    if(line == ""):
        ext = 1
    else:
        with open("RN_Word" + filename + ".txt", "w") as f:
            f.write(line + "\n")
