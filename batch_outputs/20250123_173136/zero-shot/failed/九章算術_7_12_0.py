"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：醇酒 a升 ，行酒 b斗 。
"""

"""
To solve this problem, we translate the ancient Chinese math problem into Python code. The problem involves finding the quantities of "醇酒" (pure wine) and "行酒" (diluted wine) that can be purchased with a given amount of money, given their respective prices and the total volume of wine purchased.

Here is the Python code:


"""


from fractions import Fraction

# Prices and total money
price_pure_wine = 50  # 醇酒 price per 1斗
price_diluted_wine = 10  # 行酒 price per 1斗
total_money = 30  # Total money in 錢
total_volume = 2  # Total volume in 斗

# Let the amount of pure wine be a (in 斗) and the amount of diluted wine be b (in 斗)
# Equations:
# 1. a + b = total_volume
# 2. 50a + 10b = total_money

# Solve the equations
# From equation 1: b = total_volume - a
# Substitute into equation 2: 50a + 10(total_volume - a) = total_money
# Simplify: 50a + 10(total_volume) - 10a = total_money
# Combine terms: 40a = total_money - 10(total_volume)
# Solve for a: a = (total_money - 10(total_volume)) / 40

a = Fraction(total_money - 10 * total_volume, 40)  # Amount of pure wine in 斗
b = total_volume - a  # Amount of diluted wine in 斗

# Output the results
a  # 醇酒 in 斗
b  # 行酒 in 斗


"""


### Explanation:
1. The problem gives the prices of pure wine (醇酒) and diluted wine (行酒) as 50 and 10 錢 per 斗, respectively.
2. The total money spent is 30 錢, and the total volume of wine purchased is 2 斗.
3. We set up two equations:
   - \( a + b = 2 \) (total volume)
   - \( 50a + 10b = 30 \) (total cost)
4. Solving these equations yields the values of \( a \) (pure wine in 斗) and \( b \) (diluted wine in 斗).

### Final Answer:
- \( a \): Amount of pure wine (醇酒) in 斗
- \( b \): Amount of diluted wine (行酒) in 斗
"""


"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 1/4"""
