"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
Suppose there is a trench with an upper width of 1 zhang and 5 chi, a lower width of 1 zhang, a depth of 5 chi, and a length of 7 zhang.
Question: what is the volume in cubic chi?

For walls, embankments, trenches, moats, and canals, the procedure is the same.
The procedure says: Add the upper and lower widths together and halve them.
Multiply this by the height or depth, then multiply by the length, and the result is the volume in cubic chi.

Answer: *a* cubic chi.
"""

# 上廣一丈五尺
上廣 = 1 * 10 + 5  # Convert zhang and chi to chi

# 下廣一丈
下廣 = 1 * 10  # Convert zhang to chi

# 深五尺
深 = 5  # Depth in chi

# 袤七丈
袤 = 7 * 10  # Convert zhang to chi

# 并上下廣而半之
平均廣 = (上廣 + 下廣) / 2

# 以高若深乘之
截面積 = 平均廣 * 深

# 又以袤乘之，即積尺
a = 截面積 * 袤  # Volume in cubic chi
"""
"""
