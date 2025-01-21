"""
今有田形如牛角從五十步口廣二十步。問：為田㡬何？
術曰：列口廣二十步半之得十步以從五十步乘之得五百步以畝法除之即得。
答曰： a(=2)畝 奇 b(=20)步 。
"""

"""
Suppose there is a field shaped like a bull's horn, with a length of 50 bu and a mouth width of 20 bu.
Question: how large is the field?

The procedure says: Take the mouth width of 20 bu, halve it, obtaining 10 bu.
Multiply this by the length of 50 bu, obtaining 500 bu.
Divide it by the mu-divisor, and the result is obtained.

Answer: *a*(=2) mu and *b*(=20) bu.
"""

# 口廣二十步
口廣 = 20

# 半之得十步
半口廣 = 口廣 / 2

# 從五十步
從 = 50

# 以從五十步乘之得五百步
積步 = 半口廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 分解為整畝和餘步
a = 畝數.numerator // 畝數.denominator  # 整畝數 (2)
b = 積步 % 畝法  # 餘步數 (20)
"""
Code error: both arguments should be Rational instances"""
