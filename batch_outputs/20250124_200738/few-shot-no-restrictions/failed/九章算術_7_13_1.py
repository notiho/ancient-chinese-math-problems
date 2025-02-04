"""
今有大器五、小器一容三斛；大器一、小器五容二斛。問︰大、小器各容幾何？
術曰：假令大器五斗，小器亦五斗，盈一十斗。令之大器五斗五升，小器二斗五升，不足二斗。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：大器容 a斛 ，小器容 b斛 。
"""

"""
This is a classic "excess and deficit" (盈不足) problem from ancient Chinese mathematics. Let's solve it step by step and translate the procedure into Python code.

### Problem:
There are two types of containers: large and small.  
- 5 large containers and 1 small container together hold 3 hu.  
- 1 large container and 5 small containers together hold 2 hu.  

Question: How much does each large container and each small container hold?

### Procedure:
1. Assume the capacity of the large container is \( x \) and the small container is \( y \).  
   - From the first condition: \( 5x + y = 3 \).  
   - From the second condition: \( x + 5y = 2 \).  

2. Use the "excess and deficit" method to solve for \( x \) and \( y \):  
   - Place the coefficients of \( x \) and \( y \) (the "rates") under the respective conditions.  
   - Multiply the rates by their respective coefficients, sum them to get the "numerator" (實).  
   - Add the total coefficients to get the "denominator" (法).  
   - Divide the numerator by the denominator to find the solution.  

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients from the problem
# 5 large containers + 1 small container = 3 hu
rate1_large = 5
rate1_small = 1
total1 = 3

# 1 large container + 5 small containers = 2 hu
rate2_large = 1
rate2_small = 5
total2 = 2

# 盈不足術 (Excess and Deficit Method)
# Multiply the rates by their respective totals
numerator_large = rate1_large * total2 + rate2_large * total1
numerator_small = rate1_small * total2 + rate2_small * total1

# Add the total coefficients to get the denominator
denominator = rate1_large + rate1_small + rate2_large + rate2_small

# Solve for the capacities of the large and small containers
capacity_large = Fraction(numerator_large, denominator)
capacity_small = Fraction(numerator_small, denominator)

# Output the results
a = capacity_large  # Capacity of the large container in hu
b = capacity_small  # Capacity of the small container in hu

print(f"大器容 {a} 斛，小器容 {b} 斛。")
#----- content ends here -----


"""


### Explanation of the Code:
1. The coefficients of the large and small containers are multiplied by the totals from the other equation (cross-multiplication).
2. The numerator is the sum of these products, and the denominator is the sum of all coefficients.
3. The capacities of the large and small containers are calculated as fractions to ensure precision.

### Answer:
The capacities of the large and small containers are:
- Large container: \( a \) hu.
- Small container: \( b \) hu.
"""


"""
Variable 'a' has wrong value. Expected: 13/24, Actual: 13/12
Variable 'b' has wrong value. Expected: 7/24, Actual: 17/12"""
