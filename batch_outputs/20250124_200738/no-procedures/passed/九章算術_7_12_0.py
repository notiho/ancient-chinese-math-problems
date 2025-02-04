"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
荅曰：醇酒 a升 ，行酒 b斗 。
"""

#----- content starts here -----
"""
Suppose there is pure wine (醇酒) costing 50 qian per dou, and diluted wine (行酒) costing 10 qian per dou.
Now, with 30 qian, one can buy 2 dou of wine in total.
Question: how much pure wine and how much diluted wine does one get?

Answer: one gets *a* sheng of pure wine and *b* dou of diluted wine.
"""

# Prices and total constraints
醇酒價格 = 50  # qian per dou
行酒價格 = 10  # qian per dou
總錢 = 30  # qian
總酒 = 2  # dou

# Let x be the amount of pure wine (in dou), and y be the amount of diluted wine (in dou)
# We know:
# 1. x + y = 2 (total wine is 2 dou)
# 2. 50x + 10y = 30 (total cost is 30 qian)

# Solve for x and y
from fractions import Fraction

# From equation 1: y = 2 - x
# Substitute into equation 2: 50x + 10(2 - x) = 30
# Simplify: 50x + 20 - 10x = 30
# 40x = 10
x = Fraction(10, 40)  # x = 1/4 dou of pure wine
y = 2 - x  # y = 2 - 1/4 = 7/4 dou of diluted wine

# Convert x into sheng (1 dou = 10 sheng)
a = x * 10  # a = amount of pure wine in sheng
b = y  # b = amount of diluted wine in dou

# Final results
a, b  # a is in sheng, b is in dou#----- content ends here -----

"""
"""
