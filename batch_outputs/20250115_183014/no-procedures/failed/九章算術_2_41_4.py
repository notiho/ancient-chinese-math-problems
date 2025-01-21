"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤斤率之，問︰各幾何？
荅曰：其 a石 ，斤 b錢 。其 c斤 ，斤 d錢 。
"""

"""
Suppose 13,970 qian is spent to buy 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu of silk.  
It is desired to calculate the price per jin (斤) of silk.

Answer: For *a* shi, the price per jin is *b* qian.  
For *c* jin, the price per jin is *d* qian.
"""

# Total money spent
total_money = 13970  # in qian

# Total weight of silk
# 1 shi = 120 jin, 1 jun = 20 jin, 1 liang = 1/16 jin, 1 zhu = 1/384 jin
total_weight = (
    1 * 120  # shi to jin
    + 2 * 20  # jun to jin
    + 28  # jin
    + Fraction(3, 16)  # liang to jin
    + Fraction(5, 384)  # zhu to jin
)

# Price per jin
price_per_jin = Fraction(total_money, total_weight)

# For 1 shi (120 jin), calculate the price
a = 1  # shi
b = price_per_jin * 120  # price for 1 shi (120 jin)

# For 1 jin, calculate the price
c = 1  # jin
d = price_per_jin  # price for 1 jin

# Final results
a, b, c, d
"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 1
Variable 'b' has wrong value. Expected: 67, Actual: 643737600/72269
Variable 'c' has wrong value. Expected: 7897/384, Actual: 1
Variable 'd' has wrong value. Expected: 68, Actual: 5364480/72269"""
