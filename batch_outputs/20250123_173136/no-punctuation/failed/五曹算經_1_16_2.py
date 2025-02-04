"""
今有圓田周七十八步徑二十六步問為田㡬何
術曰先列周七十八步半之得三十九步又列徑二十六步半之得一十三步二位相乘得五百七步以畝法除之即得
答曰 a畝 奇 b步 
"""

"""
Suppose there is a circular field with a circumference of 78 bu and a diameter of 26 bu.
Question: how large is the field?

The procedure says: First, take the circumference of 78 bu and halve it, obtaining 39 bu.
Then, take the diameter of 26 bu and halve it, obtaining 13 bu.
Multiply these two values together, obtaining 507 bu.
Divide this by the mu-divisor (240), and the result is the area.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# 圓田周七十八步
周 = 78

# 徑二十六步
徑 = 26

# 周七十八步半之
半周 = Fraction(周, 2)

# 徑二十六步半之
半徑 = Fraction(徑, 2)

# 二位相乘得五百七步
積步 = 半周 * 半徑

# 畝法二百四十步
畝法 = 240

# 以畝法除之
畝數 = Fraction(積步, 畝法)

# 分離整數部分和餘數部分
a = 畝數.numerator // 畝數.denominator  # 整數部分為畝
b = 畝數.numerator % 畝數.denominator  # 餘數部分為步
"""
Variable 'b' has wrong value. Expected: 27, Actual: 9"""
