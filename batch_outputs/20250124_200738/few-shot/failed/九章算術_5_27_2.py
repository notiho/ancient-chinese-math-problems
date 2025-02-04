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

Question: what is the volume of the valley?

The procedure for valleys, curved ponds, and circular ponds is the same:
Double the top length, and use the bottom length alongside it. 
Also, double the bottom length, and use the top length alongside it.
Multiply each by their respective widths, then add them together.
Multiply the result by the height or depth, and divide by 6.
For curved ponds, add the inner, middle, and outer perimeters of the top, divide by 2 to get the top length.
Do the same for the bottom.

Answer: *a* chi³.
"""

# Dimensions
上廣 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)
上袤 = 7 * 10  # Convert zhang to chi
下廣 = 8       # Already in chi
下袤 = 4 * 10  # Convert zhang to chi
深 = 6 * 10 + 5  # Convert depth to chi (6 zhang and 5 chi)

# 倍上袤，下袤從之
倍上袤 = 2 * 上袤
倍上積 = 倍上袤 * 上廣

# 亦倍下袤，上袤從之
倍下袤 = 2 * 下袤
倍下積 = 倍下袤 * 下廣

# 各以其廣乘之，并
總積 = 倍上積 + 倍下積

# 以高若深乘之
總積乘深 = 總積 * 深

# 皆六而一
a = Fraction(總積乘深, 6)  # Volume in chi³#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 52000, Actual: 111800/3"""
