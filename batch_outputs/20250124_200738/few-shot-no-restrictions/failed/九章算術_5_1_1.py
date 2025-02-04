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

Question: What is the total volume in cubic chi?

The procedure says: Add the top and bottom widths together and halve the result. Multiply this by the height (or depth). Then multiply the result by the length. This gives the total volume in cubic chi.

Answer: *a* cubic chi.
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

# 并上下廣而半之 (add top and bottom widths, then halve)
平均廣 = (下廣 + 上廣) / 2

# 以高若深乘之 (multiply by height)
橫截面積 = 平均廣 * 高

# 又以袤乘之 (multiply by length)
積尺 = 橫截面積 * 袤 * 10  # Convert zhang^3 to chi^3 (1 zhang^3 = 10 chi^3)

# Final answer
a = 積尺
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1897500, Actual: 18975.0"""
