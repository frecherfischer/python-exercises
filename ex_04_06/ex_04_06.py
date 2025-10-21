def computepay(h, r):
    if h <= 40:
        gp = h * r
    else:
        gp = (40 * r) + ((h - 40) * (r * 1.5))
    return gp

while True: 
    hrs = input("Enter Hours")
    rate = input("Enter Rate")
    try: 
        h = float(hrs)
        r = float(rate)
        break
    except:
        print("Error, please enter nummeric input")

p = computepay(h, r)
print("Pay", p)