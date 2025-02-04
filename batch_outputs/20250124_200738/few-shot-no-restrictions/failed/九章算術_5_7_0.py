"""
今有塹上廣一丈六尺三寸，下廣一丈，深六尺三寸，袤一十三丈二尺一寸。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a trench with the following dimensions:
- Top width: 1 zhang 6 chi 3 cun (1丈6尺3寸)
- Bottom width: 1 zhang (1丈)
- Depth: 6 chi 3 cun (6尺3寸)
- Length: 13 zhang 2 chi 1 cun (13丈2尺1寸)

Question: What is the total volume in cubic chi?

The procedure says: Add the top and bottom widths, then halve the sum. Multiply this by the depth, then multiply the result by the length. The result is the volume in cubic chi.

Answer: *a* cubic chi.
"""

from fractions import Fraction

# Convert all dimensions to chi (尺)
# Top width: 1丈6尺3寸
top_width = 10 + 6 + Fraction(3, 10)  # 1丈 = 10尺, 1尺 = 10寸

# Bottom width: 1丈
bottom_width = 10  # 1丈 = 10尺

# Depth: 6尺3寸
depth = 6 + Fraction(3, 10)  # 1尺 = 10寸

# Length: 13丈2尺1寸
length = 13 * 10 + 2 + Fraction(1, 10)  # 1丈 = 10尺, 1尺 = 10寸

# Procedure:
# 1. Add top and bottom widths, then halve the sum
average_width = (top_width + bottom_width) / 2

# 2. Multiply by depth
cross_section_area = average_width * depth

# 3. Multiply by length
volume = cross_section_area * length

# Answer
a = volume
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 54719/5, Actual: 21887649/2000"""
