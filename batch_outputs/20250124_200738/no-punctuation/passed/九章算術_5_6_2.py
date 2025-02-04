"""
今有溝上廣一丈五尺下廣一丈深五尺袤七丈問積幾何
荅曰四千三百七十五尺
春程人功七百六十六尺并出土功五分之一定功六百一十二尺五分尺之四問用徒幾何
術曰置本人功去其五分之一餘為法以溝積尺為實實如法而一得用徒人數
荅曰 a人 
"""

#----- content starts here -----
"""
Suppose there is a ditch with an upper width of 1 zhang 5 chi, a lower width of 1 zhang, a depth of 5 chi, and a length of 7 zhang.
Question 1: What is the volume of the ditch?
Answer: 4375 chi³.

The labor calculation says: Spring labor per person is 766 chi³, including 1/5 for removing soil. The effective labor per person is 612 chi³ and 4/5 of a chi³.
Question 2: How many workers are needed?

The procedure says: Place the effective labor per person, removing 1/5, and the remainder is the divisor.
Take the ditch volume in chi³ as the dividend.
Divide the dividend by the divisor, obtaining the number of workers needed.

Answer: *a* workers.
"""

from fractions import Fraction

# 溝上廣一丈五尺
上廣 = 1 * 10 + 5  # Convert zhang and chi to chi

# 下廣一丈
下廣 = 1 * 10  # Convert zhang to chi

# 深五尺
深 = 5

# 袤七丈
袤 = 7 * 10  # Convert zhang to chi

# 問積幾何 (Calculate the volume of the ditch)
# Volume formula for a trapezoidal prism: (上廣 + 下廣) / 2 * 深 * 袤
溝積 = Fraction((上廣 + 下廣), 2) * 深 * 袤

# Verify the given answer
assert 溝積 == 4375  # The given volume is correct

# 春程人功七百六十六尺
本人功 = 766

# 并出土功五分之一 (Remove 1/5 for soil removal)
有效人功 = 本人功 * Fraction(4, 5)

# 問用徒幾何 (Calculate the number of workers needed)
a = 溝積 / 有效人功

# Final answer
a#----- content ends here -----

"""
"""
