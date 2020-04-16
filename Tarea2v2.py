import csv
import os

with open("02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    
    header = next(csvreader)
    
    #Variables
    i = 0
    kVoteCount = 0
    cVoteCount = 0
    liVoteCount = 0
    otooleyVoteCount = 0   
    newList = []

    for row in csvreader:
        i = i+1
        if row[0] not in newList:
            newList.append(row[0])
            if row[2] == "Khan":
                kVoteCount = kVoteCount + 1
            elif row[2] == "Correy":
                cVoteCount = cVoteCount + 1
            elif row[2] == "Li":
                liVoteCount = liVoteCount + 1
            elif row [2] == "O'Tooley":
                otooleyVoteCount = otooleyVoteCount + 1


    #for row in csvreader:
        #i = i+1    
        #if row not in newList:
            #newList.append(row)

#newList.pop(0)
#print(newList)
#totalVotos = len(newList)
#print(totalVotos)



#for i in range(len(newList)):
#    if newList[i][2] == "Khan":
#        kVoteCount = kVoteCount + 1
#    elif newList [i][2] == "Correy":
#        cVoteCount = cVoteCount + 1
#    elif newList [i][2] == "Li":
#        liVoteCount = liVoteCount + 1
#    elif newList [i][2] == "O'Tooley":
#        otooleyVoteCount = otooleyVoteCount + 1
    #print(kVoteCount)
    #print(cVoteCount)
    #print(liVoteCount)
    #print(otooleyVoteCount)

totalVotos = kVoteCount + cVoteCount + liVoteCount + otooleyVoteCount
porcVKan = (kVoteCount / totalVotos) * 100
porcVCo = ( cVoteCount / totalVotos) * 100
porcVli = ( liVoteCount / totalVotos) * 100
porcVOt = ( otooleyVoteCount / totalVotos) * 100

    #print(porcVKan)
    #print(porcVCo)
    #print(porcVli)
    #print(porcVOt)

#Ganador del Electorado
    #totalPorcentagesYGanadores = {"Khanssssssssssssssss":porcVKan,"Correy":porcVCo,"Li":porcVli,"O'Tooley":porcVOt}
    #totalPorcentagesYGanadores = {
    #    "Khanssssssssssssssss":porcVKan,
    #    "Correy":porcVCo,
    #    "Li":porcVli,
    #    "O'Tooley":porcVOt
    #}
    
totalPorcentagesYGanadores = [porcVKan,porcVCo,porcVli,porcVOt]
ganador = ["Kahn","Correy","Li","O'Tooley"]

#posMax = totalPorcentagesYGanadores.index(max(totalPorcentagesYGanadores)
votMaxima = float(max(totalPorcentagesYGanadores))
#print(votMaxima)
posMaxima = totalPorcentagesYGanadores.index(float(max(totalPorcentagesYGanadores)))
#print(posMaxima)
    
nombreGanador = ganador[posMaxima]
#print(nombreGanador)




 # posMin = listaCambio.index(min(listaCambio))
 #minimoCambio = min(listaCambio)

#Output Final - Tarea
print("")
print("Elections Results")
print("-----------------------")
print(f"Total Votes: {totalVotos}")
print("-----------------------")
print(f"Khan: {porcVKan} ({kVoteCount})")
print(f"Correy: {porcVCo} ({cVoteCount})")
print(f"Li: {porcVli} ({liVoteCount})")
print(f"O'Tooley: {porcVOt} ({otooleyVoteCount})")
print("-----------------------")
print(f"Winner: {nombreGanador}")
print("-----------------------")
