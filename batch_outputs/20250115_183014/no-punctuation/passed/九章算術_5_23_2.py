"""
今有芻童下廣二丈袤三丈上廣三丈袤四丈高三丈問積幾何
芻童曲池盤池冥谷皆同術術曰倍上袤下袤從之亦倍下袤上袤從之各以其廣乘之并以高若深乘之皆六而一其曲池者并上中外周而半之以為上袤亦并下中外周而半之以為下袤
荅曰 a尺 
"""

"""
Suppose there is a trapezoidal prism (芻童) with the following dimensions:
The bottom width is 2 zhang, the bottom length is 3 zhang.
The top width is 3 zhang, the top length is 4 zhang.
The height is 3 zhang.
Question: what is the volume?

The procedure says: Double the top length and bottom length, and add them together. 
Also double the bottom length and top length, and add them together. 
Multiply each by their respective widths. 
Add these results together, then multiply by the height (or depth). 
Divide the result by 6 to obtain the volume.

The answer says: *a* chi.
"""

# 下廣二丈
下廣 = 2 * 10  # Convert to chi (1 zhang = 10 chi)

# 下袤三丈
下袤 = 3 * 10  # Convert to chi

# 上廣三丈
上廣 = 3 * 10  # Convert to chi

# 上袤四丈
上袤 = 4 * 10  # Convert to chi

# 高三丈
高 = 3 * 10  # Convert to chi

# 倍上袤下袤從之
倍上袤下袤 = 2 * 上袤 + 下袤

# 亦倍下袤上袤從之
倍下袤上袤 = 2 * 下袤 + 上袤

# 各以其廣乘之
上積 = 倍上袤下袤 * 上廣
下積 = 倍下袤上袤 * 下廣

# 并以高若深乘之
總積 = (上積 + 下積) * 高

# 皆六而一
a = Fraction(總積, 6)  # Volume in chi³
"""
"""
