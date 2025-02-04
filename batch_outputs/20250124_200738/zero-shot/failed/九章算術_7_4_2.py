"""
今有共買金，人出四百，盈三千四百；人出三百，盈一百。問︰人數、金價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a人 。金價 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the number of people (`a`) and the price of gold (`b`) based on the given conditions.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
rate1 = 400  # Rate at which each person contributes in the first case
profit1 = 3400  # Profit in the first case
rate2 = 300  # Rate at which each person contributes in the second case
profit2 = 100  # Profit in the second case

# Step 1: Compute the "實" (numerator)
numerator = (rate1 * profit2) - (rate2 * profit1)

# Step 2: Compute the "法" (denominator)
denominator = profit2 - profit1

# Step 3: Compute the number of people (a)
a = Fraction(numerator, denominator)

# Step 4: Compute the price of gold (b)
b = Fraction(profit1, a) + rate1

# The results
a, b
#----- content ends here -----


"""


### Explanation:
1. **Step 1**: Compute the "實" (numerator) by multiplying the rates by the respective profits and subtracting the smaller from the larger.
2. **Step 2**: Compute the "法" (denominator) by subtracting the smaller profit from the larger profit.
3. **Step 3**: The number of people (`a`) is calculated as the ratio of the numerator to the denominator.
4. **Step 4**: The price of gold (`b`) is calculated using the formula derived from the first condition.

### Output:
The variables `a` and `b` will contain the number of people and the price of gold, respectively, as fractions.
"""


"""
Variable 'a' has wrong value. Expected: 33, Actual: 9800/33
Variable 'b' has wrong value. Expected: 9800, Actual: 20161/49"""
