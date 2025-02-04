"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a trench with the following dimensions:
- Top width: 1 zhang 5 chi (15 chi)
- Bottom width: 1 zhang (10 chi)
- Depth: 5 chi
- Length: 7 zhang (70 chi)

Question: What is the volume of the trench?

The procedure for walls, embankments, trenches, ditches, and canals is the same:
Add the top and bottom widths, halve the result, multiply by the depth (or height), and then multiply by the length. The result is the volume in cubic chi.

Answer: *a* cubic chi.
"""

# Dimensions in chi
上廣 = 15  # Top width: 1 zhang 5 chi = 15 chi
下廣 = 10  # Bottom width: 1 zhang = 10 chi
深 = 5     # Depth: 5 chi
袤 = 70    # Length: 7 zhang = 70 chi

# Add top and bottom widths, then halve
平均廣 = (上廣 + 下廣) / 2

# Multiply by depth
截面積 = 平均廣 * 深

# Multiply by length to get the total volume
積 = 截面積 * 袤

# Answer
a = 積
a#----- content ends here -----

"""
"""
