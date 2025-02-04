"""
今有塹上廣一丈六尺三寸，下廣一丈，深六尺三寸，袤一十三丈二尺一寸。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a(=54719/5)尺 。
"""

#----- content starts here -----
"""
Suppose there is a trench with an upper width of 1 zhang 6 chi 3 cun, a lower width of 1 zhang, a depth of 6 chi 3 cun, and a length of 13 zhang 2 chi 1 cun.
Question: what is the volume?

For city walls, embankments, ditches, trenches, and canals, the procedure is the same.
The procedure says: Add the upper and lower widths and halve them. Multiply this by the height or depth. Then multiply by the length. This gives the volume in cubic chi.

Answer: *a*(=54719/5) cubic chi.
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
截面積 = 平均廣 * 深

# 又以袤乘之，即積尺
a = 截面積 * 袤 # 54719/5 cubic chi#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 54719/5, Actual: 21887649/2000"""
