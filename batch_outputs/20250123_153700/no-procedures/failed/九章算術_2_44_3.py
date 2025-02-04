"""
今有出錢六百一十，買羽二千一百翭。欲其貴賤率之，問︰各幾何？
荅曰：其 a翭 ， b翭 一錢 其 c翭 ， d翭 一錢
"""

"""
Suppose 610 qian (coins) are spent to buy 2100 hou (feathers). It is desired to determine the rate of expensive and cheap feathers.
Question: what are the rates for each?

Answer: *a* hou at *b* hou per qian, and *c* hou at *d* hou per qian.
"""

# Total money spent
total_money = 610

# Total feathers bought
total_feathers = 2100

# Expensive feathers: 3 hou per qian
expensive_rate = 3

# Cheap feathers: 5 hou per qian
cheap_rate = 5

# Let the number of expensive feathers be `a` and cheap feathers be `c`
# Solve the system of equations:
# a + c = total_feathers
# (a / expensive_rate) + (c / cheap_rate) = total_money

# Using substitution:
# c = total_feathers - a
# (a / expensive_rate) + ((total_feathers - a) / cheap_rate) = total_money

from fractions import Fraction

# Solve for `a` (expensive feathers)
a = Fraction(total_money * cheap_rate - total_feathers, cheap_rate - expensive_rate)

# Solve for `c` (cheap feathers)
c = total_feathers - a

# Calculate the rates
b = expensive_rate
d = cheap_rate

# Final results
a, b, c, d
"""
Variable 'a' has wrong value. Expected: 1140, Actual: 475
Variable 'c' has wrong value. Expected: 960, Actual: 1625
Variable 'd' has wrong value. Expected: 4, Actual: 5"""
