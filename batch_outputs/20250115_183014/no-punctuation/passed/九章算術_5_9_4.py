"""
今有穿渠上廣一丈八尺下廣三尺六寸深一丈八尺袤五萬一千八百二十四尺問積幾何
城垣隄溝壍渠皆同術術曰并上下廣而半之以高若深乘之又以袤乘之即積尺
荅曰 a尺 
"""

"""
Suppose there is a canal with the following dimensions:
- Top width: 1 zhang 8 chi
- Bottom width: 3 chi 6 cun
- Depth: 1 zhang 8 chi
- Length: 51824 chi

Question: what is the total volume in cubic chi?

The procedure for city walls, embankments, ditches, trenches, and canals is the same:
Add the top and bottom widths, then halve the result.
Multiply this by the height (or depth), then multiply by the length.
This gives the total volume in cubic chi.

Answer: *a* cubic chi.
"""

# 上廣一丈八尺
上廣 = 1 * 10 + 8  # Convert zhang to chi

# 下廣三尺六寸
下廣 = 3 + Fraction(6, 10)  # Convert cun to chi

# 深一丈八尺
深 = 1 * 10 + 8  # Convert zhang to chi

# 袤五萬一千八百二十四尺
袤 = 51824

# 并上下廣而半之
平均廣 = (上廣 + 下廣) / 2

# 以高若深乘之
橫截面積 = 平均廣 * 深

# 又以袤乘之，即積尺
a = 橫截面積 * 袤
"""
"""
