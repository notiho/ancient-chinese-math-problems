"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：醇酒 a升 ，行酒 b斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the quantities of pure wine ("醇酒") and diluted wine ("行酒") that can be purchased with a given amount of money, given their respective prices and the total volume of wine purchased.

Here is the Python code:


"""


from fractions import Fraction

# Prices and total money
price_pure_wine = 50  # 醇酒 price per 1 斗
price_diluted_wine = 10  # 行酒 price per 1 斗
total_money = 30  # Total money spent
total_volume = 2  # Total volume of wine purchased in 斗

# Let a = volume of pure wine (醇酒) in 斗
# Let b = volume of diluted wine (行酒) in 斗
# Equations:
# 1. a + b = total_volume
# 2. 50a + 10b = total_money

# Solve the equations
# From equation 1: b = total_volume - a
# Substitute into equation 2:
# 50a + 10(total_volume - a) = total_money
# 50a + 10*2 - 10a = 30
# 40a + 20 = 30
# 40a = 10
# a = 10 / 40 = 1/4

a = Fraction(1, 4)  # Volume of pure wine (醇酒) in 斗
b = total_volume - a  # Volume of diluted wine (行酒) in 斗

# Output the results
a  # 醇酒 in 斗
b  # 行酒 in 斗


"""


### Solution:
- `a = 1/4` 斗 (pure wine, 醇酒)
- `b = 7/4` 斗 (diluted wine, 行酒)
"""


"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 1/4"""
