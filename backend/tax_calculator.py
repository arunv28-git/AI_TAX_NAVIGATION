def calculate_old_regime(income, deductions):
    taxable_income = max(income - deductions, 0)

    if taxable_income <= 250000:
        return 0
    elif taxable_income <= 500000:
        return taxable_income * 0.05
    elif taxable_income <= 1000000:
        return taxable_income * 0.20
    else:
        return taxable_income * 0.30


def calculate_new_regime(income):
    if income <= 300000:
        return 0
    elif income <= 600000:
        return income * 0.05
    elif income <= 900000:
        return income * 0.10
    elif income <= 1200000:
        return income * 0.15
    else:
        return income * 0.20