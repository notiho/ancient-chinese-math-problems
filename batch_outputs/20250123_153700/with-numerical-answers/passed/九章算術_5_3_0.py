"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a(=7112)尺 。
"""

"""
Suppose there is a levee with a bottom width of 2 zhang, a top width of 8 chi, a height of 4 chi, and a length of 12 zhang 7 chi.
Question: what is the total volume?

For walls, embankments, levees, ditches, moats, and canals, the procedure is the same.
The procedure says: Add the top and bottom widths and halve them. Multiply by the height (or depth), then multiply by the length. This gives the total volume in cubic chi.

Answer: *a*(=7112) cubic chi.
"""

# 隄下廣二丈 (bottom width)
下廣 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 上廣八尺 (top width)
上廣 = 8

# 高四尺 (height)
高 = 4

# 袤一十二丈七尺 (length)
袤 = 12 * 10 + 7  # Convert zhang to chi and add chi

# 并上下廣而半之
平均廣 = (下廣 + 上廣) / 2

# 以高若深乘之
橫截面積 = 平均廣 * 高

# 又以袤乘之，即積尺
a = 橫截面積 * 袤  # 7112 cubic chi
"""
"""
