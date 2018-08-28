def main():
    total_income = []
    months = int(input("please enter the number of months: "))
    for month in range(1,months + 1):
        monthly_income = int(input("Enter income for month {}: ".format(month)))
        total_income.append(monthly_income)
    print_report(total_income)

def print_report(total_income):
    total = 0
    print("Income Report\n-------------")
    for month, monthly_income in enumerate(total_income):
        total += monthly_income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month+1,monthly_income,total))

main()
