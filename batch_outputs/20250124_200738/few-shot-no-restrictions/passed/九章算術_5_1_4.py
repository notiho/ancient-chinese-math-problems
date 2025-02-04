"""
今有城下廣四丈，上廣二丈，高五丈，袤一百二十六丈五尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a city wall with a bottom width of 4 zhang, a top width of 2 zhang, a height of 5 zhang, and a length (mao) of 126 zhang and 5 chi.
Question: what is the total volume?

The procedure says: Add the top and bottom widths together and halve them. Multiply this by the height (or depth), and then multiply by the length. This gives the total volume in chi³.

Answer: *a* chi³.
"""

from fractions import Fraction

# 城下廣四丈 (bottom width)
下廣 = 4  # in zhang

# 上廣二丈 (top width)
上廣 = 2  # in zhang

# 高五丈 (height)
高 = 5  # in zhang

# 袤一百二十六丈五尺 (length)
袤 = 126 + Fraction(5, 10)  # Convert 5 chi to zhang (1 zhang = 10 chi)

# 并上下廣而半之
平均廣 = (下廣 + 上廣) / 2  # in zhang

# 以高若深乘之
橫截面積 = 平均廣 * 高  # in zhang²

# 又以袤乘之，即積尺
積 = 橫截面積 * 袤  # in zhang³

# Convert zhang³ to chi³ (1 zhang³ = 1000 chi³)
積尺 = 積 * 1000  # in chi³

a = 積尺
a#----- content ends here -----

"""
"""
