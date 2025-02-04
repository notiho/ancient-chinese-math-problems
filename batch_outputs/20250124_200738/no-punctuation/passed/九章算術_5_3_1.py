"""
今有隄下廣二丈上廣八尺高四尺袤一十二丈七尺問積幾何
城垣隄溝壍渠皆同術術曰并上下廣而半之以高若深乘之又以袤乘之即積尺
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a levee with a bottom width of 2 zhang, a top width of 8 chi, a height of 4 chi, and a length of 12 zhang 7 chi.
Question: what is the volume in cubic chi?

The procedure for walls, levees, ditches, and canals is the same:
Add the top and bottom widths, then halve the sum. Multiply this by the height (or depth), then multiply by the length. This gives the volume in cubic chi.

Answer: *a* cubic chi.
"""

# 隄下廣二丈 (convert to chi: 1丈 = 10尺)
下廣 = 2 * 10

# 上廣八尺
上廣 = 8

# 高四尺
高 = 4

# 袤一十二丈七尺 (convert to chi: 1丈 = 10尺)
袤 = 12 * 10 + 7

# 并上下廣而半之
平均廣 = (下廣 + 上廣) / 2

# 以高乘之
橫截面積 = 平均廣 * 高

# 又以袤乘之，即積尺
a = 橫截面積 * 袤#----- content ends here -----

"""
"""
