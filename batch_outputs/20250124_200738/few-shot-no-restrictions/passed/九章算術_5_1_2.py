"""
今有城下廣四丈，上廣二丈，高五丈，袤一百二十六丈五尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a city wall with the following dimensions:
- Bottom width: 4 zhang
- Top width: 2 zhang
- Height: 5 zhang
- Length (mao): 126 zhang and 5 chi

Question: What is the total volume?

The procedure says: Add the top and bottom widths together and halve the result. Multiply this by the height (or depth). Then multiply the result by the length (mao). This gives the total volume in chi³.

Answer: *a* chi³.
"""

from fractions import Fraction

# 城下廣四丈
下廣 = 4  # in zhang

# 上廣二丈
上廣 = 2  # in zhang

# 高五丈
高 = 5  # in zhang

# 袤一百二十六丈五尺
袤 = 126 + Fraction(5, 10)  # Convert 5 chi to zhang (1 zhang = 10 chi)

# 并上下廣而半之
平均廣 = (下廣 + 上廣) / 2  # in zhang

# 以高若深乘之
橫截面積 = 平均廣 * 高  # in zhang²

# 又以袤乘之
積 = 橫截面積 * 袤  # in zhang³

# Convert zhang³ to chi³ (1 zhang³ = 1000 chi³)
積_in_尺 = 積 * 1000

a = 積_in_尺
a#----- content ends here -----

"""
"""
