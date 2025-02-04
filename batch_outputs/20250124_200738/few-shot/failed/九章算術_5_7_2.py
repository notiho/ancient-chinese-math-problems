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

The procedure for walls, embankments, ditches, trenches, and canals is the same.
The procedure says: Add the top and bottom widths, then halve the result.
Multiply this by the height (or depth), then multiply by the length.
This gives the total volume in cubic chi.

Answer: *a* cubic chi.
"""

# Dimensions
上廣 = 1 * 10 + 6 + Fraction(3, 10)  # Convert 1丈6尺3寸 to chi
下廣 = 1 * 10  # Convert 1丈 to chi
深 = 6 + Fraction(3, 10)  # Convert 6尺3寸 to chi
袤 = 13 * 10 + 2 + Fraction(1, 10)  # Convert 13丈2尺1寸 to chi

# 并上下廣而半之
平均廣 = (上廣 + 下廣) / 2

# 以高若深乘之
截面積 = 平均廣 * 深

# 又以袤乘之，即積尺
積 = 截面積 * 袤

a = 積  # Total volume in cubic chi#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 54719/5, Actual: 21887649/2000"""
