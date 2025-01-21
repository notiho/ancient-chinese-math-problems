"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
荅曰：醇酒 a升 ，行酒 b斗 。
"""

"""
Suppose there is pure wine (醇酒) priced at 50 qian per dou, and diluted wine (行酒) priced at 10 qian per dou.
Now, with 30 qian, one can obtain 2 dou of wine in total.
Question: how much pure wine and diluted wine are obtained respectively?

Answer: *a* sheng of pure wine, and *b* dou of diluted wine.
"""

# Prices and total constraints
醇酒價格 = 50  # per dou
行酒價格 = 10  # per dou
總錢 = 30  # total money
總酒 = 2  # total wine in dou

# Let x be the amount of pure wine (in dou), and y be the amount of diluted wine (in dou)
# Equations:
# 1. x + y = 2  (total wine)
# 2. 50x + 10y = 30  (total cost)

# Solve for x and y
from fractions import Fraction

# From the first equation: y = 2 - x
# Substitute into the second equation:
# 50x + 10(2 - x) = 30
# 50x + 20 - 10x = 30
# 40x = 10
x = Fraction(10, 40)  # x = 1/4 dou of pure wine
y = 2 - x  # y = 2 - 1/4 = 7/4 dou of diluted wine

# Convert x (pure wine) to sheng (1 dou = 10 sheng)
a = x * 10  # a = 10 * 1/4 = 5/2 sheng of pure wine
b = y  # b = 7/4 dou of diluted wine

# Final results
a, b  # a = 5/2 sheng, b = 7/4 dou
"""
"""
