"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
荅曰：其 a枚 ， b枚 一錢 其 c枚 ， d枚 一錢
"""

"""
Suppose 980 qian (coins) are spent to purchase 5820 arrows. It is desired to determine the price ratio of expensive arrows to cheap arrows.
Question: how many arrows are expensive and how many are cheap, and what is the price ratio?

Answer: *a* arrows cost *b* per qian, and *c* arrows cost *d* per qian.
"""

# Total money spent
total_money = 980

# Total arrows purchased
total_arrows = 5820

# Assume the expensive arrows cost 3 per qian, and the cheap arrows cost 5 per qian
expensive_price = 3
cheap_price = 5

# Let the number of expensive arrows be x, and the number of cheap arrows be y
# Solve the system of equations:
# x + y = total_arrows
# x / expensive_price + y / cheap_price = total_money

# Using substitution:
# y = total_arrows - x
# Substitute into the second equation:
# x / expensive_price + (total_arrows - x) / cheap_price = total_money

from fractions import Fraction

x = Fraction(total_money * cheap_price - total_arrows, cheap_price - expensive_price)
y = total_arrows - x

# Calculate the number of arrows and their price ratios
a = x
b = expensive_price
c = y
d = cheap_price

a, b, c, d
"""
Variable 'a' has wrong value. Expected: 300, Actual: -460
Variable 'b' has wrong value. Expected: 5, Actual: 3
Variable 'c' has wrong value. Expected: 5520, Actual: 6280
Variable 'd' has wrong value. Expected: 6, Actual: 5"""
