"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a pan-shaped pond. The top has a width of 6 zhang and a length of 8 zhang. 
The bottom has a width of 4 zhang and a length of 6 zhang. The depth is 2 zhang.
Question: what is the volume?

The procedure for calculating the volume of a pan-shaped pond, curved pond, or valley is the same:
Double the top length, and add the bottom length to it. 
Also double the bottom length, and add the top length to it. 
Multiply each by their respective widths, sum the results, and multiply by the depth. 
Finally, divide by 6 to get the volume.

For curved ponds, sum the inner, middle, and outer perimeters of the top and divide by 2 to get the top length. 
Do the same for the bottom to get the bottom length.

Answer: *a* chi³.
"""

from fractions import Fraction

# 上廣六丈，袤八丈
上廣 = 6  # zhang
上袤 = 8  # zhang

# 下廣四丈，袤六丈
下廣 = 4  # zhang
下袤 = 6  # zhang

# 深二丈
深 = 2  # zhang

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
a = Fraction(體積, 6)

# Convert zhang³ to chi³ (1 zhang = 10 chi)
a_in_chi_cubed = a * 10**3

a_in_chi_cubed#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 212000/3, Actual: 212/3"""
