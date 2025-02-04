"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：醇酒 a升 ，行酒 b斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining how much of two types of wine (醇酒 and 行酒) are purchased with a given amount of money, given their respective prices and total volume constraints.

Here is the Python code:


"""


from fractions import Fraction

# Prices and constraints
price_chun = Fraction(50)  # 醇酒 price per 1斗
price_xing = Fraction(10)  # 行酒 price per 1斗
total_money = Fraction(30)  # Total money spent
total_volume = Fraction(2)  # Total volume in 斗

# Let a = 醇酒 in 斗, b = 行酒 in 斗
# Equations:
# 1. a + b = total_volume
# 2. 50a + 10b = total_money

# Solve the equations
# From equation 1: b = total_volume - a
# Substitute into equation 2:
# 50a + 10(total_volume - a) = total_money
# 50a + 10 * total_volume - 10a = total_money
# 40a = total_money - 10 * total_volume
# a = (total_money - 10 * total_volume) / 40

a = (total_money - 10 * total_volume) / 40
b = total_volume - a

# Results
a = a * 10  # Convert 醇酒 to 升 (1斗 = 10升)
b = b  # 行酒 remains in 斗

# Output the results
a, b


"""


### Explanation:
1. We define the prices of 醇酒 (chun wine) and 行酒 (xing wine) per 斗.
2. We know the total money spent and the total volume of wine purchased.
3. Using the two equations:
   - \( a + b = 2 \) (total volume constraint)
   - \( 50a + 10b = 30 \) (total money constraint),
   we solve for \( a \) (醇酒 in 斗) and \( b \) (行酒 in 斗).
4. Finally, we convert \( a \) from 斗 to 升 (1斗 = 10升).

### Solution:
The solution variables \( a \) and \( b \) represent the amounts of 醇酒 (in 升) and 行酒 (in 斗), respectively.
"""


"""
"""
