name=input("ENTER THE NAME OF THE USER :")
units=float(input(f"ENTER THE TOTAL UNITS CONSUMED BY {name}: "))
print("-----------------------------------------------------------")
print("Bill for:",name)
print("Units Consumed:",units,"units")
print("-----------------------------------------------------------")
  #  BILL CALCULATION 
    
    
if units <= 100:
    bill = 0
elif units <= 200:
    bill = (units - 100) * 5
else:
    bill = (100 * 5) + (units - 200) * 10

if units > 200:
    discount = 0.10 * bill
    final_bill = bill - discount
else:
    discount = 0
    final_bill = bill

print(f"Bill Before Discount of {name}  : ₹{bill:.2f}")

if discount > 0:
    print(f"Discount (10%)       : ₹{discount:.2f}")
    print(f"Bill After Discount  : ₹{final_bill:.2f}")
else:
    print("Discount Applied      : None")
    print(f"Total Payable Amount : ₹{final_bill:.2f}")


print("\n----- ELECTRICITY BILL -----")
print(f"Total Units Consumed by {name}  : {units}")
print(f"Total Bill Amount for {name}  : {final_bill}")

input("\nPress Enter to exit...")