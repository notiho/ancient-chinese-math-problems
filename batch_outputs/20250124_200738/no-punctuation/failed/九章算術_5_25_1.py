"""
今有盤池上廣六丈袤八丈下廣四丈袤六丈深二丈問積幾何
芻童曲池盤池冥谷皆同術術曰倍上袤下袤從之亦倍下袤上袤從之各以其廣乘之并以高若深乘之皆六而一其曲池者并上中外周而半之以為上袤亦并下中外周而半之以為下袤
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a basin-shaped pond. The top width is 6 zhang, the top length is 8 zhang.
The bottom width is 4 zhang, the bottom length is 6 zhang. The depth is 2 zhang.
Question: what is the volume?

The procedure for curved ponds, basin-shaped ponds, and dark valleys is the same.
The procedure says: Double the top length and add the bottom length to it.
Also double the bottom length and add the top length to it.
Multiply each by its respective width.
Add these together, then multiply by the height or depth.
Divide the result by 6.

The answer says: *a* chi.
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

# 倍上袤，下袤從之
倍上袤 = 2 * 上袤 + 下袤

# 倍下袤，上袤從之
倍下袤 = 2 * 下袤 + 上袤

# 各以其廣乘之
上積 = 倍上袤 * 上廣
下積 = 倍下袤 * 下廣

# 并以高若深乘之
總積 = (上積 + 下積) * 深

# 皆六而一
a = Fraction(總積, 6)  # Convert to chi (1 zhang = 10 chi)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 212000/3, Actual: 212/3"""
