

print("WELCOME TO INTELLIGENT BILLING SYSTEM WITH CONSUMPTION")


#input user details


name=input("ENTER THE NAME OF THE USER :")
units=float(input(f"ENTER THE TOTAL UNITS CONSUMED BY {name}: "))


print("-----------------------------------------------------------")


#  HEADER


print("Bill for:",name)
print("Units Consumed:",units,"units")
print("-----------------------------------------------------------")


#  SLAB DETAILS


print("Detailed Slab Breakdown")

print("• 0-100 Units    : No charge (Free basic electricity)")
print("• 101-200 Units  : 5 per unit (only for units above 100)")
print("• Above 200 Units: 10 per unit (for all units beyond 200)")
if units < 0:
    print("Invalid input! Units cannot be negative.")
else:


    #  BILL CALCULATION 
    
    
    if units <= 100:
        bill = 0
    elif units <= 200:
        bill = (units - 100) * 5
    else:
        bill = (100 * 5) + (units - 200) * 10

print(f'Bill of {name}  : ₹{bill:.2f}')

input("\nPress Enter to exit...")