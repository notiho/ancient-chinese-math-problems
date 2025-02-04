"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：醇酒 a升 ，行酒 b斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the quantities of pure wine ("醇酒") and diluted wine ("行酒") that can be purchased with a given amount of money, given their respective prices.

Here is the Python code:


"""


from fractions import Fraction

# Given data
price_pure_wine = 50  # Price of 1斗 of pure wine in 錢
price_diluted_wine = 10  # Price of 1斗 of diluted wine in 錢
total_money = 30  # Total money in 錢
total_wine = 2  # Total wine in 斗

# Let the amount of pure wine be a (in 斗)
# Let the amount of diluted wine be b (in 斗)
# We have the following equations:
# 1. a + b = 2 (total wine is 2斗)
# 2. 50a + 10b = 30 (total cost is 30錢)

# Solve the equations
# From equation 1: b = 2 - a
# Substitute into equation 2: 50a + 10(2 - a) = 30
# Simplify: 50a + 20 - 10a = 30
# 40a = 10
# a = 10 / 40 = 1/4 (斗)

a = Fraction(1, 4)  # Amount of pure wine in 斗
b = total_wine - a  # Amount of diluted wine in 斗
b = Fraction(b)  # Convert to Fraction for consistency

# Output the results
a  # Amount of pure wine in 斗
b  # Amount of diluted wine in 斗


"""


### Explanation:
1. We set up two equations based on the problem:
   - The total amount of wine is 2斗: \( a + b = 2 \)
   - The total cost is 30錢: \( 50a + 10b = 30 \)
2. We solve these equations to find \( a \) (amount of pure wine) and \( b \) (amount of diluted wine).
3. The solution is computed using basic algebra and represented using the `Fraction` class for precision.

### Solution:
- \( a = \frac{1}{4} \) 斗 (pure wine)
- \( b = \frac{7}{4} \) 斗 (diluted wine)
"""


"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 1/4"""
