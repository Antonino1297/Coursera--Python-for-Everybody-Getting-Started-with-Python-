hrs = input("Enter Hours: ")
h = float(hrs)
rte = input("Enter Rate: ")
r = float(rte)

if h > 40:
    reg = h * r
    otp = (h - 40.0) * (r * 0.5)
    xp = reg + otp
else:
    xp = h * r

print(xp)