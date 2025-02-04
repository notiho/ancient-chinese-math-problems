"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a(=50372928/5)尺 。
"""

"""
Suppose there is a dug canal with an upper width of 1 zhang 8 chi, a lower width of 3 chi 6 cun, a depth of 1 zhang 8 chi, and a length of 51824 chi.
Question: what is the volume?

For walls, embankments, ditches, moats, and canals, the procedure is the same.
The procedure says: Add the upper and lower widths and halve them. Multiply this by the height or depth, then multiply by the length. This gives the volume in cubic chi.

Answer: *a*(=50372928/5) cubic chi.
"""

# 上廣一丈八尺
上廣 = 1 * 10 + 8  # Convert to chi (1 zhang = 10 chi)

# 下廣三尺六寸
下廣 = 3 + Fraction(6, 10)  # Convert to chi (1 chi = 10 cun)

# 深一丈八尺
深 = 1 * 10 + 8  # Convert to chi

# 袤五萬一千八百二十四尺
袤 = 51824  # Length in chi

# 并上下廣而半之
平均廣 = (上廣 + 下廣) / 2

# 以高若深乘之
橫截面積 = 平均廣 * 深

# 又以袤乘之，即積尺
積 = 橫截面積 * 袤

a = Fraction(積)  # 50372928/5 cubic chi
"""
"""
