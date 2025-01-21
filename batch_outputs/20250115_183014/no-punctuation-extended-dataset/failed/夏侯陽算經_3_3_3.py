"""
今有金一斤直錢一百貫問一兩幾何
術曰置錢數以十六兩除之即得
答曰 a兩 b貫
"""

"""
Suppose there is 1 jin of gold worth 100 guan of money.
Question: how much is 1 liang worth?

The procedure says: Place the amount of money and divide it by 16 liang, then the result is obtained.

Answer: *a* liang and *b* guan.
"""

# 金一斤直錢一百貫
錢數 = 100  # 貫

# 一斤等於十六兩
兩數 = 16

# 置錢數以十六兩除之即得
每兩價值 = Fraction(錢數, 兩數)

# 分解為貫和餘數
a = 每兩價值.numerator // 每兩價值.denominator  # 整數部分 (貫)
b = Fraction(每兩價值.numerator % 每兩價值.denominator, 每兩價值.denominator)  # 餘數部分 (貫)
"""
Variable 'a' has wrong value. Expected: 1, Actual: 6
Variable 'b' has wrong value. Expected: 25/4, Actual: 1/4"""
