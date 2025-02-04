"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a trench with an upper width of 1 zhang 5 chi, a lower width of 1 zhang, a depth of 5 chi, and a length of 7 zhang.
Question: what is the volume?

For walls, embankments, trenches, ditches, and canals, the same method applies.
The procedure says: Add the upper and lower widths, then halve the sum.
Multiply this by the height (or depth), then multiply by the length.
This gives the volume in cubic chi.

Answer: *a* cubic chi.
"""

from fractions import Fraction

# Given dimensions
上廣 = 1 * 10 + 5  # Convert 1 zhang 5 chi to chi
下廣 = 1 * 10       # Convert 1 zhang to chi
深 = 5              # Depth in chi
袤 = 7 * 10         # Convert 7 zhang to chi

# Procedure
# Add the upper and lower widths, then halve the sum
平均廣 = Fraction(上廣 + 下廣, 2)

# Multiply by depth
橫截面積 = 平均廣 * 深

# Multiply by length
積 = 橫截面積 * 袤

# Result
a = 積
a#----- content ends here -----

"""
"""
