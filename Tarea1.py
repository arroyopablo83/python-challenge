import csv
import os

outpath = os.path.join("limpiezaDeBaseT1.csv")

with open("02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    newlist = []

    for row in csvreader:
        if row not in newlist:
            if len(row)>1:
                newlist.append(row)

    newlist.pop(0)
    #print(newlist)
    
    totalMonths = int(len(newlist))
    #print(totalMonths)

    totalgeneral = 0
    for i in range(len(newlist)):
        totalgeneral = totalgeneral + float(newlist[i][1])
    
    #print(totalgeneral)

    listaCambio = []

    for i in range(1,len(newlist)):
        cambio = float(newlist[i][1]) - float(newlist[i-1][1])
        listaCambio.append(cambio)

    #print(listaCambio)

    sumaDeCambio = 0
    for i in range(len(listaCambio)):
        sumaDeCambio = sumaDeCambio + float(listaCambio[i])

    #print(sumaDeCambio)
    
    cambioPromedio = sumaDeCambio / len(listaCambio)
    #print(cambioPromedio)

    #Calulo de los valores max y min dentro de la tabla de cambios
    maximoCambio = max(listaCambio)
    minimoCambio = min(listaCambio)
    
    #Calculo de la posicion de cada uno de los valores mx  y min dentro de la tabla de cambios
    posMax = listaCambio.index(max(listaCambio))
    posMin = listaCambio.index(min(listaCambio))

    fechaMax = newlist[posMax+1][0]
    #print(fechaMax)
    fechaMin = newlist[posMin+1][0]
    #print(fechaMin)
    
    #Mensaje Final
    print("")
    print("Financial Analysis")
    print("")
    print("-----------------------------------")
    print("")
    print(f"Total Months: {totalMonths}")
    print(f"Total: {totalgeneral}")
    print(f"Average Change: {cambioPromedio}")
    print(f"Greatest Change in Profits: {fechaMax} & (${maximoCambio})")
    print(f"Greatest Decrease in Profit: {fechaMin} & (${minimoCambio})")

    #print(newlist)
#    with open(outpath, "w") as csvfile2:
#        csvwriter = csv.writer(csvfile2,delimiter=",")
#        csvwriter.writerows(newlist)

#with open("limpiezaDeBaseT1.csv") as csvfile:
#    csvreader = csv.reader(csvfile,delimiter=",")

#    print(next(csvreader))
