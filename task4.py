name1=input("ENTER THE NAME OF THE USER :")
units1=float(input(f"ENTER THE TOTAL UNITS CONSUMED BY {name1}: "))
print("-----------------------------------------------------------")
print("Bill for:",name1)
print("Units Consumed:",units1,"units")
print("-----------------------------------------------------------")
print("Detailed Slab Breakdown")

print("• 0-100 Units    : No charge (Free basic electricity)")
print("• 101-200 Units  : 5 per unit (only for units above 100)")
print("• Above 200 Units: 10 per unit (for all units beyond 200)")
print("-----------------------------------------------------------")
if units1< 0:
    print("Invalid input! Units cannot be negative.")
else:


    #  BILL CALCULATION 
    
    
  if units1 <= 100:
    bill = 0
  elif units1 <= 200:
    bill = (units1 - 100) * 5
  else:
    bill = (100 * 5) + (units1 - 200) * 10


if units1 > 200:
    discount = 0.10 * bill
    final_bill1 = bill - discount
else:
    discount = 0
    final_bill1 = bill
print(f"Bill Before Discount of {name1}  : ₹{bill:.2f}")

if discount > 0:
    print(f"Discount (10%)       : ₹{discount:.2f}")
    print(f"Bill After Discount  : ₹{final_bill1:.2f}")
else:
    print("Discount Applied      : None")
    print(f"Total Payable Amount : ₹{final_bill1:.2f}")


print("\n----- ELECTRICITY BILL -----")
print(f"Total Units Consumed by {name1}  : {units1}")
print(f"Total Bill Amount for {name1}  : {final_bill1}")
print("-----------------------------------------------------------")
print("" \
"")
print("***********************************************************")
print("" \
"")
print("-----------------------------------------------------------")

name2=input("ENTER THE NAME OF THE USER :")
units2=float(input(f"ENTER THE TOTAL UNITS CONSUMED BY {name2}: "))
print("-----------------------------------------------------------")
print("Bill for:",name2)
print("Units Consumed:",units2,"units")
print("-----------------------------------------------------------")
print("Detailed Slab Breakdown")

print("• 0-100 Units    : No charge (Free basic electricity)")
print("• 101-200 Units  : 5 per unit (only for units above 100)")
print("• Above 200 Units: 10 per unit (for all units beyond 200)")
print("-----------------------------------------------------------")
if units2 < 0:
    print("Invalid input! Units cannot be negative.")
else:


    #  BILL CALCULATION


  if units2 <= 100:
    bill = 0
  elif units2 <= 200:
    bill = (units2 - 100) * 5
  else:
    bill = (100 * 5) + (units2 - 200) * 10


if units2 > 200:
        discount = 0.10 * bill
        final_bill2 = bill - discount
else:
        discount = 0
        final_bill2 = bill
print(f"Bill Before Discount of {name2}  : ₹{bill:.2f}")

if discount > 0:
    print(f"Discount (10%)       : ₹{discount:.2f}")
    print(f"Bill After Discount  : ₹{final_bill2:.2f}")
else:
    print("Discount Applied      : None")
    print(f"Total Payable Amount : ₹{final_bill2:.2f}")


print("\n----- ELECTRICITY BILL -----")
print(f"Total Units Consumed by {name2}  : {units2}")
print(f"Total Bill Amount for {name2}  : {final_bill2}")

print("************************************************************")
if final_bill1 > final_bill2:
    percent_difference = ((final_bill1 - final_bill2) / final_bill2) * 100
    print(f"{name1} has a higher bill amount than {name2} by {percent_difference:.2f}%.")
elif final_bill1 < final_bill2:
    percent_difference = ((final_bill2 - final_bill1) / final_bill1) * 100
    print(f"{name2} has a higher bill amount than {name1} by {percent_difference:.2f}%.")
print("************************************************************")

input("\nPress Enter to exit...")