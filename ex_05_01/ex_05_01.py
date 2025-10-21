tot = 0.0
num = 0
while True:
    Number = input("Enter Number")
    if Number == "done":
        break
    try: 
        fnumber = float(Number)
        tot = tot + fnumber
        num = num + 1
    except: 
        print ("keine Zahl")
    
print ("Summe:",tot,"Eingaben:",num, "Durchschnitt:", tot/num)
    
    