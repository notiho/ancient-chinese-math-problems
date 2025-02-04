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

Question: what is the volume?

The procedure for valleys, curved ponds, and other similar shapes is the same:
Double the upper length, and add the lower length to it. Also double the lower length, and add the upper length to it.
Multiply each by their respective widths. Add these two results together, and multiply by the depth.
Finally, divide the result by 6 to get the volume.

Answer: *a*(=52000) chi³.
"""

# 上廣二丈
上廣 = 2 * 10  # Convert zhang to chi

# 袤七丈
上袤 = 7 * 10  # Convert zhang to chi

# 下廣八尺
下廣 = 8

# 袤四丈
下袤 = 4 * 10  # Convert zhang to chi

# 深六丈五尺
深 = 6 * 10 + 5  # Convert zhang and chi to chi

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
a = Fraction(體積, 6)  # 52000 chi³
"""
"""
