"""
今有共買牛，七家共出一百九十，不足三百三十；九家共出二百七十，盈三十。問︰家數、牛價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a家 ，牛價 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves determining the number of families (`a`) and the price of a cow (`b`) based on the given conditions.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
rate1 = 7  # Seven families
rate2 = 9  # Nine families
total1 = 190  # Total money contributed by 7 families
total2 = 270  # Total money contributed by 9 families
deficit = 330 - total1  # Deficit when 7 families contribute
surplus = total2 - 300  # Surplus when 9 families contribute

# Step 1: Compute the difference in rates and the difference in total contributions
rate_difference = rate2 - rate1
total_difference = surplus + deficit

# Step 2: Compute the price of a cow (b)
b = Fraction(total_difference, rate_difference)

# Step 3: Compute the number of families (a)
a = Fraction(total1, b)

# Results
a = int(a)  # Number of families must be an integer
b = float(b)  # Price of a cow

# Outputs
print("Number of families (a):", a)
print("Price of a cow (b):", b)
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Data**: The problem provides the contributions of 7 families and 9 families, along with the deficit and surplus.
2. **Rate Difference**: The difference in the number of families contributing is `rate2 - rate1`.
3. **Total Difference**: The sum of the surplus and deficit is used to compute the price of a cow.
4. **Price of a Cow (b)**: Using the formula `b = total_difference / rate_difference`, we calculate the price of a cow.
5. **Number of Families (a)**: Using the formula `a = total1 / b`, we calculate the number of families.

### Outputs:
- `a`: The number of families.
- `b`: The price of a cow.
"""


"""
Variable 'a' has wrong value. Expected: 126, Actual: 3
Variable 'b' has wrong value. Expected: 3750, Actual: 55.0"""
