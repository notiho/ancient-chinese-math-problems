"""
今有溝上廣一丈五尺下廣一丈深五尺袤七丈問積幾何
荅曰四千三百七十五尺
春程人功七百六十六尺并出土功五分之一定功六百一十二尺五分尺之四問用徒幾何
術曰置本人功去其五分之一餘為法以溝積尺為實實如法而一得用徒人數
荅曰 a人 
"""

"""
Suppose there is a ditch with an upper width of 1 zhang 5 chi, a lower width of 1 zhang, a depth of 5 chi, and a length of 7 zhang.
Question: what is the volume?

Answer: 4375 cubic chi.

The labor required for spring work is 766 cubic chi, including the effort for removing soil, which is 1/5 of the total.
The effective labor per person is 612.8 cubic chi (or 612 chi and 4/5 chi).
Question: how many workers are needed?

The procedure says: Place the labor per person, subtracting 1/5, and the remainder becomes the divisor.
Take the ditch volume in cubic chi as the dividend.
Divide the dividend by the divisor, obtaining the number of workers required.

Answer: *a* workers.
"""

from fractions import Fraction

# 溝上廣一丈五尺
上廣 = 1 * 10 + 5  # Convert to chi

# 下廣一丈
下廣 = 1 * 10  # Convert to chi

# 深五尺
深 = 5  # In chi

# 袤七丈
袤 = 7 * 10  # Convert to chi

# 計算溝積幾何
# 溝積公式: 積 = (上廣 + 下廣) * 深 * 袤 / 2
溝積 = (上廣 + 下廣) * 深 * 袤 / 2

# 確認溝積
assert 溝積 == 4375, "Calculated volume does not match the given value."

# 春程人功七百六十六尺
春程人功 = 766

# 去其五分之一
有效人功 = 春程人功 * Fraction(4, 5)

# 確認有效人功
assert 有效人功 == Fraction(612, 1) + Fraction(4, 5), "Effective labor per person does not match the given value."

# 以溝積尺為實
實 = 溝積

# 餘為法
法 = 有效人功

# 實如法而一，得用徒人數
a = Fraction(實, 法)  # Number of workers required
"""
Code error: both arguments should be Rational instances"""
