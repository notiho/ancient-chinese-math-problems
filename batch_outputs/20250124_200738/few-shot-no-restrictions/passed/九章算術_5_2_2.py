"""
今有垣下廣三尺，上廣二尺，高一丈二尺，袤二十二丈五尺八寸。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a wall with the following dimensions:
- Bottom width: 3 chi
- Top width: 2 chi
- Height: 1 zhang 2 chi (12 chi)
- Length: 22 zhang 5 chi 8 cun (225.8 chi)

Question: What is the total volume in cubic chi?

The procedure says: Add the top and bottom widths, then halve the result. Multiply this by the height (or depth), then multiply the result by the length. This gives the total volume in cubic chi.

Answer: *a* cubic chi.
"""

from fractions import Fraction

# Dimensions
下廣 = 3  # Bottom width in chi
上廣 = 2  # Top width in chi
高 = 12  # Height in chi (1 zhang = 10 chi, so 1 zhang 2 chi = 12 chi)
袤 = 225 + Fraction(8, 10)  # Length in chi (22 zhang 5 chi 8 cun = 225.8 chi)

# Procedure
# 并上下廣而半之
平均廣 = (下廣 + 上廣) / 2

# 以高若深乘之
橫截面積 = 平均廣 * 高

# 又以袤乘之，即積尺
積 = 橫截面積 * 袤

# Answer
a = 積
a#----- content ends here -----

"""
"""
