"""
今有隄下廣二丈上廣八尺高四尺袤一十二丈七尺問積幾何
城垣隄溝壍渠皆同術術曰并上下廣而半之以高若深乘之又以袤乘之即積尺
荅曰 a尺 
"""

"""
Suppose there is a dike with a bottom width of 2 zhang, a top width of 8 chi, a height of 4 chi, and a length of 12 zhang and 7 chi.
Question: what is the total volume?

The procedure for city walls, dikes, moats, trenches, and channels is the same.
The procedure says: Add the top and bottom widths, then halve them. Multiply by the height (or depth), then multiply by the length. This gives the total volume in cubic chi.

Answer: *a* cubic chi.
"""

# 下廣二丈 (convert to chi: 1 zhang = 10 chi)
下廣 = 2 * 10

# 上廣八尺
上廣 = 8

# 高四尺
高 = 4

# 袤一十二丈七尺 (convert to chi: 1 zhang = 10 chi)
袤 = 12 * 10 + 7

# 并上下廣
上下廣和 = 下廣 + 上廣

# 而半之
平均廣 = Fraction(上下廣和, 2)

# 以高乘之
橫截面積 = 平均廣 * 高

# 又以袤乘之，即積尺
a = 橫截面積 * 袤
"""
"""
