import random

OCUPATIONES = {}
occupashuns = open("data/occupations.csv", "rU")
occupashuns.readline()
for line in occupashuns:
    if line[0] == "\"":
        #"how obfuscated can i make this next line..."
        # - me half an hour earlier
        #sorry mr. dw
        OCUPATIONES[line[1:line.find("\"", 1, (len(line) + 1))].strip("\n")] = [line[line.find(",", line.find("\"", 1, (len(line) + 1)), (len(line))) + 1:line.find(",", line.find(",", line.find("\"", 1, (len(line) + 1)), (len(line))) + 1, len(line))].strip("\n"), line[line.find("http", line.find(",", line.find(",", line.find("\"", 1, (len(line) + 1)), (len(line))) + 1, len(line)), len(line)):len(line)] ]
    else:
        x = line.split(",")
        OCUPATIONES[x[0].strip("\n")] = [x[1].strip("\n"), x[2].strip("\n")]
        
    newoccdict = OCUPATIONES

def getOccuDict():
    return OCUPATIONES.items()

def getRandOccu(x):
    return [newoccdict.keys()[x], newoccdict.values()[x][0], newoccdict.values()[x][1]]

occupashuns.close()
