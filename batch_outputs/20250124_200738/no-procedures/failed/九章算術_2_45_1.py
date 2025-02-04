"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
荅曰：其 a枚 ， b枚 一錢 其 c枚 ， d枚 一錢
"""

#----- content starts here -----
"""
Suppose 980 qian (units of money) are spent to buy 5820 arrows. It is desired to determine the price ratio of expensive and cheap arrows.
Question: how many of each type are there, and what is the price ratio?

Answer: *a* arrows at *b* arrows per qian, and *c* arrows at *d* arrows per qian.
"""

# Total money spent
total_money = 980

# Total arrows purchased
total_arrows = 5820

# Assume the expensive arrows are sold at 3 arrows per qian
expensive_rate = 3  # 3 arrows per qian

# Assume the cheap arrows are sold at 7 arrows per qian
cheap_rate = 7  # 7 arrows per qian

# Let the number of expensive arrows be x, and the number of cheap arrows be y
# We know:
# x + y = total_arrows
# (x / expensive_rate) + (y / cheap_rate) = total_money

# Solve for x and y
from fractions import Fraction

# Using substitution:
# y = total_arrows - x
# (x / expensive_rate) + ((total_arrows - x) / cheap_rate) = total_money

# Multiply through by the common denominator (expensive_rate * cheap_rate)
common_denominator = expensive_rate * cheap_rate
x = Fraction(
    total_money * common_denominator - (total_arrows * cheap_rate),
    expensive_rate - cheap_rate,
)
y = total_arrows - x

# Calculate the number of arrows per qian for each type
a, b = x, expensive_rate
c, d = y, cheap_rate

a, b, c, d#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 300, Actual: 5040
Variable 'b' has wrong value. Expected: 5, Actual: 3
Variable 'c' has wrong value. Expected: 5520, Actual: 780
Variable 'd' has wrong value. Expected: 6, Actual: 7"""
