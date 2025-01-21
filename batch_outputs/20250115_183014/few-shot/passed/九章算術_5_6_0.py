"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
荅曰：四千三百七十五尺。
春程人功七百六十六尺，并出土功五分之一，定功六百一十二尺、五分尺之四。問︰用徒幾何？
術曰：置本人功，去其五分之一，餘為法。以溝積尺為實。實如法而一，得用徒人數。
荅曰： a人 。
"""

"""
Suppose there is a ditch with an upper width of 1 zhang and 5 chi, a lower width of 1 zhang, a depth of 5 chi, and a length of 7 zhang.
Question: what is the volume?

Answer: 4375 cubic chi.

The labor required for spring digging is 766 cubic chi per person, including an additional one-fifth for removing the excavated soil. The adjusted labor per person is 612 and 4/5 cubic chi.
Question: how many workers are needed?

The procedure says: Place the labor per person, subtract one-fifth of it, and the remainder becomes the divisor.
Take the ditch volume in cubic chi as the dividend.
Divide the dividend by the divisor to obtain the number of workers needed.

Answer: *a* workers.
"""

# 溝上廣一丈五尺
上廣 = 1 * 10 + 5  # Convert to chi

# 下廣一丈
下廣 = 1 * 10  # Convert to chi

# 深五尺
深 = 5  # chi

# 袤七丈
袤 = 7 * 10  # Convert to chi

# 計算溝積
# 溝積公式: ((上廣 + 下廣) / 2) * 深 * 袤
溝積 = Fraction((上廣 + 下廣), 2) * 深 * 袤

# 本人功七百六十六尺
本人功 = Fraction(766)

# 去其五分之一
去五分之一 = 本人功 * Fraction(1, 5)

# 餘為法
法 = 本人功 - 去五分之一

# 以溝積尺為實
實 = 溝積

# 實如法而一，得用徒人數
a = Fraction(實, 法)  # Number of workers needed
"""
"""
