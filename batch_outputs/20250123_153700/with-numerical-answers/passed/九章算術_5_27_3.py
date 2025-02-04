"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a(=52000)尺 。
"""

"""
Suppose there is a valley (冥谷) with the following dimensions:
- Top width: 2 zhang
- Top length: 7 zhang
- Bottom width: 8 chi
- Bottom length: 4 zhang
- Depth: 6 zhang 5 chi

Question: What is the total volume?

The procedure for valleys, curved ponds, and circular ponds is the same:
Double the top length, and add the bottom length to it. 
Similarly, double the bottom length, and add the top length to it.
Multiply each by their respective widths, then add the results together.
Multiply the sum by the height or depth, and divide by 6 to get the volume.

For curved ponds, add the inner, middle, and outer circumferences of the top, divide by 2 to get the top length.
Do the same for the bottom.

Answer: *a*(=52000) chi³.
"""

# Dimensions
上廣 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)
上袤 = 7 * 10
下廣 = 8
下袤 = 4 * 10
深 = 6 * 10 + 5  # Convert depth to chi (6 zhang 5 chi)

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
