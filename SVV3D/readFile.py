def stof(lista):
     Lista2=[]
     for elem in lista:
          Lista2+=[float(elem)]
     return Lista2

def readAllFrames(name):
     filein = open(name,"r")
     lines = []
     col = []
     count = 0
     for line in filein:
          if line[0]=="#":
               if count>0:
                    lines+=[col]
                    col = []
          else:
               col+=[stof(line.strip().split(' '))]
               count+=1
     return lines
