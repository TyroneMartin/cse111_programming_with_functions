from datetime import datetime

# Call the now() method to get the current date and time as a datetime object
current_date_and_time = datetime.now(tz=None)

# Get the day of the week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()
# mondays = 0, tuesdays = 1, wednesdays = 2, thursdays = 3, fridays = 4, saturdays = 5, sundays = 6
discount_rate = 0.10
sales_tax_rate = 0.06
total = 0
subtotal = float(input("Enter the subtotal: "))
sales_tax_amount = float(input("Sales tax amount: "))

if subtotal >= 50 and (day_of_week == 2 or day_of_week == 3):
    discount = subtotal * discount_rate
    sales_taxes = sales_tax_amount * sales_tax_rate
    # total = (subtotal + sales_tax_amount) - discount
    total = (subtotal +  sales_taxes) - discount

    print(f" The discount price is {total:.2f}")
else:
    discount = 0
    # total = (subtotal + sales_tax_amount) - discount
    sales_taxes = sales_tax_amount * sales_tax_rate
    total = (subtotal +  sales_taxes) - discount
    print(f" The total price is {total:.2f}")