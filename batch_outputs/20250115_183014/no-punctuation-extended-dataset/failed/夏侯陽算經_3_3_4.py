"""
今有金一斤直錢一百貫問一兩幾何
術曰置錢數以十六兩除之即得
答曰 a兩 b貫
"""

"""
Suppose there is 1 jin of gold, worth 100 guan of coins.
Question: how much is 1 liang worth?

The procedure says: Place the number of coins and divide it by 16 liang, then the result is obtained.

Answer: *a* liang and *b* guan.
"""

# 金一斤直錢一百貫
錢數 = 100  # 貫 (1 貫 = 1000 錢)

# 一斤 = 16兩
兩數 = 16

# 置錢數以十六兩除之即得
每兩價值 = Fraction(錢數, 兩數)

# 分解為貫和錢
a = 每兩價值.numerator // 每兩價值.denominator  # 貫
b = 每兩價值 - a  # 剩餘部分 in 貫

a貫 = a
b貫 = b
"""
Variable 'a' has wrong value. Expected: 1, Actual: 6
Variable 'b' has wrong value. Expected: 25/4, Actual: 1/4"""
