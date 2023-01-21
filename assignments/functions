def computepay(h, r):
    pay = 40 * r
    if h > 40:
        ot_rate = 1.5 * r
        ot_pay = ot_rate * (h-40)
        final = ot_pay + pay
        return(final)
    else: 
        return(pay)
        
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
p = computepay(h, r)
print("Pay", p)
