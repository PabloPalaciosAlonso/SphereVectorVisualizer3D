numberColors = 64
file = open("TestColors.svv", "w")
for i in range(numberColors):
    file.write(str(3*i)+"0 0 1 "+str(i)+"\n")
file.close()
