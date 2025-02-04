"""
今有出錢五百七十六，買竹七十八箇。欲其大小率之，問︰各幾何？
荅曰：其 a箇 ，箇 b錢 。其 c箇 ，箇 d錢 。
"""

"""
Suppose there is a total of 576 qian spent to buy 78 bamboo poles. The poles are of two types: large and small. 
It is desired to determine the number of each type and their respective prices.

Answer: there are *a* large poles, each costing *b* qian, and *c* small poles, each costing *d* qian.
"""

# Total money spent
total_money = 576

# Total number of bamboo poles
total_poles = 78

# Assume the price of a large pole is 9 qian and the price of a small pole is 7 qian
price_large = 9
price_small = 7

# Let the number of large poles be a, and the number of small poles be c
# Solve the system of equations:
# a + c = total_poles
# a * price_large + c * price_small = total_money

# From the first equation: c = total_poles - a
# Substitute into the second equation:
# a * price_large + (total_poles - a) * price_small = total_money
# Simplify:
# a * price_large + total_poles * price_small - a * price_small = total_money
# a * (price_large - price_small) = total_money - total_poles * price_small
# a = (total_money - total_poles * price_small) / (price_large - price_small)

a = (total_money - total_poles * price_small) // (price_large - price_small)
c = total_poles - a

# Calculate the price of each type
b = price_large
d = price_small

# Results
a, b, c, d
"""
Variable 'a' has wrong value. Expected: 48, Actual: 15
Variable 'b' has wrong value. Expected: 7, Actual: 9
Variable 'c' has wrong value. Expected: 30, Actual: 63
Variable 'd' has wrong value. Expected: 8, Actual: 7"""
