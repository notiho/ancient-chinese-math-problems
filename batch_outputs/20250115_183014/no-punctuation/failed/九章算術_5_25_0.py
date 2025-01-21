"""
今有盤池上廣六丈袤八丈下廣四丈袤六丈深二丈問積幾何
芻童曲池盤池冥谷皆同術術曰倍上袤下袤從之亦倍下袤上袤從之各以其廣乘之并以高若深乘之皆六而一其曲池者并上中外周而半之以為上袤亦并下中外周而半之以為下袤
荅曰 a尺 
"""

"""
Suppose there is a rectangular pond with the following dimensions:
- The top width is 6 zhang, the top length is 8 zhang.
- The bottom width is 4 zhang, the bottom length is 6 zhang.
- The depth is 2 zhang.

Question: what is the volume of the pond?

The procedure for ponds (including curved ponds, rectangular ponds, and valleys) is the same:
Double the top length and add it to the bottom length. Similarly, double the bottom length and add it to the top length.
Multiply each by its respective width. Add these results together, then multiply by the depth.
Finally, divide the result by 6 to obtain the volume.

Answer: *a* chi.
"""

# 上廣六丈
上廣 = 6

# 上袤八丈
上袤 = 8

# 下廣四丈
下廣 = 4

# 下袤六丈
下袤 = 6

# 深二丈
深 = 2

# 倍上袤下袤從之
倍上袤 = 2 * 上袤 + 下袤

# 倍下袤上袤從之
倍下袤 = 2 * 下袤 + 上袤

# 各以其廣乘之
上積 = 倍上袤 * 上廣
下積 = 倍下袤 * 下廣

# 并以高若深乘之
總積 = (上積 + 下積) * 深

# 皆六而一
a = Fraction(總積, 6) * 10  # Convert zhang to chi (1 zhang = 10 chi)
"""
Variable 'a' has wrong value. Expected: 212000/3, Actual: 2120/3"""
