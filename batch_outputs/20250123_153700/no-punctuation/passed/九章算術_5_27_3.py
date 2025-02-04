"""
今有冥谷上廣二丈袤七丈下廣八尺袤四丈深六丈五尺問積幾何
芻童曲池盤池冥谷皆同術術曰倍上袤下袤從之亦倍下袤上袤從之各以其廣乘之并以高若深乘之皆六而一其曲池者并上中外周而半之以為上袤亦并下中外周而半之以為下袤
荅曰 a尺 
"""

"""
Suppose there is a dark valley (冥谷) with the following dimensions:
- The top width is 2 zhang, and the top length is 7 zhang.
- The bottom width is 8 chi, and the bottom length is 4 zhang.
- The depth is 6 zhang and 5 chi.

Question: What is the total volume?

The procedure for dark valleys, curved ponds, and circular ponds is the same:
Double the top length and add the bottom length to it. Similarly, double the bottom length and add the top length to it.
Multiply each by its respective width. Add these results together and multiply by the height or depth.
Finally, divide the result by 6.

For curved ponds, the top length is calculated by adding the inner, middle, and outer circumferences and halving the result. Similarly, the bottom length is calculated by adding the inner, middle, and outer circumferences and halving the result.

Answer: *a* chi³.
"""

# Dimensions
上廣 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)
上袤 = 7 * 10  # Convert zhang to chi
下廣 = 8       # Already in chi
下袤 = 4 * 10  # Convert zhang to chi
深 = 6 * 10 + 5  # Convert depth to chi (6 zhang and 5 chi)

# 倍上袤，下袤從之
倍上袤 = 2 * 上袤 + 下袤

# 倍下袤，上袤從之
倍下袤 = 2 * 下袤 + 上袤

# 各以其廣乘之
上積 = 倍上袤 * 上廣
下積 = 倍下袤 * 下廣

# 并以高若深乘之
總積 = (上積 + 下積) * 深

# 皆六而一
a = Fraction(總積, 6)  # Final volume in chi³
"""
"""
