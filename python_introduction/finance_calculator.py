monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

Monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are: ${Monthly_savings}")

interest = 0.05
projected_savings = Monthly_savings * 12 + (Monthly_savings * 12 * interest)

print(f"Projected savings after one year, with interest, is: ${projected_savings}")
