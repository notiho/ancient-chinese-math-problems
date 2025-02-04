"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：醇酒 a升 ，行酒 b斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves determining how much of two types of wine (醇酒 and 行酒) are obtained when spending a certain amount of money and receiving a specific total volume of wine. Here's the solution:


"""


from fractions import Fraction

# Given data
price_pure_wine = 50  # 醇酒一斗，直錢五十
price_mixed_wine = 10  # 行酒一斗，直錢一十
total_money = 30  # 錢三十
total_volume = 2  # 酒二斗

# Let the amount of pure wine (醇酒) be a (in dou) and the amount of mixed wine (行酒) be b (in dou).
# We have the following equations:
# 1. a + b = 2 (total volume of wine)
# 2. 50a + 10b = 30 (total cost of wine)

# Solve the system of equations
# From equation 1: b = 2 - a
# Substitute into equation 2: 50a + 10(2 - a) = 30
# Simplify: 50a + 20 - 10a = 30
# 40a = 10
# a = 10 / 40 = 1/4 (in dou)

a = Fraction(1, 4)  # Amount of pure wine (醇酒) in dou
b = total_volume - a  # Amount of mixed wine (行酒) in dou

# Output the results
a  # 醇酒 in dou
b  # 行酒 in dou


"""


### Explanation of the solution:
1. We set up two equations based on the problem:
   - The total volume of wine is 2 dou: \( a + b = 2 \).
   - The total cost of the wine is 30 units of money: \( 50a + 10b = 30 \).
2. We solve the system of equations by substitution:
   - From the first equation, \( b = 2 - a \).
   - Substitute \( b \) into the second equation and solve for \( a \).
3. After finding \( a \), we calculate \( b \) using \( b = 2 - a \).
4. The results are stored in the variables `a` (醇酒 in dou) and `b` (行酒 in dou).

### Final Answer:
- 醇酒 \( a = \frac{1}{4} \) dou
- 行酒 \( b = \frac{7}{4} \) dou
"""


"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 1/4"""
