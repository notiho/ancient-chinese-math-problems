"""
今有塹上廣一丈六尺三寸下廣一丈深六尺三寸袤一十三丈二尺一寸問積幾何
城垣隄溝壍渠皆同術術曰并上下廣而半之以高若深乘之又以袤乘之即積尺
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a trench with the following dimensions:
- Top width: 1 zhang 6 chi 3 cun
- Bottom width: 1 zhang
- Depth: 6 chi 3 cun
- Length: 13 zhang 2 chi 1 cun

Question: What is the volume in cubic chi?

The procedure for city walls, embankments, ditches, trenches, and canals is the same:
Add the top and bottom widths, then halve the result. Multiply this by the height (or depth), then multiply by the length. The result is the volume in cubic chi.

Answer: *a* cubic chi.
"""

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
橫截面積 = 平均廣 * 深

# 又以袤乘之，即積尺
a = 橫截面積 * 袤#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 54719/5, Actual: 21887649/2000"""
