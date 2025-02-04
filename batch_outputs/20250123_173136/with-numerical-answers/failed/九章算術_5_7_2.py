"""
今有塹上廣一丈六尺三寸，下廣一丈，深六尺三寸，袤一十三丈二尺一寸。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a(=54719/5)尺 。
"""

"""
Suppose there is a trench with the following dimensions:
The top width is 1 zhang 6 chi 3 cun, the bottom width is 1 zhang, the depth is 6 chi 3 cun, and the length is 13 zhang 2 chi 1 cun.
Question: what is the volume of the trench?

For walls, embankments, dikes, trenches, and canals, the procedure is the same.
The procedure says: Add the top and bottom widths together and halve them. Multiply by the height or depth, and then multiply by the length. This gives the volume in cubic chi.

Answer: *a*(=54719/5) cubic chi.
"""

# Dimensions
# Top width: 1丈6尺3寸
上廣 = 1 * 10 + 6 + Fraction(3, 10)

# Bottom width: 1丈
下廣 = 1 * 10

# Depth: 6尺3寸
深 = 6 + Fraction(3, 10)

# Length: 13丈2尺1寸
袤 = 13 * 10 + 2 + Fraction(1, 10)

# 并上下廣而半之
平均廣 = (上廣 + 下廣) / 2

# 以高若深乘之
橫截面積 = 平均廣 * 深

# 又以袤乘之，即積尺
積 = 橫截面積 * 袤

a = 積 # 54719/5 cubic chi
"""
Variable 'a' has wrong value. Expected: 54719/5, Actual: 21887649/2000"""
