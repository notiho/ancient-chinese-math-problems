"""
今有三人共車，二車空；二人共車，九人步。問：人與車各幾何？
術曰：置二人以三乘之，得六，加步者九人，得車一十五，欲知人者，以二乘車，加九人即得。
答曰： a 車， b人 。
"""

#----- content starts here -----
"""
Suppose there are three people sharing one cart, leaving two carts empty. 
If two people share one cart, nine people are left walking.
Question: how many people and carts are there?

The procedure says: Multiply 2 people by 3, obtaining 6. Add the 9 people walking, obtaining 15 carts.
To find the number of people, multiply the number of carts by 2, then add the 9 people walking.

Answer: *a* carts, *b* people.
"""

from sympy import symbols, Eq, solve

# Define variables
人 = symbols('人')  # Total number of people
車 = symbols('車')  # Total number of carts

# Equation 1: 3 people per cart, leaving 2 carts empty
eq1 = Eq(人 / 3 + 2, 車)

# Equation 2: 2 people per cart, leaving 9 people walking
eq2 = Eq(人 / 2 + 9, 車)

# Solve the system of equations
solution = solve((eq1, eq2), (人, 車))

# Extract the results
a = solution[車]
b = solution[人]

a, b  # Output the number of carts and people#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 15, Actual: -12
Variable 'b' has wrong value. Expected: 39, Actual: -42"""
