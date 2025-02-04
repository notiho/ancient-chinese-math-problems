"""
今有溝上廣一丈五尺下廣一丈深五尺袤七丈問積幾何
城垣隄溝壍渠皆同術術曰并上下廣而半之以高若深乘之又以袤乘之即積尺
荅曰 a尺 
"""

"""
Suppose there is a ditch with an upper width of 1 zhang 5 chi, a lower width of 1 zhang, a depth of 5 chi, and a length of 7 zhang.
Question: what is the volume in cubic chi?

The procedure for city walls, embankments, ditches, trenches, and canals is the same:
Add the upper and lower widths, then halve the result.
Multiply this by the height (or depth), and then multiply by the length.
This gives the volume in cubic chi.

Answer: *a* cubic chi.
"""

# 上廣一丈五尺
上廣 = 1 * 10 + 5  # Convert to chi (1 zhang = 10 chi)

# 下廣一丈
下廣 = 1 * 10  # Convert to chi

# 深五尺
深 = 5  # Already in chi

# 袤七丈
袤 = 7 * 10  # Convert to chi

# 并上下廣而半之
平均廣 = (上廣 + 下廣) / 2

# 以高若深乘之
斷面積 = 平均廣 * 深

# 又以袤乘之，即積尺
a = 斷面積 * 袤
"""
"""
