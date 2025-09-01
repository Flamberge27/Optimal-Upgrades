## Start stuff to change

fileName="UP_SCANX"

nameDict = {
    "R:": "Radius",
    "A:": "Fauna",
    "P:": "Flora"
}

## End stuff to change

baseFile = open(fileName+"_RESULT.txt","r")
fullLines = baseFile.readlines()

outFile = open("NEW_"+fileName+".csv","a")

outString = "Seed,Name"
for key in nameDict.keys():
    outString += "," + nameDict[key]

outFile.write(outString)

for line in fullLines:
    pieces=line.split("\t")
    
    outString = "\n"

    outString += pieces[0] + "," # first piece is seed
    outString += (pieces[-1])[:-1] # second piece is name

    stat = 1 # which stat we're looking at
    for key in nameDict.keys():
        outString += ","
        if key in pieces[stat]:
            outString += (pieces[stat])[2:]
            stat += 1

    outFile.write(outString)
