check = float(input("Enter total bill amount:"))
service = input("What was the level of service? Enter 'good', 'fair', or 'bad':")
service = str(service.lower())

def tip_calc(val1):
    tip = val1 * check
    total = check + tip
    print("Tip amount: $%.2f" % tip)
    print("Total amount: $%.2f" % total)

if service == 'good':
    tip_calc(.2)
elif service == 'fair':
    tip_calc(.15)
else:
    tip_calc(.1)