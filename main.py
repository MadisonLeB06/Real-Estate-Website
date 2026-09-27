# the affordability counter

# user inputs #
annual_income = 100000
monthly_debt = 500 # optional, default 0
down_payment = 50000
interest_rate = 7.438 # optional
loan_term = 30 # optional, default 30
property_tax = 281 # optional
home_insurance = 78 # optional
pmi = 0 # optional, default 0
hoa = 0 # optional, default 0

# calc constants #
RECOMMENDED_HOUSING_RATIO = 0.30
RECOMMENDED_DTI = 0.36
MAX_DTI = 0.43


# calculated variables #

monthly_income = annual_income / 12
housing_limit = monthly_income * RECOMMENDED_HOUSING_RATIO
dti_limit = (monthly_income * RECOMMENDED_DTI) - monthly_debt
housing_budget = min(housing_limit, dti_limit)
other_housing_costs = property_tax + home_insurance + pmi + hoa
mortgage_payment = housing_budget - other_housing_costs
monthly_interest_rate = (interest_rate / 100) / 12
number_of_payments = loan_term * 12
loan_amount = mortgage_payment * ((1 - (1 + monthly_interest_rate) ** -number_of_payments) / monthly_interest_rate)
recommended_home_price = loan_amount + down_payment

# calculation for max house price #

max_housing_budget = (monthly_income * MAX_DTI) - monthly_debt
max_mortgage_payment = max_housing_budget - other_housing_costs
max_loan_amount = max_mortgage_payment * ((1 - (1 + monthly_interest_rate) ** -number_of_payments) / monthly_interest_rate)
max_home_price = max_loan_amount + down_payment

print(f"${int(recommended_home_price)} is your recommended home price in your budget range.\n")
print(f"${int(max_home_price)} is your max home price still within your budget range.")

'''
for search engine, have filtering options such as "up to recommended house price ($100k - $358k)",
"recommeneded house price to maximum house price ($358k - $442k)", and "up to maximum house price ($100k - $442k)"
'''