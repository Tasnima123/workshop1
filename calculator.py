import os

duplicate=[]

with open("step3.txt", "r") as f:
    while True:
        line = f.readline()
        y = line.split()
        if (len(y)==5):
            paramA = int(y[3])
            paramB = int(y[4])
            if (y[2]=="+"):
                value = int(paramA + paramB)
            elif (y[2]=="x"):
                value = int(paramA * paramB)
            elif (y[2]=="-"):
                value = int(paramA - paramB)
            else:
                value = int(paramA / paramB)
        else:
            value = y[1]
            print(value)
        
        if (value in duplicate):
            break
        else:
            duplicate.append(value)
            line = f.readlines(value)

print(line)
f.close()









