from decimal import Decimal, getcontext

def arctan_series(x, iterations):
    getcontext().prec = iterations * 2  # Set precision higher for intermediate calculations
    term = Decimal(x)
    sum_val = term
    for i in range(1, iterations):
        term = term * (-x*x) * (2*i - 1) / (2*i + 1)
        sum_val += term
    return sum_val

def calculate_pi_machin(num_digits, iterations_per_arctan):
    getcontext().prec = num_digits + 5 # Add buffer for precision
    
    arctan_1_5 = arctan_series(Decimal(1)/5, iterations_per_arctan)
    arctan_1_239 = arctan_series(Decimal(1)/239, iterations_per_arctan)
    
    pi_val = 16 * arctan_1_5 - 4 * arctan_1_239
    return pi_val