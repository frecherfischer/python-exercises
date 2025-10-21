while True:
    hrs = input("Enter Hours:")
    rate = input("Enter Rate:")
    try:
        h = float(hrs)
        r = float(rate)
        break
    except:
        print("Error, please enter nummeric input")
if h <= 40:
    gp = h * r
    print(gp)
else:
    gp = (40 * r) + ((h - 40) * (r * 1.5))
    print(gp)


