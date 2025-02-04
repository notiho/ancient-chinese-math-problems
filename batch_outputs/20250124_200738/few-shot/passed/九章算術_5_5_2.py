"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a ditch with an upper width of 1 zhang 5 chi, a lower width of 1 zhang, a depth of 5 chi, and a length of 7 zhang.
Question: what is the volume in cubic chi?

For walls, embankments, ditches, trenches, and canals, the procedure is the same.
The procedure says: Add the upper and lower widths and halve them. Multiply this by the height or depth. Then multiply by the length. This gives the volume in cubic chi.

Answer: *a* cubic chi.
"""

# 上廣一丈五尺
上廣 = 1 * 10 + 5  # Convert zhang to chi

# 下廣一丈
下廣 = 1 * 10  # Convert zhang to chi

# 深五尺
深 = 5

# 袤七丈
袤 = 7 * 10  # Convert zhang to chi

# 并上下廣而半之
平均廣 = (上廣 + 下廣) / 2

# 以高若深乘之
橫截面積 = 平均廣 * 深

# 又以袤乘之，即積尺
a = 橫截面積 * 袤#----- content ends here -----

"""
"""
