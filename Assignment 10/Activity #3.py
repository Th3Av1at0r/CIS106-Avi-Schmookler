def calculateFirstPi(oddOrEven, firstPi, number):
    if oddOrEven != 0:
        firstPi = firstPi + float(4) / (number * (number + 1) * (number + 2))
    else:
        firstPi = firstPi - float(4) / (number * (number + 1) * (number + 2))
    
    return firstPi

def displayResults(finalPi):
    print("The final iteration of Pi for your number of runs is " + str(finalPi))

def getFinalPi(seriesNumber):
    count = 1
    number = 2
    firstPi = 3
    while count <= seriesNumber:
        oddOrEven = count % 2
        firstPi = calculateFirstPi(oddOrEven, firstPi, number)
        print(str(count) + " - " + str(firstPi))
        count = count + 1
        number = number + 2
    finalPi = firstPi
    
    return finalPi

def getSeriesNumber():
    print("How many times do you want to run the series?")
    seriesNumber = int(input())
    
    return seriesNumber

# Main
# This Program calculates Pi through the Nilakantha series
seriesNumber = getSeriesNumber()
finalPi = getFinalPi(seriesNumber)
displayResults(finalPi)
