"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a(=52000)尺 。
"""

"""
Suppose there is a valley (冥谷) with the following dimensions:
- The upper width is 2 zhang, and the upper length is 7 zhang.
- The lower width is 8 chi, and the lower length is 4 zhang.
- The depth is 6 zhang and 5 chi.

Question: what is the total volume?

The procedure for valleys, curved ponds, and similar shapes is the same:
Double the upper length, and follow it with the lower length.
Also, double the lower length, and follow it with the upper length.
Multiply each by its respective width, then add them together.
Multiply the result by the height or depth, and divide by 6.

For curved ponds, add the upper inner, middle, and outer perimeters, halve them to get the upper length.
Do the same for the lower inner, middle, and outer perimeters to get the lower length.

Answer: *a*(=52000) chi³.
"""

# 上廣二丈
上廣 = 2 * 10  # Convert zhang to chi

# 袤七丈
上袤 = 7 * 10  # Convert zhang to chi

# 下廣八尺
下廣 = 8  # Already in chi

# 袤四丈
下袤 = 4 * 10  # Convert zhang to chi

# 深六丈五尺
深 = 6 * 10 + 5  # Convert zhang to chi and add chi

# 倍上袤，下袤從之
倍上袤 = 2 * 上袤
倍上積 = 倍上袤 * 上廣

# 倍下袤，上袤從之
倍下袤 = 2 * 下袤
倍下積 = 倍下袤 * 下廣

# 各以其廣乘之，并
總積 = 倍上積 + 倍下積

# 以高若深乘之，皆六而一
a = Fraction(總積 * 深, 6)  # 52000 chi³
"""
Variable 'a' has wrong value. Expected: 52000, Actual: 111800/3"""
