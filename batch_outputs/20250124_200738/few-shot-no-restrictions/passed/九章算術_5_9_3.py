"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a canal with the following dimensions:
- Top width: 1 zhang 8 chi
- Bottom width: 3 chi 6 cun
- Depth: 1 zhang 8 chi
- Length: 51824 chi

Question: what is the total volume in cubic chi?

The procedure says: Add the top width and bottom width, then halve the sum. Multiply this by the depth (or height), then multiply the result by the length. This gives the total volume in cubic chi.

Answer: *a* cubic chi.
"""

from fractions import Fraction

# Dimensions
上廣 = 1 * 10 + 8  # Convert 1 zhang 8 chi to chi
下廣 = 3 + Fraction(6, 10)  # Convert 3 chi 6 cun to chi
深 = 1 * 10 + 8  # Convert 1 zhang 8 chi to chi
袤 = 51824  # Length in chi

# Procedure
# Add the top and bottom widths, then halve the sum
平均廣 = (上廣 + 下廣) / 2

# Multiply by depth
截面積 = 平均廣 * 深

# Multiply by length to get total volume
a = 截面積 * 袤

a  # Total volume in cubic chi#----- content ends here -----

"""
"""
