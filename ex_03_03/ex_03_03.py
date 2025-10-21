while True:
    score = input("Enter Score:")
    try:
        scr = float(score)
     
        break
    except:
        print("Error, please enter nummeric input")

if scr >1.0:
    print ("Error, value out of range")
elif scr < 0.0:
    print ("Error, value out of range")
elif scr >= 0.9:
    print ("A")
elif scr >= 0.8:
    print ("B")
elif scr >= 0.7:
    print (C)
elif scr >= 0.6:
    print ("D")
elif scr < 0.6:
    print ("F")



