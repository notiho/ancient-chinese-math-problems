"""
今有垣下廣三尺，上廣二尺，高一丈二尺，袤二十二丈五尺八寸。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a(=6774)尺 。
"""

#----- content starts here -----
"""
Suppose there is a wall with a bottom width of 3 chi, a top width of 2 chi, a height of 1 zhang 2 chi, and a length of 22 zhang 5 chi 8 cun.
Question: what is the volume in cubic chi?

For walls, embankments, ditches, moats, and canals, the procedure is the same.
The procedure says: Add the top and bottom widths and halve them.
Multiply this by the height (or depth), then multiply by the length.
This gives the volume in cubic chi.

Answer: *a*(=6774) cubic chi.
"""

# 垣下廣三尺
下廣 = 3

# 上廣二尺
上廣 = 2

# 高一丈二尺
高 = 1 * 10 + 2  # Convert zhang to chi (1 zhang = 10 chi)

# 袤二十二丈五尺八寸
袤 = 22 * 10 + 5 + Fraction(8, 10)  # Convert zhang and cun to chi (1 zhang = 10 chi, 1 chi = 10 cun)

# 并上下廣而半之
平均廣 = (下廣 + 上廣) / 2

# 以高若深乘之
橫截面積 = 平均廣 * 高

# 又以袤乘之，即積尺
a = 橫截面積 * 袤  # 6774 cubic chi#----- content ends here -----

"""
"""
