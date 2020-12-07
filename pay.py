def computepay(h,r):
    if h > 40:
        h_above = h-40
        h = 40
        r_new = 1.5*r
        first = h*r
        second = h_above*r_new
        pay = first + second
    else:
        pay = h*r
    return pay

hrs = input("Enter Hours: ")
hrs = float(hrs)
rate = input("Enter Rate: ")
rate = float(rate)
p = computepay(hrs,rate)
print("Pay",p)
