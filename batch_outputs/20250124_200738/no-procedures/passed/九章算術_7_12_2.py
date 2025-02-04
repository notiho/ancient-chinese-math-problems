"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
荅曰：醇酒 a升 ，行酒 b斗 。
"""

#----- content starts here -----
"""
Suppose there is pure wine (醇酒) that costs 50 qian per dou, and diluted wine (行酒) that costs 10 qian per dou.
Now, with 30 qian, one can buy a total of 2 dou of wine.
Question: how much pure wine and diluted wine does one get?

Answer: one gets *a* sheng of pure wine and *b* dou of diluted wine.
"""

# Define the costs and total constraints
醇酒價格 = 50  # per dou
行酒價格 = 10  # per dou
總錢 = 30  # total money
總酒 = 2  # total wine in dou

# Let x be the amount of pure wine in dou, and y be the amount of diluted wine in dou
# Equations:
# 1. x + y = 2 (total wine)
# 2. 50x + 10y = 30 (total cost)

# Solve for x (醇酒 in dou) and y (行酒 in dou)
from fractions import Fraction

x = Fraction(總錢 - 行酒價格 * 總酒, 醇酒價格 - 行酒價格)  # amount of pure wine in dou
y = 總酒 - x  # amount of diluted wine in dou

# Convert x to sheng (1 dou = 10 sheng)
a = x * 10  # pure wine in sheng
b = y  # diluted wine in dou

# Results
a, b  # a is pure wine in sheng, b is diluted wine in dou#----- content ends here -----

"""
"""
