run1 = False

if run1:
    for year in range (158845, 158850):
        checkSum = 0
        passCheck = 318338237039211050000

        for x in range(1,year):
            checkSum += x
        checkResult = (passCheck - 1337) / (year ** 2)
        if (float(checkSum) == checkResult):
            print(year)

else:

    year = 158847
    passCheck = 1337
    checkSum = 0
    for x in range (1, year + 1):
        passCheck += year * x * year
    if passCheck < 318338237039211050000:
        print('increase')

##    year = 158848
##    checkSum = 0
##    passCheck = 318338237039211050000
##    for x in range(1,year):
##        checkSum += x
##    checkResult = (passCheck - 1337) / (year ** 2)
##    if (float(checkSum) > checkResult):
##        print ('reduce')