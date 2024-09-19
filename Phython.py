# This function prompts the user for a valid float input and handles errors.
def get_valid_float(prompt: str, error_message: str, positive_only: bool = True):
    while True:  # This loop will keep running until a valid input is received.
        try:
            # Ask the user to input a value and try to convert it to a float.
            value = float(input(prompt))
            
            # If the value should only be positive, check if it is greater than 0.
            if positive_only and value <= 0:
                # If the value is not positive, print the error message and ask again.
                print(error_message)
            else:
                # If the value is valid, return it and exit the loop.
                return value
        except ValueError:
            # If the input is not a number, print this message and ask again.
            print('Invalid Input. Please Enter a Number.')

# This function calculates financial details based on the provided inputs.
def calculate_finances(monthly_income: float, tax_rate: float, monthly_expenses: float, currency: str) -> None:
    # Calculate yearly expenses by multiplying monthly expenses by 12 (months in a year).
    yearly_expenses: float = monthly_expenses * 12
    
    # Calculate yearly income by multiplying monthly income by 12.
    yearly_income: float = monthly_income * 12
    
    # Calculate monthly tax by applying the tax rate to the monthly income.
    monthly_tax: float = monthly_income * (tax_rate / 100)
    
    # Calculate yearly tax by multiplying the monthly tax by 12.
    yearly_tax: float = monthly_tax * 12
    
    # Calculate the monthly net income after subtracting taxes and expenses.
    monthly_net_income: float = monthly_income - monthly_tax - monthly_expenses
    
    # Calculate the yearly net income after subtracting yearly taxes and expenses.
    yearly_net_income: float = yearly_income - yearly_tax - yearly_expenses

    # Print the financial details with formatted output.
    print('-----------')
    print(f'Monthly Income : {currency}{monthly_income:,.2f}')  # Display monthly income with 2 decimal places.
    print(f'Tax Rate : {tax_rate:,.0f}%')  # Display tax rate as a percentage with no decimal places.
    print(f'Yearly Income : {currency}{yearly_income:,.2f}')  # Display yearly income.
    print(f'Yearly Net Income : {currency}{yearly_net_income:,.2f}')  # Display yearly net income.
    print(f'Monthly Net Income : {currency}{monthly_net_income:,.2f}')  # Display monthly net income.
    print(f'Monthly Tax Paid : {currency}{monthly_tax:,.2f}')  # Display the amount of tax paid monthly.
    print(f'Yearly Tax Paid : {currency}{yearly_tax:,.2f}')  # Display the amount of tax paid yearly.
    print(f'Monthly Expenses : {currency}{monthly_expenses:,.2f}')  # Display monthly expenses.
    print(f'Yearly Expenses : {currency}{yearly_expenses:,.2f}')  # Display yearly expenses.
    print('-------------')

# The main function collects user inputs and calculates finances.
def main() -> None:
    # Get the user's monthly income (must be a positive float).
    monthly_income = get_valid_float("Please Enter Your Monthly Salary: $", "Monthly income must be positive.")
    
    # Get the user's tax rate (can be any float, including negative for tax rebates).
    tax_rate = get_valid_float('Please Enter Your Tax Rate(%): ', 'Tax Rate Must Be a Positive Number.', positive_only=False)
    
    # Get the user's rent payment (must be a positive float).
    rent = get_valid_float('Please Enter Your Rent Payment: $', 'This Input Must Be a Positive Number.')
    
    # Get the user's food costs (must be a positive float).
    food = get_valid_float('Please Enter Your Food Cost: $', 'Please Enter a Number.')
    
    # Get the user's gym membership fee (must be a positive float).
    gym_membership = get_valid_float('Please Enter Gym Membership Fee: $', 'This Input Must Be a Positive Number.')
    
    # Add up all the monthly expenses (rent + food + gym membership).
    monthly_expenses = rent + food + gym_membership
    
    # Call the calculate_finances function to display the results.
    calculate_finances(monthly_income, tax_rate, monthly_expenses, currency='$')

# This ensures the script runs only when executed directly, not when imported.
if __name__ == '__main__':
    main()