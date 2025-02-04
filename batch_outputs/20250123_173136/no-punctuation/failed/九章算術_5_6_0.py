"""
今有溝上廣一丈五尺下廣一丈深五尺袤七丈問積幾何
荅曰四千三百七十五尺
春程人功七百六十六尺并出土功五分之一定功六百一十二尺五分尺之四問用徒幾何
術曰置本人功去其五分之一餘為法以溝積尺為實實如法而一得用徒人數
荅曰 a人 
"""

"""
Suppose there is a trench with an upper width of 1 zhang 5 chi, a lower width of 1 zhang, a depth of 5 chi, and a length of 7 zhang.
Question 1: What is the volume of the trench?
Answer: 4375 cubic chi.

Additionally, the spring labor rate is 766 cubic chi, including 1/5 for removing soil. The effective labor rate is 612 and 4/5 cubic chi.
Question 2: How many workers are needed?

The procedure says: Place the effective labor rate, removing 1/5, and the remainder becomes the divisor.
Take the trench volume in cubic chi as the dividend.
Divide the dividend by the divisor, obtaining the number of workers.

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

# 計算溝積
# 溝積公式：積 = (上廣 + 下廣) * 深 * 袤 / 2
溝積 = (上廣 + 下廣) * 深 * 袤 / 2

# 確認溝積
assert 溝積 == 4375  # Given in the problem

# 春程人功七百六十六尺
春程人功 = 766

# 并出土功五分之一
出土功 = Fraction(1, 5) * 春程人功

# 定功六百一十二尺五分尺之四
定功 = 春程人功 - 出土功

# 置本人功去其五分之一餘為法
法 = 定功

# 以溝積尺為實
實 = 溝積

# 實如法而一得用徒人數
a = Fraction(實, 法)

# Answer
a
"""
Code error: both arguments should be Rational instances"""
