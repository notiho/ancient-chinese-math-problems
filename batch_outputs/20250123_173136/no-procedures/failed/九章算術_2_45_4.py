"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
荅曰：其 a枚 ， b枚 一錢 其 c枚 ， d枚 一錢
"""

"""
Suppose there is a total of 980 qian spent to buy 5820 arrows. The arrows are of two types: expensive and cheap. 
The goal is to determine the rate (number of arrows per qian) for each type of arrow.

Answer: The expensive arrows are *a* arrows per *b* qian, and the cheap arrows are *c* arrows per *d* qian.
"""

# Total money and arrows
total_money = 980
total_arrows = 5820

# Assume the expensive arrows are 3 arrows per 1 qian
expensive_rate = Fraction(3, 1)  # 3 arrows per 1 qian

# Assume the cheap arrows are 7 arrows per 1 qian
cheap_rate = Fraction(7, 1)  # 7 arrows per 1 qian

# Let x be the number of qian spent on expensive arrows
# Let y be the number of qian spent on cheap arrows
# x + y = total_money
# (3x + 7y = total_arrows)

# Solve for x and y
x = Fraction(total_arrows - (cheap_rate * total_money), expensive_rate - cheap_rate)
y = total_money - x

# Calculate the number of arrows for each type
expensive_arrows = expensive_rate * x
cheap_arrows = cheap_rate * y

# Output the rates
a, b = 3, 1  # Expensive arrows: 3 arrows per 1 qian
c, d = 7, 1  # Cheap arrows: 7 arrows per 1 qian
"""
Variable 'a' has wrong value. Expected: 300, Actual: 3
Variable 'b' has wrong value. Expected: 5, Actual: 1
Variable 'c' has wrong value. Expected: 5520, Actual: 7
Variable 'd' has wrong value. Expected: 6, Actual: 1"""
