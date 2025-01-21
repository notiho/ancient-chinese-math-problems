"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a(=7112)尺 。
"""

"""
Suppose there is a dike with a bottom width of 2 zhang, a top width of 8 chi, a height of 4 chi, and a length of 12 zhang and 7 chi.
Question: what is the volume?

The procedure for walls, embankments, dikes, trenches, moats, and canals is the same. 
The procedure says: Add the top and bottom widths and halve them. Multiply this by the height (or depth). Then multiply by the length, obtaining the volume in cubic chi.

Answer: *a*(=7112) cubic chi.
"""

# 隄下廣二丈 (bottom width)
下廣 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 上廣八尺 (top width)
上廣 = 8

# 高四尺 (height)
高 = 4

# 袤一十二丈七尺 (length)
袤 = 12 * 10 + 7  # Convert zhang and chi to chi

# 并上下廣而半之
平均廣 = (下廣 + 上廣) / 2

# 以高若深乘之
截面積 = 平均廣 * 高

# 又以袤乘之，即積尺
積 = 截面積 * 袤

a = 積  # 7112 cubic chi
"""
"""
