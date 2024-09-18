def get_valid_float(promt: str, error_message: str, positive_only: bool =True):
  while True:
    try:
      value = float(input(promt))
      if positive_only and value <=0:
        print(error_message)
      else: return value
    except ValueError:
      print('Invalid Input. Please Enter a Number.')
        
def calculate_finances(monthly_income : float, tax_rate : float, monthly_expenses : float, currency : str) -> None:
    yearly_expenses : float = monthly_expenses * 12
    yearly_income : float = monthly_income * 12
    monthly_tax : float = monthly_income * (tax_rate / 100)
    yearly_tax : float = monthly_tax * 12
    monthly_net_income : float = monthly_income - monthly_tax - monthly_expenses
    yearly_net_income : float = yearly_income - yearly_tax - yearly_expenses


    print('-----------')
    print(f'Monthly Income : {currency}{monthly_income:,.2f}')
    print(f'Tax Rate : {tax_rate:,.0f}%')
    print(f'Yearly Income : {currency}{yearly_income:,.2f}')
    print(f'Yearly Net Income : {currency}{yearly_net_income:,.2f}')
    print(f'Monthly Net Income : {currency}{monthly_net_income:,.2f}')
    print(f'Monthly Tax Paid : {currency}{monthly_tax:,.2f}')
    print(f'Yearly Tax Paid : {currency}{yearly_tax:,.2f}')
    print(f'Monthly Expenses : {currency}{monthly_expenses:,.2f}')
    print(f'Yearly Expenses : {currency}{yearly_expenses:,.2f}') 
    print('-------------')

def main() -> None:
    monthly_income = get_valid_float("Please Enter Your Monthly Salary: $", "Monthly income must be positive.")
    tax_rate = get_valid_float('Please Enter Your Tax Rate(%): ', 'Tax Rate Must Be a Positive Numbe.r', positive_only= False)
    rent = get_valid_float('Please Enter Your Rent Payment: $', 'This Input Must Be a Positive Number.')
    food = get_valid_float('Pleaase Enter Your Food Cost: $', 'Please Enter a Number.')
    gym_membership = get_valid_float('Please Enter Gym Membership Fee: $', 'This Input Must Be a Positive Number.')
    monthly_expenses = rent + food + gym_membership
    calculate_finances(monthly_income, tax_rate, monthly_expenses, currency= '$')

if __name__ == '__main__':
    main()
