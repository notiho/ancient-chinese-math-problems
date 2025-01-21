"""
今有城下廣四丈，上廣二丈，高五丈，袤一百二十六丈五尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a(=1897500)尺 。
"""

"""
Suppose there is a city wall with a bottom width of 4 zhang, a top width of 2 zhang, a height of 5 zhang, and a length (mao) of 126 zhang and 5 chi.
Question: what is the total volume?

The procedure for city walls, walls, embankments, ditches, moats, and canals is the same.
The procedure says: Add the top and bottom widths and halve the result. Multiply this by the height (or depth), and then multiply by the length. This gives the total volume in chi.

Answer: *a*(=1897500) chi³.
"""

# 城下廣四丈
下廣 = 4 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 上廣二丈
上廣 = 2 * 10  # Convert zhang to chi

# 高五丈
高 = 5 * 10  # Convert zhang to chi

# 袤一百二十六丈五尺
袤 = 126 * 10 + 5  # Convert zhang to chi and add chi

# 并上下廣而半之
平均廣 = (下廣 + 上廣) / 2

# 以高若深乘之
橫截面積 = 平均廣 * 高

# 又以袤乘之，即積尺
a = 橫截面積 * 袤  # 1897500 chi³
"""
"""
