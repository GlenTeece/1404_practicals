TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

# print("Electricity bill estimator")
# cents_per_kwh = float(input("Enter cents per kWh: "))
# daily_use_kwh = float(input("Enter daily use in kwh: "))
# billing_days = int(input("Enter number of billing days: "))
# total_cost = ((daily_use_kwh * billing_days)*cents_per_kwh)/100
# print("Estimated bill: ${:.2f}".format(total_cost))


print("Electricity bill estimator 2.0")
choice = input("Which Tariff? 11 or 31: ")
if choice == 11:
    cents_per_kwh = TARIFF_11
else:
    cents_per_kwh = TARIFF_31
daily_use_kwh = float(input("Enter daily use in kwh: "))
billing_days = int(input("Enter number of billing days: "))
total_cost = ((daily_use_kwh * billing_days)*cents_per_kwh)
print("Estimated bill: ${:.2f}".format(total_cost))