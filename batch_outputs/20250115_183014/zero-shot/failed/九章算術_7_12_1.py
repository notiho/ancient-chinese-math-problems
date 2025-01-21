"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：醇酒 a升 ，行酒 b斗 。
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
# 2. price_chun * a + price_xing * b = total_money

# Solve for a and b
# From equation 1: b = total_volume - a
# Substitute into equation 2:
# price_chun * a + price_xing * (total_volume - a) = total_money
# price_chun * a + price_xing * total_volume - price_xing * a = total_money
# (price_chun - price_xing) * a = total_money - price_xing * total_volume
# a = (total_money - price_xing * total_volume) / (price_chun - price_xing)

a = (total_money - price_xing * total_volume) / (price_chun - price_xing)
b = total_volume - a

# Results
a  # 醇酒 in 斗
b  # 行酒 in 斗


"""


### Explanation:
1. We define the prices of 醇酒 (price_chun) and 行酒 (price_xing) per 斗.
2. The total money spent is 30, and the total volume of wine purchased is 2 斗.
3. Using the two equations:
   - \( a + b = 2 \) (total volume constraint)
   - \( 50a + 10b = 30 \) (total money constraint),
   we solve for \( a \) (醇酒 in 斗) and \( b \) (行酒 in 斗).
4. Substituting \( b = 2 - a \) into the second equation, we solve for \( a \) and then calculate \( b \).

### Final Values:
- \( a \) represents the amount of 醇酒 in 斗.
- \( b \) represents the amount of 行酒 in 斗.
"""


"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 1/4"""
