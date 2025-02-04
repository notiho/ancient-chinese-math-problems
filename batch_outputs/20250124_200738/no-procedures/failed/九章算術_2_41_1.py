"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤斤率之，問︰各幾何？
荅曰：其 a石 ，斤 b錢 。其 c斤 ，斤 d錢 。
"""

#----- content starts here -----
"""
Suppose there is a total of 13,970 qian spent to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
It is desired to calculate the price per jin (斤) of silk.

Answer: For every *a* shi, the price per jin is *b* qian.
For every *c* jin, the price per jin is *d* qian.
"""

# Conversion factors
shi_to_jin = 120  # 1 石 = 120 斤
jun_to_jin = 20   # 1 鈞 = 20 斤
liang_to_jin = Fraction(1, 16)  # 1 兩 = 1/16 斤
zhu_to_jin = Fraction(1, 384)  # 1 銖 = 1/384 斤

# Total weight in jin
weight_in_jin = (
    1 * shi_to_jin +  # 1 石
    2 * jun_to_jin +  # 2 鈞
    28 +              # 28 斤
    3 * liang_to_jin +  # 3 兩
    5 * zhu_to_jin     # 5 銖
)

# Total money spent
total_qian = 13970

# Price per jin
price_per_jin = Fraction(total_qian, weight_in_jin)

# Answer
a = 1  # For every 1 shi
b = price_per_jin  # Price per jin in qian
c = 1  # For every 1 jin
d = price_per_jin  # Price per jin in qian

# Final results
a, b, c, d#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 1
Variable 'b' has wrong value. Expected: 67, Actual: 5364480/72269
Variable 'c' has wrong value. Expected: 7897/384, Actual: 1
Variable 'd' has wrong value. Expected: 68, Actual: 5364480/72269"""
