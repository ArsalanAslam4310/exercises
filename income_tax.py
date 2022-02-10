amount = 45000
tax = 0

if amount <= 10000:
    tax = 0

elif amount <= 20000:
    x = amount - 10000
    tax= x*10/100
else:
    tax = 0
    tax = 10000*10/100
    tax = tax+ (amount-20000)*20/100
print(int(tax))
