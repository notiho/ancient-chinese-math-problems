"""
今有城下廣四丈上廣二丈高五丈袤一百二十六丈五尺問積幾何
城垣隄溝壍渠皆同術術曰并上下廣而半之以高若深乘之又以袤乘之即積尺
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a wall with a bottom width of 4 zhang, a top width of 2 zhang, a height of 5 zhang, and a length of 126 zhang and 5 chi.
Question: what is the total volume?

The procedure for walls, embankments, ditches, moats, and canals is the same.
The procedure says: Add the top and bottom widths and halve them. Multiply this by the height (or depth), then multiply by the length. This gives the total volume in chi³.

Answer: *a* chi³.
"""

# 下廣四丈
下廣 = 4

# 上廣二丈
上廣 = 2

# 高五丈
高 = 5

# 袤一百二十六丈五尺 (convert to chi: 1 zhang = 10 chi)
袤 = 126 * 10 + 5

# 并上下廣而半之
平均廣 = (下廣 + 上廣) / 2

# 以高乘之
橫截面積 = 平均廣 * 高

# 又以袤乘之，即積尺
a = 橫截面積 * 袤#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1897500, Actual: 18975.0"""
