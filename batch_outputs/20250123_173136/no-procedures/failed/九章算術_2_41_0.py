"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤斤率之，問︰各幾何？
荅曰：其 a石 ，斤 b錢 。其 c斤 ，斤 d錢 。
"""

"""
Suppose there is 13,970 qian spent to buy 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu of silk.
It is desired to calculate the price per jin (pound) of silk.

Answer: For *a* shi, the price per jin is *b* qian. For *c* jin, the price per jin is *d* qian.
"""

# Total money spent
total_money = 13970  # in qian

# Conversion factors
shi_to_jin = 120  # 1 shi = 120 jin
jun_to_jin = 20   # 1 jun = 20 jin
liang_to_jin = Fraction(1, 16)  # 1 liang = 1/16 jin
zhu_to_jin = Fraction(1, 384)   # 1 zhu = 1/384 jin

# Total weight in jin
total_weight = (
    1 * shi_to_jin +  # 1 shi
    2 * jun_to_jin +  # 2 jun
    28 +              # 28 jin
    3 * liang_to_jin +  # 3 liang
    5 * zhu_to_jin      # 5 zhu
)

# Price per jin
price_per_jin = Fraction(total_money, total_weight)

# Results
a = 1  # For 1 shi
b = price_per_jin  # Price per jin for 1 shi
c = 1  # For 1 jin
d = price_per_jin  # Price per jin for 1 jin

# Final results
a, b, c, d
"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 1
Variable 'b' has wrong value. Expected: 67, Actual: 5364480/72269
Variable 'c' has wrong value. Expected: 7897/384, Actual: 1
Variable 'd' has wrong value. Expected: 68, Actual: 5364480/72269"""
