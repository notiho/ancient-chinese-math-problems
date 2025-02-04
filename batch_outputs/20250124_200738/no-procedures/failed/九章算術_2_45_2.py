"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
荅曰：其 a枚 ， b枚 一錢 其 c枚 ， d枚 一錢
"""

#----- content starts here -----
"""
Suppose 980 qian (units of money) are spent to buy 5820 arrows. The arrows are of two types: expensive and cheap.
Question: what is the price ratio of the expensive and cheap arrows?

Answer: *a* arrows for *b* qian, and *c* arrows for *d* qian.
"""

# Total money spent
total_money = 980

# Total arrows purchased
total_arrows = 5820

# Assume the expensive arrows are sold at 3 arrows per qian
# Assume the cheap arrows are sold at 7 arrows per qian

# Let x be the number of expensive arrows, and y be the number of cheap arrows
# x + y = total_arrows
# (x / 3) + (y / 7) = total_money

# Solve for x and y
from fractions import Fraction

# Expensive arrows per qian
expensive_rate = 3

# Cheap arrows per qian
cheap_rate = 7

# Solve for x (expensive arrows)
x = Fraction(total_money * cheap_rate - total_arrows, cheap_rate - expensive_rate)

# Solve for y (cheap arrows)
y = total_arrows - x

# Calculate the price ratio
a, b = expensive_rate, 1  # Expensive arrows: 3 arrows per qian
c, d = cheap_rate, 1      # Cheap arrows: 7 arrows per qian

# Output results
a, b, c, d#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 300, Actual: 3
Variable 'b' has wrong value. Expected: 5, Actual: 1
Variable 'c' has wrong value. Expected: 5520, Actual: 7
Variable 'd' has wrong value. Expected: 6, Actual: 1"""
