import sys

cpe = (sys.argv[1:])
cpeArray = ''.join(cpe).split(":")


if (len(cpeArray)!= 13):
    raise ValueError('Niepoprawny ciąg CPE 2.3')

for n in range(0,len(cpeArray)-7):
    if cpeArray[n+7]=="*":
        cpeArray[n+7]="ANY"
    if cpeArray[n+7]=="-":
        cpeArray[n+7]="NA"

cpeDict = {
    "part":cpeArray[2],
    "vendor":cpeArray[3],
    "product":cpeArray[4],
    "version":cpeArray[5],
    "update":cpeArray[6],
    "edition":cpeArray[7],
    "language":cpeArray[8],
    "sw_edition":cpeArray[9],
    "target_sw":cpeArray[10],
    "target_hw":cpeArray[11],
    "other":cpeArray[12],
}




print (cpeDict)