"""
今有共買物，人出八，盈三；人出七，不足四。問︰人數、物價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，物價 b 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given data
rate1 = 8  # Each person contributes 8
surplus = 3  # Surplus of 3
rate2 = 7  # Each person contributes 7
deficit = 4  # Deficit of 4

# Step 1: Compute the total amount contributed in each case
total1 = rate1 * surplus
total2 = rate2 * deficit

# Step 2: Compute the difference in rates and the difference in total contributions
rate_difference = rate1 - rate2
total_difference = total1 + total2

# Step 3: Solve for the number of people (a) and the price of the item (b)
a = Fraction(total_difference, rate_difference)  # Number of people
b = Fraction(rate1 * a - surplus)  # Price of the item

# Results
a, b


"""


This code calculates the number of people (`a`) and the price of the item (`b`) using the method described in the problem. The results are stored in the variables `a` and `b`.
"""


"""
Variable 'a' has wrong value. Expected: 7, Actual: 52
Variable 'b' has wrong value. Expected: 53, Actual: 413"""
