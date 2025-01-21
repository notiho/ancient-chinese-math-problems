"""
今有金一斤直錢一百貫問一兩幾何
術曰置錢數以十六兩除之即得
答曰 a兩 b貫
"""

"""
Suppose there is 1 jin of gold worth 100 guan of money.
Question: how much is 1 liang worth?

The procedure says: Place the amount of money and divide it by 16 liang, then you obtain the value.

Answer: *a* liang and *b* guan.
"""

# 金一斤直錢一百貫
錢數 = 100  # 貫
一斤 = 16  # 16 兩 in 1 斤

# 以十六兩除之
每兩價值 = Fraction(錢數, 一斤)

# 分解為兩和貫
a = 每兩價值.numerator  # Liang (whole part)
b = 每兩價值.denominator  # Guan (fractional part)
"""
Variable 'a' has wrong value. Expected: 1, Actual: 25
Variable 'b' has wrong value. Expected: 25/4, Actual: 4"""
