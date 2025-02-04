"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
荅曰：四千三百七十五尺。
春程人功七百六十六尺，并出土功五分之一，定功六百一十二尺、五分尺之四。問︰用徒幾何？
術曰：置本人功，去其五分之一，餘為法。以溝積尺為實。實如法而一，得用徒人數。
荅曰： a(=21875/3064)人 。
"""

#----- content starts here -----
"""
Suppose there is a ditch with an upper width of 1 zhang 5 chi, a lower width of 1 zhang, a depth of 5 chi, and a length of 7 zhang.
Question: what is the volume?

Answer: 4375 cubic chi.

The labor capacity of a person is 766 cubic chi, including 1/5 for removing the soil, leaving 612 4/5 cubic chi as the effective labor capacity.
Question: how many workers are needed?

The procedure says: Place the effective labor capacity of a person, removing 1/5, and the remainder becomes the divisor.
Take the volume of the ditch as the dividend.
Divide the dividend by the divisor to obtain the number of workers needed.

Answer: *a*(=21875/3064) persons.
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

# 積幾何？
# Trapezoidal area formula: ((上廣 + 下廣) / 2) * 深
橫截面積 = Fraction((上廣 + 下廣), 2) * 深

# Volume = cross-sectional area * length
溝積 = 橫截面積 * 袤  # 4375 cubic chi

# 春程人功七百六十六尺
人功 = 766

# 并出土功五分之一
出土功 = Fraction(1, 5) * 人功

# 定功六百一十二尺、五分尺之四
定功 = Fraction(612) + Fraction(4, 5)

# 問：用徒幾何？
# 置本人功，去其五分之一，餘為法
法 = 定功

# 以溝積尺為實
實 = 溝積

# 實如法而一，得用徒人數
a = Fraction(實, 法)  # 21875/3064 persons#----- content ends here -----

"""
"""
