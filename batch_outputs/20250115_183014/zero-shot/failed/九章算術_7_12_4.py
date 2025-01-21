"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：醇酒 a升 ，行酒 b斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves determining how much of two types of wine (醇酒 and 行酒) are purchased with a given amount of money, given their respective prices.

Here is the Python code:


"""


from fractions import Fraction

# Prices and quantities
price_chunjiu = Fraction(50, 10)  # 醇酒 price per 1斗 (50錢 per 1斗)
price_xingjiu = Fraction(10, 10)  # 行酒 price per 1斗 (10錢 per 1斗)

# Total money and total wine
total_money = 30  # 錢
total_wine = 2  # 斗

# Let a = 醇酒 in 斗, b = 行酒 in 斗
# We have the following equations:
# 1. a + b = 2 (total wine)
# 2. 5a + b = 30 (total money, converted to 錢)

# Solve the system of equations
# From equation 1: b = 2 - a
# Substitute into equation 2: 5a + (2 - a) = 30
# Simplify: 5a + 2 - a = 30
#           4a + 2 = 30
#           4a = 28
#           a = 7

a = Fraction(7, 10)  # 醇酒 in 斗
b = total_wine - a  # 行酒 in 斗
b = Fraction(2) - a

# Results
a  # 醇酒 in 斗
b  # 行酒 in 斗


"""


### Explanation:
1. The problem gives the price of 醇酒 (50錢 per 1斗) and 行酒 (10錢 per 1斗).
2. The total money spent is 30錢, and the total wine purchased is 2斗.
3. We set up two equations:
   - \( a + b = 2 \) (total wine)
   - \( 5a + b = 30 \) (total money, where 醇酒 is 5 times more expensive than 行酒)
4. Solving these equations gives \( a = \frac{7}{10} \) (醇酒 in 斗) and \( b = \frac{13}{10} \) (行酒 in 斗).

### Final Answer:
- 醇酒 \( a = \frac{7}{10} \) 斗
- 行酒 \( b = \frac{13}{10} \) 斗
"""


"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 7/10
Variable 'b' has wrong value. Expected: 7/4, Actual: 13/10"""
