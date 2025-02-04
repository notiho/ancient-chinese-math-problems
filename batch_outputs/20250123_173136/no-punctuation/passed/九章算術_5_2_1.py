"""
今有垣下廣三尺上廣二尺高一丈二尺袤二十二丈五尺八寸問積幾何
城垣隄溝壍渠皆同術術曰并上下廣而半之以高若深乘之又以袤乘之即積尺
荅曰 a尺 
"""

"""
Suppose there is a wall with a bottom width of 3 chi, a top width of 2 chi, a height of 1 zhang and 2 chi, and a length of 22 zhang, 5 chi, and 8 cun.
Question: what is the total volume in cubic chi?

The procedure for walls, embankments, ditches, moats, and canals is the same:
Add the top and bottom widths, then halve it. Multiply by the height (or depth), then multiply by the length. This gives the total volume in cubic chi.

Answer: *a* cubic chi.
"""

# 下廣三尺
下廣 = 3

# 上廣二尺
上廣 = 2

# 高一丈二尺 (convert to chi: 1 zhang = 10 chi)
高 = 1 * 10 + 2

# 袤二十二丈五尺八寸 (convert to chi: 1 zhang = 10 chi, 1 chi = 10 cun)
袤 = 22 * 10 + 5 + Fraction(8, 10)

# 并上下廣而半之
平均廣 = (下廣 + 上廣) / 2

# 以高乘之
截面積 = 平均廣 * 高

# 又以袤乘之，即積尺
a = 截面積 * 袤
"""
"""
