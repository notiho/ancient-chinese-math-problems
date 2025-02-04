"""
今有芻童，下廣二丈，袤三丈，上廣三丈，袤四丈，高三丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a trapezoidal prism (芻童) with the following dimensions:
The bottom width is 2 zhang, the bottom length is 3 zhang.
The top width is 3 zhang, the top length is 4 zhang.
The height is 3 zhang.

Question: what is the volume?

The procedure for trapezoidal prisms, curved pools, circular pools, and deep valleys is the same.
The procedure says: Double the top length, and let the bottom length follow it.
Also, double the bottom length, and let the top length follow it.
Multiply each by its respective width, add them together, and then multiply by the height (or depth).
Finally, divide by 6 to obtain the volume.

For curved pools: Add the top inner and outer perimeters, halve them to get the top length.
Do the same for the bottom inner and outer perimeters to get the bottom length.

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
倍上袤 = 2 * 上袤
倍下袤 = 下袤

# 倍下袤，上袤從之
倍下袤 = 2 * 下袤
倍上袤 = 上袤

# 各以其廣乘之
上積 = 倍上袤 * 上廣
下積 = 倍下袤 * 下廣

# 并
總積 = 上積 + 下積

# 以高乘之
體積 = 總積 * 高

# 皆六而一
a = Fraction(體積, 6)  # Final volume in chi³#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 26500, Actual: 12000"""
