"""
今有盤池上廣六丈袤八丈下廣四丈袤六丈深二丈問積幾何
芻童曲池盤池冥谷皆同術術曰倍上袤下袤從之亦倍下袤上袤從之各以其廣乘之并以高若深乘之皆六而一其曲池者并上中外周而半之以為上袤亦并下中外周而半之以為下袤
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a basin-shaped pond. The upper width is 6 zhang, the upper length is 8 zhang.
The lower width is 4 zhang, the lower length is 6 zhang, and the depth is 2 zhang.
Question: what is the volume?

The procedure for curved ponds, basin-shaped ponds, and dark valleys is the same:
Double the upper length and add it to the lower length. 
Also, double the lower length and add it to the upper length.
Multiply each by their respective widths. Add these together and multiply by the height or depth.
Divide the result by 6.

For curved ponds: Add the upper, middle, and outer circumferences, halve them to get the upper length.
Similarly, add the lower, middle, and outer circumferences, halve them to get the lower length.

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
上袤倍加下袤 = 2 * 上袤 + 下袤

# 倍下袤上袤從之
下袤倍加上袤 = 2 * 下袤 + 上袤

# 各以其廣乘之
上積 = 上袤倍加下袤 * 上廣
下積 = 下袤倍加上袤 * 下廣

# 并以高若深乘之
總積 = (上積 + 下積) * 深

# 皆六而一
a = Fraction(總積, 6)  # Convert to chi (1 zhang = 10 chi) if necessary#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 212000/3, Actual: 212/3"""
