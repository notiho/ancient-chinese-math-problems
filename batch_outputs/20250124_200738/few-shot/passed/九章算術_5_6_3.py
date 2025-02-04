"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
荅曰：四千三百七十五尺。
春程人功七百六十六尺，并出土功五分之一，定功六百一十二尺、五分尺之四。問︰用徒幾何？
術曰：置本人功，去其五分之一，餘為法。以溝積尺為實。實如法而一，得用徒人數。
荅曰： a人 。
"""

#----- content starts here -----
"""
Suppose there is a ditch with an upper width of 1 zhang 5 chi, a lower width of 1 zhang, a depth of 5 chi, and a length of 7 zhang.
Question: what is the volume?

Answer: 4375 chi³.

For spring labor, one person can dig 766 chi³, including 1/5 for removing the soil. The effective labor is 612 chi³ and 4/5 chi³.
Question: how many workers are needed?

The procedure says: Place the effective labor of one person, removing 1/5, and the remainder is the divisor.
Take the volume of the ditch as the dividend.
Divide the dividend by the divisor to obtain the number of workers required.

Answer: *a* workers.
"""

from fractions import Fraction

# 溝上廣一丈五尺
上廣 = 1 * 10 + 5  # Convert zhang and chi to chi

# 下廣一丈
下廣 = 1 * 10  # Convert zhang to chi

# 深五尺
深 = 5  # chi

# 袤七丈
袤 = 7 * 10  # Convert zhang to chi

# 計算溝積
# 溝積公式：積 = ((上廣 + 下廣) / 2) * 深 * 袤
溝積 = Fraction((上廣 + 下廣), 2) * 深 * 袤

# 春程人功七百六十六尺
本人功 = 766

# 去其五分之一
有效功 = 本人功 * Fraction(4, 5)

# 以溝積尺為實
實 = 溝積

# 實如法而一，得用徒人數
a = Fraction(實, 有效功)  # Number of workers required#----- content ends here -----

"""
"""
