def countA(a):
    numA = 0
    for i in range(0, len(a)):
        if a[i] == "a":
            numA = numA + 1
    print("There are " + str(numA) + " a's in the word " + a)