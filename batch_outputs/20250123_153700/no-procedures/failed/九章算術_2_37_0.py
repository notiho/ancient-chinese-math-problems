"""
今有出錢五百七十六，買竹七十八箇。欲其大小率之，問︰各幾何？
荅曰：其 a箇 ，箇 b錢 。其 c箇 ，箇 d錢 。
"""

"""
Suppose there is a total of 576 qian (coins) used to buy 78 bamboo pieces. The bamboo pieces are of two types: large and small.
It is desired to determine the number of each type and their respective prices.

Answer: there are *a* pieces of one type, each costing *b* qian, and *c* pieces of the other type, each costing *d* qian.
"""

# Total money and total bamboo pieces
總錢 = 576
總竹 = 78

# Assume the large bamboo costs 9 qian each and the small bamboo costs 5 qian each
大竹價 = 9
小竹價 = 5

# Let the number of large bamboo pieces be x and small bamboo pieces be y
# We know:
# x + y = 總竹
# 9x + 5y = 總錢

# Solve for x and y
from fractions import Fraction

x = Fraction(總錢 - 小竹價 * 總竹, 大竹價 - 小竹價)
y = 總竹 - x

# Assign the results
a = x
b = 大竹價
c = y
d = 小竹價

# Results
a, b, c, d
"""
Variable 'a' has wrong value. Expected: 48, Actual: 93/2
Variable 'b' has wrong value. Expected: 7, Actual: 9
Variable 'c' has wrong value. Expected: 30, Actual: 63/2
Variable 'd' has wrong value. Expected: 8, Actual: 5"""
