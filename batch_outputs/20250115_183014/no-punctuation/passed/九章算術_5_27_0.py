"""
今有冥谷上廣二丈袤七丈下廣八尺袤四丈深六丈五尺問積幾何
芻童曲池盤池冥谷皆同術術曰倍上袤下袤從之亦倍下袤上袤從之各以其廣乘之并以高若深乘之皆六而一其曲池者并上中外周而半之以為上袤亦并下中外周而半之以為下袤
荅曰 a尺 
"""

"""
Suppose there is a valley (冥谷) with the following dimensions:
- Top width: 2 zhang
- Top length: 7 zhang
- Bottom width: 8 chi
- Bottom length: 4 zhang
- Depth: 6 zhang 5 chi

Question: What is the total volume?

The procedure for valleys, curved ponds, and circular ponds is the same. The procedure says:
Double the top length and add it to the bottom length. Similarly, double the bottom length and add it to the top length. Multiply each by their respective widths. Add these results together and multiply by the height or depth. Divide the result by 6.

For curved ponds, add the inner, middle, and outer perimeters of the top and divide by 2 to get the top length. Similarly, add the inner, middle, and outer perimeters of the bottom and divide by 2 to get the bottom length.

Answer: *a* chi³.
"""

# Dimensions
上廣 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)
上袤 = 7 * 10  # Convert zhang to chi
下廣 = 8       # Already in chi
下袤 = 4 * 10  # Convert zhang to chi
深 = 6 * 10 + 5  # Convert depth to chi (6 zhang 5 chi)

# 倍上袤下袤從之
倍上袤 = 2 * 上袤 + 下袤

# 倍下袤上袤從之
倍下袤 = 2 * 下袤 + 上袤

# 各以其廣乘之
上積 = 倍上袤 * 上廣
下積 = 倍下袤 * 下廣

# 并以高若深乘之
總積 = (上積 + 下積) * 深

# 皆六而一
a = Fraction(總積, 6)  # Divide by 6 to get the final volume in chi³
"""
"""
