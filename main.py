'''
Moataz Khallaf
MultiDayBio
12/11/2018
'''
###imports
import string, csv, sys
###class
class syntaz(Exception("-")):
    pass
###vars
fil = 0
rows = []
data = []
informationList = [
    "Area of park",
    "Population year",
    "Survey Year",
    "Survey Month",
    "Survey Day",
    "Species name",
    "Unknown age and sex count",
    "Adult male count",
    "Adult female count",
    "Adult unknown count",
    "Yearling count",
    "Calf count",
    "Survey total",
    "Sightability correction factor",
    "Additional captive count",
    "Animals removed prior to survey",
    "Fall population estimate",
    "Survey comment",
    "Estimate method"
    ]
###inFucs
def menu():
    x = input('''
    Why here there stranger! Mighty fine day right? Only 500 degrees (C) partner.
    This here museum got data back to the fine days where we had plants and living animals.
    what would'ya like to do stranger?
    1) View the data
    2) Error 404 don't click or do I'm not ur boss
    3) Add some new data
    4) View growth over a set of years
    5) exit 
    ''')
    x = int(x)
    return x

def askYear():
    x = input("what year? ")
    return x

def askMam():
    x = input("what animal? (Deer/Bison/Elk/Moose) ")
    return x
###procFuncs
def read(a, b):
    a = open("data.csv", newline = "")
    b = csv.reader(fil)
    return b

def getNewInfo(informationList):
    a = []
    for i in range(len(informationList)):
        x = input(informationList[i])
        a.append(x)
    return a

def popChangeCalc(a,b,c,d,e,f):
    x = ((a + b) - (c + d)) / (e - f)
    return x
###outFuncs
###CodeStartsHere###
###in
answer = menu()
if answer == 3:
    newData = getNewInfo(informationList)


if answer == 4:
    year1 = askYear()
    print("2nd")
    year2 = askYear()
    mam = askMam()
###proc
fil = open("data.csv", newline = "")
data = csv.reader(fil)
for line in data:
    rows.append(line)

if answer == 3:
    rows.append(newData)
    fil = open("data.csv", "w", newline="")
    wrtieCSV = csv.writer(fil)
    for i in range(len(rows)):
        wrtieCSV.writerow(rows[i])

if answer == 4:
    for i in range(len(rows)):
        if mam == rows[i][5]:
            if year1 == rows[i][1]:
                if "South" == rows[i][0]:
                    southPop1 = rows[i][-3]
                    print("Check")
                    print(rows[i])
                else:
                    northPop1 = rows[i][-3]
                    print("Check")
                    print(rows[i])
    for i in range(len(rows)):
        if mam == rows[i][5]:
            if  year2 == rows[i][1]:
                if "South" == rows[i][0]:
                    southPop2 = rows[i][-3]
                    print(rows[i])
                else:
                    northPop2 = rows[i][-3]
                    print(rows[i])

    change = popChangeCalc(
    int(southPop1), int(northPop1),
    int(southPop2), int(northPop2),
    int(year1), int(year2)
    ) 

###out
if answer == 1:
    print(rows)
    print('''
    This here be the data, notice we used to have these things called elk, deer, bison and moose
    ''')

if answer == 2:
    raise syntaz()
if answer == 3:
    print("weird that you'd wanna do that but whatever. it's done.")


if answer == 4:
    print(southPop1,northPop1,southPop2,northPop2,year1,year2)
    print("the increase is", change, "mam/year")

print("goodbye partner")