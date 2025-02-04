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
- Length: 126 zhang and 5 chi

Question: What is the total volume in cubic chi?

The procedure says: Add the top and bottom widths and take half of the sum. Multiply this by the height (or depth), then multiply the result by the length. This gives the total volume in cubic chi.

Answer: *a* cubic chi.
"""

from fractions import Fraction

# 城下廣四丈 (Bottom width: 4 zhang)
下廣 = 4

# 城上廣二丈 (Top width: 2 zhang)
上廣 = 2

# 高五丈 (Height: 5 zhang)
高 = 5

# 袤一百二十六丈五尺 (Length: 126 zhang and 5 chi)
# Convert to zhang (1 zhang = 10 chi)
袤 = 126 + Fraction(5, 10)

# 并上下廣而半之 (Add top and bottom widths, then halve)
平均廣 = (下廣 + 上廣) / 2

# 以高若深乘之 (Multiply by height)
橫截面積 = 平均廣 * 高

# 又以袤乘之 (Multiply by length)
積 = 橫截面積 * 袤

# Convert the result to cubic chi (1 zhang^3 = 1000 chi^3)
a = 積 * 1000

a#----- content ends here -----

"""
"""
