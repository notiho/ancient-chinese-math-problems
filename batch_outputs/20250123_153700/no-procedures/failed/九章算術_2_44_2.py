"""
今有出錢六百一十，買羽二千一百翭。欲其貴賤率之，問︰各幾何？
荅曰：其 a翭 ， b翭 一錢 其 c翭 ， d翭 一錢
"""

"""
Suppose 610 qian (coins) are spent to buy 2100 hou (feathers). The feathers are of two types: expensive and cheap.
Question: how many of each type of feather are there, and what is the price ratio?

Answer: *a* hou at *b* hou per qian, and *c* hou at *d* hou per qian.
"""

# Total money spent
total_money = 610

# Total feathers bought
total_feathers = 2100

# Let the expensive feathers cost 3 hou per qian
expensive_rate = 3

# Let the cheap feathers cost 5 hou per qian
cheap_rate = 5

# Solve for the number of expensive and cheap feathers
# Let x be the number of expensive feathers, and y be the number of cheap feathers
# x + y = total_feathers
# x / expensive_rate + y / cheap_rate = total_money

from fractions import Fraction

# Solve for x (expensive feathers)
x = Fraction(total_money * cheap_rate - total_feathers, cheap_rate - expensive_rate)

# Solve for y (cheap feathers)
y = total_feathers - x

# Assign results
a = x
b = expensive_rate
c = y
d = cheap_rate

# Results
a, b, c, d
"""
Variable 'a' has wrong value. Expected: 1140, Actual: 475
Variable 'c' has wrong value. Expected: 960, Actual: 1625
Variable 'd' has wrong value. Expected: 4, Actual: 5"""
