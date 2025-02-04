"""
今有塹上廣一丈六尺三寸下廣一丈深六尺三寸袤一十三丈二尺一寸問積幾何
城垣隄溝壍渠皆同術術曰并上下廣而半之以高若深乘之又以袤乘之即積尺
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a trench with the following dimensions:
- Upper width: 1 zhang 6 chi 3 cun
- Lower width: 1 zhang
- Depth: 6 chi 3 cun
- Length: 13 zhang 2 chi 1 cun

Question: what is the total volume in cubic chi?

The procedure says: Add the upper and lower widths, then halve the sum.
Multiply this by the height (or depth), then multiply the result by the length.
This gives the total volume in cubic chi.

Answer: *a* cubic chi.
"""

# Convert all dimensions to chi (尺)
# 上廣一丈六尺三寸
上廣 = 10 + 6 + Fraction(3, 10)

# 下廣一丈
下廣 = 10

# 深六尺三寸
深 = 6 + Fraction(3, 10)

# 袤一十三丈二尺一寸
袤 = 13 * 10 + 2 + Fraction(1, 10)

# 并上下廣而半之
平均廣 = (上廣 + 下廣) / 2

# 以高若深乘之
截面積 = 平均廣 * 深

# 又以袤乘之，即積尺
a = 截面積 * 袤#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 54719/5, Actual: 21887649/2000"""
