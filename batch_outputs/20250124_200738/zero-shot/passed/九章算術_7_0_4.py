"""
今有共買物，人出八，盈三；人出七，不足四。問︰人數、物價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，物價 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the number of people (`a`) and the price of the item (`b`) based on the given conditions.

### Problem Breakdown:
1. If each person contributes 8 units, there is an excess of 3 units.
2. If each person contributes 7 units, there is a shortage of 4 units.

Using the "盈不足術" (Surplus and Deficit Method), we can calculate the number of people (`a`) and the price of the item (`b`).

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Given data
rate1 = 8  # Contribution rate when there is a surplus
surplus = 3  # Surplus amount
rate2 = 7  # Contribution rate when there is a deficit
deficit = 4  # Deficit amount

# Step 1: Calculate the difference in rates
rate_difference = rate1 - rate2  # Difference between the two rates

# Step 2: Add surplus and deficit
total_difference = surplus + deficit  # Total difference (surplus + deficit)

# Step 3: Calculate the number of people (a)
a = Fraction(total_difference, rate_difference)  # Number of people

# Step 4: Calculate the price of the item (b)
b = a * rate1 - surplus  # Price of the item

# Results
a, b  # a is the number of people, b is the price of the item
#----- content ends here -----


"""


### Explanation of the Code:
1. **Rate Difference**: The difference between the two contribution rates (`rate1 - rate2`) is used to determine how much each person's contribution changes.
2. **Total Difference**: The sum of the surplus and deficit gives the total difference in the contributions.
3. **Number of People (`a`)**: Using the formula from the "盈不足術", the number of people is calculated as `total_difference / rate_difference`.
4. **Price of the Item (`b`)**: The price is calculated using the formula `b = a * rate1 - surplus`.

### Output:
The variables `a` and `b` will contain the number of people and the price of the item, respectively.
"""


"""
"""
