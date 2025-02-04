"""
今有共買物，人出八，盈三；人出七，不足四。問︰人數、物價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，物價 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the number of people (`a`) and the price of the item (`b`) based on the given conditions.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given conditions
rate1 = 8  # Each person contributes 8
excess = 3  # Excess amount is 3
rate2 = 7  # Each person contributes 7
deficit = 4  # Deficit amount is 4

# Step 1: Compute the total amount contributed in each case
total1 = rate1  # Total contribution rate for the first case
total2 = rate2  # Total contribution rate for the second case

# Step 2: Compute the difference in rates and the sum of excess and deficit
difference_in_rates = total1 - total2  # Difference in contribution rates
sum_excess_deficit = excess + deficit  # Sum of excess and deficit

# Step 3: Compute the number of people (a)
a = Fraction(sum_excess_deficit, difference_in_rates)

# Step 4: Compute the price of the item (b)
b = Fraction(rate1 * a - excess)

# Results
a = int(a)  # Number of people must be an integer
b = int(b)  # Price of the item must be an integer

# Output the results
print("Number of people (a):", a)
print("Price of the item (b):", b)
#----- content ends here -----


"""


### Explanation:
1. The problem states that if each person contributes 8, there is an excess of 3. If each person contributes 7, there is a deficit of 4.
2. Using the "盈不足術" (Surplus and Deficit Method), we calculate the number of people (`a`) and the price of the item (`b`).
3. The difference in rates (8 - 7) and the sum of the excess and deficit (3 + 4) are used to compute `a`.
4. Once `a` is found, we use it to calculate the price of the item (`b`).

### Output:
The code will compute the values of `a` (number of people) and `b` (price of the item).
"""


"""
"""
