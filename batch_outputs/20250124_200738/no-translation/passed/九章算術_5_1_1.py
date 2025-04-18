"""
今有城下廣四丈，上廣二丈，高五丈，袤一百二十六丈五尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

#----- content starts here -----

# 城下廣四丈
下廣 = 4

# 上廣二丈
上廣 = 2

# 高五丈
高 = 5

# 袤一百二十六丈五尺
袤 = 126 + Fraction(5, 10)  # 5尺 = 0.5丈

# 并上下廣而半之
平均廣 = Fraction((下廣 + 上廣), 2)

# 以高若深乘之
橫截面積 = 平均廣 * 高

# 又以袤乘之，即積尺
積 = 橫截面積 * 袤

# Convert 積 from 丈^3 to 尺^3 (1丈 = 10尺, so 1丈^3 = 1000尺^3)
a = 積 * 1000#----- content ends here -----

"""
"""
