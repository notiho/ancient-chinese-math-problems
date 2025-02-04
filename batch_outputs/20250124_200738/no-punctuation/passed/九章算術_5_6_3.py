"""
今有溝上廣一丈五尺下廣一丈深五尺袤七丈問積幾何
荅曰四千三百七十五尺
春程人功七百六十六尺并出土功五分之一定功六百一十二尺五分尺之四問用徒幾何
術曰置本人功去其五分之一餘為法以溝積尺為實實如法而一得用徒人數
荅曰 a人 
"""

#----- content starts here -----
"""
Suppose there is a ditch with the top width of 1 zhang and 5 chi, the bottom width of 1 zhang, the depth of 5 chi, and the length of 7 zhang.
Question: what is the volume?

Answer: 4375 cubic chi.

The labor calculation says: Spring labor per person is 766 cubic chi, including the effort of removing soil, which is 1/5 of the total. The effective labor is 612 and 4/5 cubic chi.
Question: how many workers are needed?

The procedure says: Place the labor per person, subtract 1/5, and the remainder becomes the divisor.
Take the ditch volume in cubic chi as the dividend.
Divide the dividend by the divisor, and the result is the number of workers.

Answer: *a* workers.
"""

from fractions import Fraction

# 溝上廣一丈五尺
上廣 = 1 * 10 + 5  # Convert zhang to chi

# 下廣一丈
下廣 = 1 * 10  # Convert zhang to chi

# 深五尺
深 = 5

# 袤七丈
袤 = 7 * 10  # Convert zhang to chi

# 計算溝積
溝積 = Fraction((上廣 + 下廣) * 深 * 袤, 2)  # Trapezoidal volume formula

# 本人功七百六十六尺
本人功 = 766

# 去其五分之一，餘為法
法 = 本人功 - Fraction(本人功, 5)

# 以溝積尺為實
實 = 溝積

# 實如法而一，得用徒人數
a = Fraction(實, 法)

a#----- content ends here -----

"""
"""
