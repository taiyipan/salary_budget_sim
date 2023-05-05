# declare monthly cash outflows 
expense = {
    'rent/mortgage': 2300, # including property tax payments and homeowner association fees if applicable 
    'utilies': 200, # water, electricity, heat, gas, Internet
    'subscriptions': 100, # cloud services (iCloud, Google Cloud), streaming services (Netflix, HBO, Hulu, Disney+, Prime Video, Apple TV)
    'student_loan_repayment': 400, # depending on repayment plans on Aidvantage 
    'food': 1000, # including restaurants, food deliveries, and groceries 
    'transportation': 500, # metro, gas, car maintenance, etc. 
    'insurance': 25, # including life, auto, home insurance 
    'misc': 400 # random Amazon purchases, ex. books, electronics, gadgets, games 
}

# declare tax brackets: each bracket value indicates the base value of that bracket
brackets = {
    '10%': 0,
    '12%': 11000,
    '22%': 44725,
    '24%': 95376,
    '32%': 182101,
    '35%': 231251,
    '37%': 578126
}

# salary expectation
salary = 90000

# savings rate 
savings_rate = 0.15

# compute income tax: progressive tax 
def income_tax(n: float) -> float:
    if n <= brackets.get('12%'):
        return 0.1 * n 
    elif n > brackets.get('12%') and n <= brackets.get('22%'):
        return 1100 + 0.12 * (n - brackets.get('12%'))
    elif n > brackets.get('22%') and n <= brackets.get('24%'):
        return 5147 + 0.22 * (n - brackets.get('22%'))
    elif n > brackets.get('24%') and n <= brackets.get('32%'):
        return 16290 + 0.24 * (n - brackets.get('24%'))
    elif n > brackets.get('32%') and n <= brackets.get('35%'):
        return 37104 + 0.32 * (n - brackets.get('32%'))
    elif n > brackets.get('35%') and n <= brackets.get('37%'):
        return 52832 + 0.35 * (n - brackets.get('35%'))
    elif n > brackets.get('37%'):
        return 174238.25 + 0.37 * (n - brackets.get('37%'))

# compute social security tax: regressive tax
def social_security_tax(n: float) -> float:
    if n < 147000:
        return n * 0.062
    else:
        return 147000 * 0.062

# compute medicare tax 
def medicare_tax(n: float) -> float:
    if n < 200000:
        return n * 0.0145
    else:
        return 200000 * 0.0145 + (n - 200000) * 0.009

# compute mandatory savings: pay outstanding debts first before investment 
def savings(n: float) -> float:
    return savings_rate * n

# compute expenses 
def expenses(e: dict) -> float:
    total = 0
    for category, cost in expense.items():
        total += cost 
    return total * 12

# compute discretionary spending 
def discretionary(n: float) -> float:
    return n - income_tax(n) - social_security_tax(n) - medicare_tax(n) - savings(n) - expenses(expense)

# display metrics given hypothetical salary
def main():
    print('Salary: {}'.format(salary))
    print('Income tax: {}'.format(income_tax(salary)))
    print('Social security tax: {}'.format(social_security_tax(salary)))
    print('Medicare tax: {}'.format(medicare_tax(salary)))
    print('Mandatory {:.0f}% pre-tax savings: {}'.format(savings_rate * 100, savings(salary)))
    print('Minimum fixed expenses: {}'.format(expenses(expense)))
    print('Discretionary spending: {}'.format(discretionary(salary)))

if __name__ == '__main__':
    main()
