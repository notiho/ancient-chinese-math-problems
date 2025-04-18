"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
荅曰：四千三百七十五尺。
春程人功七百六十六尺，并出土功五分之一，定功六百一十二尺、五分尺之四。問︰用徒幾何？
術曰：置本人功，去其五分之一，餘為法。以溝積尺為實。實如法而一，得用徒人數。
荅曰： a人 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 溝上廣一丈五尺
上廣 = 1 * 10 + 5  # 1丈5尺 converted to 尺

# 下廣一丈
下廣 = 1 * 10  # 1丈 converted to 尺

# 深五尺
深 = 5  # in 尺

# 袤七丈
袤 = 7 * 10  # 7丈 converted to 尺

# 計算溝積
# 積 = ((上廣 + 下廣) / 2) * 深 * 袤
積 = Fraction((上廣 + 下廣), 2) * 深 * 袤

# 春程人功七百六十六尺
本人功 = 766

# 并出土功五分之一
出土功 = Fraction(1, 5)

# 去其五分之一，餘為法
法 = 本人功 * (1 - 出土功)

# 以溝積尺為實
實 = 積

# 實如法而一，得用徒人數
a = Fraction(實, 法)

# Output results
print(f"溝積: {積} 尺")
print(f"用徒人數: {a} 人")
#----- content ends here -----


"""

"""


"""
"""
