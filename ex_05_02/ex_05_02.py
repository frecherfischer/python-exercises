tot = 0.0
num = 0
maxN = None
minN = None
while True:
    Number = input("Enter Number")
    if Number == "done":
        break
    try: 
        fnumber = float(Number)
        tot = tot + fnumber
        num = num + 1
    except: 
        print ("Invalid input")
    
    if maxN is None:
        maxN = fnumber
    elif fnumber > maxN:
        maxN = fnumber
    if minN is None:
        minN = fnumber
    elif fnumber < minN:
        minN = fnumber
print ("Maximum",maxN,"Minumum",minN)
#alternative mit Ergebnissen
# print ("Summe:",tot,"Eingaben:",num, "Durchschnitt:",tot/num, "min",minN, "max",maxN)
    