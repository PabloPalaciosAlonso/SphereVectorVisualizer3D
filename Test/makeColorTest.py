numberColors = 65
file = open("Colors.svv", "w")
for i in range(numberColors):
    file.write(str(3*(i%13))+" "+str(3*int(i/13))+" 0 1 "+str(i)+"\n")
file.close()
