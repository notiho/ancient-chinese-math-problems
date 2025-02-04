"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
Suppose there is good farmland where 1 mu costs 300 coins, and poor farmland where 7 mu costs 500 coins.
Now, if 1 qing (100 mu) of mixed farmland is purchased for 10,000 coins, how much of it is good farmland and how much is poor farmland?

Answer: *a* mu of good farmland, and *b* mu of poor farmland.
"""

from fractions import Fraction

# Prices and total land
善田價 = 300  # per mu
惡田價 = Fraction(500, 7)  # per mu
總價 = 10000  # total price
總畝 = 100  # total land in mu

# Let x = 善田 (good farmland in mu), and y = 惡田 (poor farmland in mu)
# We know:
# 1. x + y = 總畝
# 2. 善田價 * x + 惡田價 * y = 總價

# Solve for x and y
# From equation 1: y = 總畝 - x
# Substitute into equation 2:
# 善田價 * x + 惡田價 * (總畝 - x) = 總價

# Expand and simplify:
# 善田價 * x + 惡田價 * 總畝 - 惡田價 * x = 總價
# (善田價 - 惡田價) * x = 總價 - 惡田價 * 總畝
# x = (總價 - 惡田價 * 總畝) / (善田價 - 惡田價)

x = (總價 - 惡田價 * 總畝) / (善田價 - 惡田價)
y = 總畝 - x

# Results
a = x  # 善田 (good farmland in mu)
b = y  # 惡田 (poor farmland in mu)

a, b  # Output the results
"""
"""
