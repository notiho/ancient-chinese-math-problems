"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
荅曰：其 a枚 ， b枚 一錢 其 c枚 ， d枚 一錢
"""

"""
Suppose 980 qian (units of money) are spent to buy 5820 arrows. The arrows are of two types: expensive and cheap.
Question: what is the price ratio of the expensive and cheap arrows?

Answer: *a* arrows, *b* arrows per qian for the expensive type; *c* arrows, *d* arrows per qian for the cheap type.
"""

# Total money spent
total_money = 980

# Total arrows purchased
total_arrows = 5820

# Assume the expensive arrows cost 3 arrows per qian, and the cheap arrows cost 7 arrows per qian.
# Let x be the number of expensive arrows, and y be the number of cheap arrows.

# Expensive arrows cost 3 arrows per qian
expensive_rate = 3

# Cheap arrows cost 7 arrows per qian
cheap_rate = 7

# Solve for the number of expensive and cheap arrows
# x + y = total_arrows
# x / expensive_rate + y / cheap_rate = total_money

from fractions import Fraction

# Solve for x (expensive arrows)
x = Fraction(total_money * cheap_rate - total_arrows, cheap_rate - expensive_rate)

# Solve for y (cheap arrows)
y = total_arrows - x

# Calculate the number of arrows per qian for each type
a = x
b = expensive_rate
c = y
d = cheap_rate

a, b, c, d
"""
Variable 'a' has wrong value. Expected: 300, Actual: 260
Variable 'b' has wrong value. Expected: 5, Actual: 3
Variable 'c' has wrong value. Expected: 5520, Actual: 5560
Variable 'd' has wrong value. Expected: 6, Actual: 7"""
