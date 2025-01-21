"""
今有芻童下廣二丈袤三丈上廣三丈袤四丈高三丈問積幾何
芻童曲池盤池冥谷皆同術術曰倍上袤下袤從之亦倍下袤上袤從之各以其廣乘之并以高若深乘之皆六而一其曲池者并上中外周而半之以為上袤亦并下中外周而半之以為下袤
荅曰 a尺 
"""

"""
Suppose there is a trapezoidal prism (a frustum) with the following dimensions:
- Bottom width: 2 zhang
- Bottom length: 3 zhang
- Top width: 3 zhang
- Top length: 4 zhang
- Height: 3 zhang

Question: What is the total volume?

The procedure for calculating the volume of a frustum says:
Double the top length and add it to the bottom length. Similarly, double the bottom length and add it to the top length.
Multiply each by its respective width. Add these together and multiply by the height (or depth).
Divide the result by 6 to obtain the volume.

Answer: *a* chi.
"""

# 下廣二丈
下廣 = 2 * 10  # Convert zhang to chi

# 袤三丈
下袤 = 3 * 10  # Convert zhang to chi

# 上廣三丈
上廣 = 3 * 10  # Convert zhang to chi

# 袤四丈
上袤 = 4 * 10  # Convert zhang to chi

# 高三丈
高 = 3 * 10  # Convert zhang to chi

# 倍上袤，下袤從之
倍上袤 = 2 * 上袤 + 下袤

# 倍下袤，上袤從之
倍下袤 = 2 * 下袤 + 上袤

# 各以其廣乘之
上積 = 倍上袤 * 上廣
下積 = 倍下袤 * 下廣

# 并以高乘之
總積 = (上積 + 下積) * 高

# 皆六而一
a = Fraction(總積, 6)  # Volume in chi³
"""
"""
