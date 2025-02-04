"""
今有塹上廣一丈六尺三寸，下廣一丈，深六尺三寸，袤一十三丈二尺一寸。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a(=54719/5)尺 。
"""

"""
Suppose there is a trench with the following dimensions:
- Top width: 1 zhang 6 chi 3 cun
- Bottom width: 1 zhang
- Depth: 6 chi 3 cun
- Length: 13 zhang 2 chi 1 cun

Question: What is the volume in cubic chi?

For walls, embankments, ditches, trenches, and canals, the procedure is the same.
The procedure says: Add the top and bottom widths and halve them. Multiply by the height (or depth). Then multiply by the length. This gives the volume in cubic chi.

Answer: *a*(=54719/5) cubic chi.
"""

# Convert all dimensions to chi (尺)
# 上廣一丈六尺三寸
上廣 = 1 * 10 + 6 + Fraction(3, 10)

# 下廣一丈
下廣 = 1 * 10

# 深六尺三寸
深 = 6 + Fraction(3, 10)

# 袤一十三丈二尺一寸
袤 = 13 * 10 + 2 + Fraction(1, 10)

# 并上下廣而半之
平均廣 = (上廣 + 下廣) / 2

# 以高若深乘之
截面積 = 平均廣 * 深

# 又以袤乘之，即積尺
積 = 截面積 * 袤

a = 積  # 54719/5 cubic chi
"""
Variable 'a' has wrong value. Expected: 54719/5, Actual: 21887649/2000"""
