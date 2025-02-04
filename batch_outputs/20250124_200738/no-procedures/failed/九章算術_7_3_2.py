"""
今有共買牛，七家共出一百九十，不足三百三十；九家共出二百七十，盈三十。問︰家數、牛價各幾何？
荅曰： a家 ，牛價 b 。
"""

#----- content starts here -----
"""
Suppose there are people pooling money to buy a cow. 
- Seven families together contribute 190, which is 330 less than the required amount.
- Nine families together contribute 270, which is 30 more than the required amount.

Question: How many families are there in total (*a*), and what is the price of the cow (*b*)?

Answer: *a* families, and the price of the cow is *b*.
"""

# Let x be the number of families, and y be the price of the cow.

# Equation 1: 7 families contribute 190, which is 330 less than the price of the cow.
# 7 * (y / x) = 190 + 330
# Equation 2: 9 families contribute 270, which is 30 more than the price of the cow.
# 9 * (y / x) = 270 - 30

# Solving these equations step by step:

# Step 1: Express y/x from each equation.
# From Equation 1:
price_per_family_1 = Fraction(190 + 330, 7)

# From Equation 2:
price_per_family_2 = Fraction(270 - 30, 9)

# Step 2: Set the two expressions for y/x equal to each other.
# price_per_family_1 = price_per_family_2
# Solve for x (number of families):
a = Fraction(9 * (190 + 330), 7 * (270 - 30))

# Step 3: Solve for y (price of the cow):
b = a * price_per_family_1

# Final results:
a = int(a)  # Number of families must be an integer
b = int(b)  # Price of the cow must be an integer

a, b  # Output the results#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 126, Actual: 2
Variable 'b' has wrong value. Expected: 3750, Actual: 206"""
