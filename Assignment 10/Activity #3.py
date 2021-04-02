def displayResults(finalPi):
    print("The final iteration of Pi for your number of runs is " + str(finalPi))

def getFinalPi(seriesNumber):
    count = 1
    i = 2
    firstPi = 3
    while count <= seriesNumber:
        oddOrEven = count % 2
        if oddOrEven != 0:
            firstPi = firstPi + float(4) / (i * (i + 1) * (i + 2))
        else:
            firstPi = firstPi - float(4) / (i * (i + 1) * (i + 2))
        print(str(count) + " - " + str(firstPi))
        count = count + 1
        i = i + 2
    finalPi = firstPi
    
    return finalPi

def getSeriesNumber():
    print("How many times do you want to run the series?")
    seriesNumber = int(input())
    
    return seriesNumber

# Main
seriesNumber = getSeriesNumber()
finalPi = getFinalPi(seriesNumber)
displayResults(finalPi)
