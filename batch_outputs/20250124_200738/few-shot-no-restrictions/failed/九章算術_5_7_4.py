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

Question: What is the total volume in cubic chi?

The procedure says: Add the top and bottom widths, then halve the result.
Multiply this by the depth (or height), then multiply by the length.
The result is the total volume in cubic chi.

Answer: *a* cubic chi.
"""

# Convert all measurements to chi (1 zhang = 10 chi, 1 chi = 10 cun)

# 上廣 (Top width): 1丈6尺3寸
上廣 = 1 * 10 + 6 + Fraction(3, 10)

# 下廣 (Bottom width): 1丈
下廣 = 1 * 10

# 深 (Depth): 6尺3寸
深 = 6 + Fraction(3, 10)

# 袤 (Length): 13丈2尺1寸
袤 = 13 * 10 + 2 + Fraction(1, 10)

# 并上下廣而半之
平均廣 = (上廣 + 下廣) / 2

# 以高若深乘之
截面積 = 平均廣 * 深

# 又以袤乘之，即積尺
積 = 截面積 * 袤

# Result
a = 積
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 54719/5, Actual: 21887649/2000"""
