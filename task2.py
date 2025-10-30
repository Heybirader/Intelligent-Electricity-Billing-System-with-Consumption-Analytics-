#task 2
name=input("ENTER THE NAME OF THE USER :")
units=float(input(f"ENTER THE TOTAL UNITS CONSUMED BY {name}: "))
print("-----------------------------------------------------------")
print("Bill for:",name)
print("Units Consumed:",units,"units")
print("-----------------------------------------------------------")
if units <= 150:
        print("Low Consumption - Eco-Friendly User")
elif units <= 200:
        print("Average Consumption - Moderate User")
else:
        print("HIGH CONSUMPTION - ENERGY EFFICIENCY ALERT!")

input("\nPress Enter to exit...")