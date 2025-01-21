"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
荅曰：四千三百七十五尺。
春程人功七百六十六尺，并出土功五分之一，定功六百一十二尺、五分尺之四。問︰用徒幾何？
荅曰： a人 。
"""

from fractions import Fraction

# Given dimensions
上廣 = Fraction(1, 1) + Fraction(5, 10)  # 1丈5尺 = 1.5丈
下廣 = Fraction(1, 1)                   # 1丈
深 = Fraction(5, 10)                    # 5尺 = 0.5丈
袤 = Fraction(7, 1)                     # 7丈

# Volume formula: V = ((上廣 + 下廣) * 深 / 2) * 袤
V = ((上廣 + 下廣) * 深 / 2) * 袤
print(f"Volume of the ditch (積): {V} 丈³")

# Convert volume to 尺³ (1丈³ = 1000尺³)
V_in_尺 = V * 1000
print(f"Volume of the ditch (積): {V_in_尺} 尺³")
"""
Missing variable in output: 'a'"""
