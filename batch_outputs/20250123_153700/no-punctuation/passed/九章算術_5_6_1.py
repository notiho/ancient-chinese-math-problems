"""
今有溝上廣一丈五尺下廣一丈深五尺袤七丈問積幾何
荅曰四千三百七十五尺
春程人功七百六十六尺并出土功五分之一定功六百一十二尺五分尺之四問用徒幾何
術曰置本人功去其五分之一餘為法以溝積尺為實實如法而一得用徒人數
荅曰 a人 
"""

"""
Suppose there is a ditch with the top width of 1 zhang 5 chi, the bottom width of 1 zhang, the depth of 5 chi, and the length of 7 zhang.
Question: what is the volume of the ditch?

Answer: 4375 cubic chi.

The second part asks: If the spring labor rate is 766 cubic chi per person, including 1/5 for removing soil, the effective labor rate is 612 and 4/5 cubic chi per person. 
Question: how many workers are needed?

The procedure says: Place the original labor rate and remove 1/5 of it; the remainder is the divisor.
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
深 = 5  # Already in chi

# 袤七丈
袤 = 7 * 10  # Convert to chi

# 計算溝積
# 溝積公式: 積 = (上廣 + 下廣) / 2 * 深 * 袤
溝積 = Fraction((上廣 + 下廣), 2) * 深 * 袤

# 確認溝積
assert 溝積 == 4375  # Given in the problem

# 春程人功七百六十六尺
本人功 = 766

# 去其五分之一
有效人功 = 本人功 - Fraction(1, 5) * 本人功

# 餘為法
法 = 有效人功

# 以溝積尺為實
實 = 溝積

# 實如法而一，得用徒人數
a = Fraction(實, 法)

# Final answer
a
"""
"""
