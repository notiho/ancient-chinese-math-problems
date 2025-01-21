"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：醇酒 a升 ，行酒 b斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the amounts of pure wine (`a`, in sheng) and diluted wine (`b`, in dou) that can be purchased with 30 coins, given their respective prices and constraints.

Here is the Python code:


"""


from fractions import Fraction

# Prices and constraints
price_pure_wine = 50  # Pure wine costs 50 coins per dou
price_diluted_wine = 10  # Diluted wine costs 10 coins per dou
total_money = 30  # Total money available (in coins)
total_wine = 2  # Total wine purchased (in dou)

# Let a = amount of pure wine (in dou)
# Let b = amount of diluted wine (in dou)

# System of equations:
# 1. a + b = total_wine
# 2. 50a + 10b = total_money

# Solve for a and b
# From equation 1: b = total_wine - a
# Substitute into equation 2:
# 50a + 10(total_wine - a) = total_money
# 50a + 10*total_wine - 10a = total_money
# 40a = total_money - 10*total_wine
# a = (total_money - 10*total_wine) / 40
a = Fraction(total_money - 10 * total_wine, 40)

# Solve for b using b = total_wine - a
b = Fraction(total_wine) - a

# Convert a to sheng (1 dou = 10 sheng)
a = a * 10  # Convert a from dou to sheng

# Output the results
a  # Amount of pure wine in sheng
b  # Amount of diluted wine in dou


"""


### Explanation of the Code:
1. **Define the prices and constraints**:
   - Pure wine costs 50 coins per dou.
   - Diluted wine costs 10 coins per dou.
   - You have 30 coins and want to buy 2 dou of wine in total.

2. **Set up the equations**:
   - Equation 1: `a + b = 2` (total wine is 2 dou).
   - Equation 2: `50a + 10b = 30` (total cost is 30 coins).

3. **Solve for `a` and `b`**:
   - Substitute `b = 2 - a` into the second equation.
   - Solve for `a` and then calculate `b`.

4. **Convert units**:
   - Convert `a` from dou to sheng (1 dou = 10 sheng).

### Final Results:
- `a` is the amount of pure wine in sheng.
- `b` is the amount of diluted wine in dou.
"""


"""
"""
