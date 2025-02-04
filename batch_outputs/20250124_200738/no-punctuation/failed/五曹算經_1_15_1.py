"""
今有田形如牛角從五十步口廣二十步問為田㡬何
術曰列口廣二十步半之得十步以從五十步乘之得五百步以畝法除之即得
答曰 a畝 奇 b步 
"""

#----- content starts here -----
"""
Suppose there is a field shaped like a cow's horn. The length is 50 bu, and the width at the mouth is 20 bu.
Question: how large is the field?

The procedure says: Take the width at the mouth, 20 bu, and halve it, obtaining 10 bu.
Multiply it by the length, 50 bu, obtaining 500 bu.
Divide this by the mu-divisor, 240, to obtain the result.

Answer: *a* mu and *b* bu.
"""

# 口廣二十步
口廣 = 20

# 半之得十步
半口廣 = 口廣 / 2

# 從五十步
從 = 50

# 以從五十步乘之，得五百步
積步 = 半口廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之，即得
畝數 = Fraction(積步, 畝法)

# 分解為整畝和餘步
a = 畝數.numerator // 畝數.denominator  # 整畝
b = 畝數.numerator % 畝數.denominator  # 餘步#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
