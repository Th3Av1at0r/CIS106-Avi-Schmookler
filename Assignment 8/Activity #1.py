def displayresult(value, expressions):
    incrament = 1
    count = 1
    while count <= expressions:
        solution = value * count
        print(str(value) + " * " + str(count) + " = " + str(solution))
        count = count + incrament

def getexpressions():
    print("How many expressions?")
    expressions = int(input())
    
    return expressions

def getvalue():
    print("what is your value?")
    value = int(input())
    
    return value

# Main
# This program takes a value and a number of expressions and produces the number of expressions using the value
value = getvalue()
expressions = getexpressions()
displayresult(value, expressions)
