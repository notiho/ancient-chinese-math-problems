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

The procedure for irregular shapes like valleys, curved ponds, or basins is the same:
1. Double the top length and add the bottom length to it.
2. Double the bottom length and add the top length to it.
3. Multiply each of these by their respective widths.
4. Add the two results together.
5. Multiply the sum by the depth.
6. Divide the result by 6 to get the volume.

Answer: The volume is *a* chi³.
"""

from fractions import Fraction

# Dimensions
上廣 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)
上袤 = 7 * 10  # Convert zhang to chi
下廣 = 8  # Already in chi
下袤 = 4 * 10  # Convert zhang to chi
深 = 6 * 10 + 5  # Convert depth to chi (6 zhang and 5 chi)

# Step 1: Double the top length and add the bottom length
倍上袤 = 2 * 上袤 + 下袤

# Step 2: Double the bottom length and add the top length
倍下袤 = 2 * 下袤 + 上袤

# Step 3: Multiply each by their respective widths
上積 = 倍上袤 * 上廣
下積 = 倍下袤 * 下廣

# Step 4: Add the two results together
總積 = 上積 + 下積

# Step 5: Multiply by the depth
總積乘深 = 總積 * 深

# Step 6: Divide by 6 to get the volume
a = Fraction(總積乘深, 6)

# Output the result
a#----- content ends here -----

"""
"""
