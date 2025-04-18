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

The labor calculation says: Spring labor per person is 766 cubic chi, including 1/5 for excavating the soil, resulting in an adjusted labor of 612 4/5 cubic chi.
Question: how many workers are needed?

The procedure says: Place the labor per person, remove 1/5, and the remainder is the divisor.
Take the ditch volume as the dividend.
Divide the dividend by the divisor to obtain the number of workers needed.

Answer: *a*(=21875/3064) people.
"""

from fractions import Fraction

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
溝積 = Fraction((上廣 + 下廣), 2) * 深 * 袤  # 4375 cubic chi

# 春程人功七百六十六尺
人功 = 766

# 并出土功五分之一
出土功 = Fraction(1, 5) * 人功

# 定功
定功 = Fraction(766) - 出土功  # 612 4/5 cubic chi

# 置本人功，去其五分之一，餘為法
法 = 定功

# 以溝積尺為實
實 = 溝積

# 實如法而一，得用徒人數
a = Fraction(實, 法)  # 21875/3064 people#----- content ends here -----

"""
"""
