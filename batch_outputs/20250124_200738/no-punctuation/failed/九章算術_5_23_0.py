"""
今有芻童下廣二丈袤三丈上廣三丈袤四丈高三丈問積幾何
芻童曲池盤池冥谷皆同術術曰倍上袤下袤從之亦倍下袤上袤從之各以其廣乘之并以高若深乘之皆六而一其曲池者并上中外周而半之以為上袤亦并下中外周而半之以為下袤
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a trapezoidal solid (a "Chu Tong") with the following dimensions:
The bottom width is 2 zhang, the bottom length is 3 zhang.
The top width is 3 zhang, the top length is 4 zhang.
The height is 3 zhang.
Question: what is the volume?

The procedure says: Double the top length and add it to the bottom length. 
Also double the bottom length and add it to the top length.
Multiply each by its respective width.
Add these together, then multiply by the height (or depth).
Finally, divide by 6.

Answer: *a* chi.
"""

# 下廣二丈
下廣 = 2

# 袤三丈
下袤 = 3

# 上廣三丈
上廣 = 3

# 袤四丈
上袤 = 4

# 高三丈
高 = 3

# 倍上袤下袤從之
上袤倍加下袤 = 2 * 上袤 + 下袤

# 倍下袤上袤從之
下袤倍加上袤 = 2 * 下袤 + 上袤

# 各以其廣乘之
上積 = 上袤倍加下袤 * 上廣
下積 = 下袤倍加上袤 * 下廣

# 并以高乘之
總積 = (上積 + 下積) * 高

# 皆六而一
a = Fraction(總積, 6)  # Convert to chi
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 26500, Actual: 53/2"""
