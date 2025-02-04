"""
今有溝上廣一丈五尺下廣一丈深五尺袤七丈問積幾何
城垣隄溝壍渠皆同術術曰并上下廣而半之以高若深乘之又以袤乘之即積尺
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a ditch with the following dimensions:
- Top width: 1 zhang 5 chi
- Bottom width: 1 zhang
- Depth: 5 chi
- Length: 7 zhang

Question: what is the volume of the ditch?

The procedure for walls, embankments, ditches, moats, and canals is the same:
Add the top and bottom widths, then halve the result.
Multiply this by the height (or depth), then multiply by the length.
This gives the volume in cubic chi.

Answer: *a* cubic chi.
"""

# 上廣一丈五尺
上廣 = 1 * 10 + 5  # Convert zhang and chi to chi

# 下廣一丈
下廣 = 1 * 10  # Convert zhang to chi

# 深五尺
深 = 5  # Depth in chi

# 袤七丈
袤 = 7 * 10  # Convert zhang to chi

# 并上下廣而半之
平均廣 = (上廣 + 下廣) / 2

# 以高若深乘之
橫截面積 = 平均廣 * 深

# 又以袤乘之，即積尺
a = 橫截面積 * 袤  # Volume in cubic chi#----- content ends here -----

"""
"""
