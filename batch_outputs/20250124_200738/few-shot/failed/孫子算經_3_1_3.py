"""
今有丁一千五百萬，出兵四十萬。問：幾丁科一兵？
術曰：置丁一千五百萬為實，以兵四十萬為法，實如法，即得。
答曰： a 丁 b分 。
"""

#----- content starts here -----
"""
Suppose there are 15,000,000 adult males (丁), and 400,000 soldiers are to be conscripted.
Question: how many adult males are required to provide one soldier?

The procedure says: Place the 15,000,000 adult males as the dividend.
Take the 400,000 soldiers as the divisor.
Divide the dividend by the divisor, and the result is obtained.

Answer: *a* adult males and *b* fractional parts.
"""

# 置丁一千五百萬為實
丁 = 15000000

# 以兵四十萬為法
兵 = 400000

# 實如法，即得
result = Fraction(丁, 兵)

# 分解為整數部分和分數部分
a = result.numerator // result.denominator  # 整數部分
b = Fraction(result.numerator % result.denominator, result.denominator)  # 分數部分#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 5, Actual: 1/2"""
