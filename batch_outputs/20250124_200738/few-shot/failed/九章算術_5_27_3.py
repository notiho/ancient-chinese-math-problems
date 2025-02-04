"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a valley (冥谷) with the following dimensions:
- The upper width is 2 zhang, and the upper length is 7 zhang.
- The lower width is 8 chi, and the lower length is 4 zhang.
- The depth is 6 zhang and 5 chi.

Question: what is the total volume?

The procedure for valleys, curved ponds, and other similar shapes is the same:
Double the upper length, and use the lower length as it is. Also, double the lower length, and use the upper length as it is.
Multiply each by its respective width, then add them together. Multiply the result by the height or depth, and divide by 6.
For curved ponds, add the inner, middle, and outer perimeters of the top and divide by 2 to get the upper length. Do the same for the bottom to get the lower length.

Answer: *a* chi³.
"""

# Dimensions
上廣 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)
上袤 = 7 * 10  # Convert zhang to chi
下廣 = 8       # Already in chi
下袤 = 4 * 10  # Convert zhang to chi
深 = 6 * 10 + 5  # Convert depth to chi (6 zhang 5 chi)

# 倍上袤，下袤從之
倍上袤 = 2 * 上袤
下袤從之 = 下袤

# 倍下袤，上袤從之
倍下袤 = 2 * 下袤
上袤從之 = 上袤

# 各以其廣乘之
上積 = 倍上袤 * 上廣
下積 = 倍下袤 * 下廣

# 并
總積 = 上積 + 下積

# 以高若深乘之
體積 = 總積 * 深

# 皆六而一
a = Fraction(體積, 6)  # Final volume in chi³#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 52000, Actual: 111800/3"""
