"""
今有錢二百三十八貫五百七十三文足欲為九十二陌問得㡬何
術曰列錢二百三十八貫五百七十三文足以九十二除之即得
答曰 a貫 奇足錢 b分 
"""

"""
Suppose there is 238 guan and 573 wen of money. It is desired to convert this into 92 mo.
Question: how much does one obtain?

The procedure says: Place the money, 238 guan and 573 wen. Divide it by 92, and the result is obtained.

Answer: *a* guan and *b* fractional parts of guan.
"""

from fractions import Fraction

# 錢二百三十八貫五百七十三文足
錢 = 238 + Fraction(573, 1000)  # Convert 573 wen into fractional guan (1 guan = 1000 wen)

# 欲為九十二陌
陌 = 92

# 以九十二除之即得
result = Fraction(錢, 陌)

# 分解結果為貫和餘分
a = result.numerator // result.denominator  # 整數部分為貫
b = Fraction(result.numerator % result.denominator, result.denominator)  # 餘分部分

a, b
"""
Variable 'a' has wrong value. Expected: 129659/500, Actual: 2
Variable 'b' has wrong value. Expected: 22/5, Actual: 54573/92000"""
