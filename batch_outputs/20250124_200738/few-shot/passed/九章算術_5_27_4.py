"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a valley (冥谷) with the following dimensions:
- The top width is 2 zhang, and the top length is 7 zhang.
- The bottom width is 8 chi, and the bottom length is 4 zhang.
- The depth is 6 zhang and 5 chi.

Question: What is the total volume?

The procedure for valleys, curved ponds, and other similar shapes is the same:
Double the top length, and add the bottom length to it. Similarly, double the bottom length, and add the top length to it.
Multiply each by its respective width, then add these results together.
Multiply the sum by the depth. Divide the result by 6 to obtain the volume.
For curved ponds, take the sum of the inner, middle, and outer perimeters of the top, divide by 2 to get the top length. Do the same for the bottom.

Answer: *a* chi³.
"""

# 上廣二丈 (convert to chi: 1丈 = 10尺)
上廣 = 2 * 10

# 上袤七丈 (convert to chi)
上袤 = 7 * 10

# 下廣八尺
下廣 = 8

# 下袤四丈 (convert to chi)
下袤 = 4 * 10

# 深六丈五尺 (convert to chi)
深 = 6 * 10 + 5

# 倍上袤，下袤從之
倍上袤 = 2 * 上袤 + 下袤

# 倍下袤，上袤從之
倍下袤 = 2 * 下袤 + 上袤

# 各以其廣乘之
上積 = 倍上袤 * 上廣
下積 = 倍下袤 * 下廣

# 并
總積 = 上積 + 下積

# 以高若深乘之
體積 = 總積 * 深

# 皆六而一
a = Fraction(體積, 6)  # Volume in chi³#----- content ends here -----

"""
"""
