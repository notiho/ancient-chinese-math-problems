"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a valley with the following dimensions:
- Top width: 2 zhang
- Top length: 7 zhang
- Bottom width: 8 chi
- Bottom length: 4 zhang
- Depth: 6 zhang 5 chi

Question: what is the total volume?

The procedure for irregular shapes like valleys, curved pools, and similar structures is the same:
Double the top length, and add the bottom length to it.
Also, double the bottom length, and add the top length to it.
Multiply each by their respective widths, then add the results together.
Multiply this sum by the height (or depth).
Finally, divide by 6 to get the volume.

For curved pools, the procedure involves averaging the inner, middle, and outer perimeters for both the top and bottom lengths, but this is not needed here.

Answer: *a* chi³.
"""

# Dimensions
上廣 = 2 * 10  # Convert zhang to chi
上袤 = 7 * 10  # Convert zhang to chi
下廣 = 8       # Already in chi
下袤 = 4 * 10  # Convert zhang to chi
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
a = Fraction(體積, 6)  # Final volume in chi³#----- content ends here -----

"""
"""
