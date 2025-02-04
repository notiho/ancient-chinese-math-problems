"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

"""
Suppose there is a valley (冥谷) with an upper width of 2 zhang, an upper length of 7 zhang, a lower width of 8 chi, a lower length of 4 zhang, and a depth of 6 zhang 5 chi.
Question: what is the volume?

The procedure for valleys, curved ponds, and other irregular shapes is the same. 
The procedure says: Double the upper length, and take the lower length as it is. 
Also, double the lower length, and take the upper length as it is. 
Multiply each by its respective width, then add the results. 
Multiply the sum by the height or depth, then divide by 6. 
For curved ponds, add the upper middle and outer perimeters, halve them to get the upper length; do the same for the lower middle and outer perimeters to get the lower length.

Answer: *a* chi³.
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
下袤從之 = 下袤

# 亦倍下袤，上袤從之
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
a = Fraction(體積, 6)  # Final volume in chi³
"""
Variable 'a' has wrong value. Expected: 52000, Actual: 111800/3"""
