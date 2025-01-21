"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：醇酒 a升 ，行酒 b斗 。
"""

"""
To solve this problem, we translate the ancient Chinese math problem into Python code. The problem involves finding the quantities of "醇酒" (pure wine) and "行酒" (diluted wine) given certain constraints. Here's the Python code:


"""


from fractions import Fraction

# Let a = amount of 醇酒 (pure wine) in 升
# Let b = amount of 行酒 (diluted wine) in 斗

# Given:
# 1 斗 of 醇酒 costs 50 錢
# 1 斗 of 行酒 costs 10 錢
# Total money spent = 30 錢
# Total wine obtained = 2 斗

# Convert everything to consistent units (升):
# 1 斗 = 10 升
# Cost of 醇酒 per 升 = 50 / 10 = 5 錢
# Cost of 行酒 per 升 = 10 / 10 = 1 錢

# Equations:
# 1. 5a + b = 30  (total cost in 錢)
# 2. a + b = 20   (total volume in 升)

# Solve the system of equations:
# From equation 2: b = 20 - a
# Substitute into equation 1:
# 5a + (20 - a) = 30
# 5a + 20 - a = 30
# 4a = 10
# a = 10 / 4
a = Fraction(10, 4)

# Substitute a back into equation 2 to find b:
# a + b = 20
# b = 20 - a
b = 20 - a

# Results:
# a = amount of 醇酒 in 升
# b = amount of 行酒 in 升


"""


The solution is:
- `a = 5/2` 升 (醇酒)
- `b = 35/2` 升 (行酒)
"""


"""
Variable 'b' has wrong value. Expected: 7/4, Actual: 35/2"""
