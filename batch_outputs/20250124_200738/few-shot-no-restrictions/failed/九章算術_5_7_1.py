"""
今有塹上廣一丈六尺三寸，下廣一丈，深六尺三寸，袤一十三丈二尺一寸。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a trench with the following dimensions:
- Top width: 1 zhang 6 chi 3 cun
- Bottom width: 1 zhang
- Depth: 6 chi 3 cun
- Length: 13 zhang 2 chi 1 cun

Question: what is the total volume in cubic chi?

The procedure says: Add the top and bottom widths together, then halve the result.
Multiply this by the depth (or height), then multiply by the length.
The result is the total volume in cubic chi.

Answer: *a* cubic chi.
"""

from fractions import Fraction

# Convert all dimensions to chi (1 zhang = 10 chi, 1 chi = 10 cun)

# Top width: 1 zhang 6 chi 3 cun
top_width = 10 + 6 + Fraction(3, 10)

# Bottom width: 1 zhang
bottom_width = 10

# Depth: 6 chi 3 cun
depth = 6 + Fraction(3, 10)

# Length: 13 zhang 2 chi 1 cun
length = 13 * 10 + 2 + Fraction(1, 10)

# Add top and bottom widths, then halve
average_width = (top_width + bottom_width) / 2

# Multiply by depth and length to get the volume
volume = average_width * depth * length

# The answer
a = volume
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 54719/5, Actual: 21887649/2000"""
