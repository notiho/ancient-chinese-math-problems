"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
荅曰：四千三百七十五尺。
春程人功七百六十六尺，并出土功五分之一，定功六百一十二尺、五分尺之四。問︰用徒幾何？
術曰：置本人功，去其五分之一，餘為法。以溝積尺為實。實如法而一，得用徒人數。
荅曰： a人 。
"""

"""
Suppose there is a ditch with an upper width of 1 zhang 5 chi, a lower width of 1 zhang, a depth of 5 chi, and a length of 7 zhang.
Question: what is the volume?

Answer: 4375 chi³.

The labor capacity of one person is 766 chi³, including an additional one-fifth for the effort of removing the excavated soil.
The adjusted capacity is 612 chi³ and 4/5 chi³.
Question: how many workers are needed?

The procedure says: Place the capacity of one person, remove one-fifth of it, and the remainder becomes the divisor.
Take the ditch volume as the dividend.
Divide the dividend by the divisor to obtain the number of workers needed.

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
# 溝積公式: 積 = (上廣 + 下廣) * 深 / 2 * 袤
溝積 = Fraction((上廣 + 下廣) * 深, 2) * 袤

# 本人功七百六十六尺
本人功 = 766

# 并出土功五分之一
出土功 = Fraction(1, 5) * 本人功

# 定功 = 本人功 - 出土功
定功 = 本人功 - 出土功

# 置本人功，去其五分之一，餘為法
法 = 定功

# 以溝積尺為實
實 = 溝積

# 實如法而一，得用徒人數
a = Fraction(實, 法)
"""
"""
