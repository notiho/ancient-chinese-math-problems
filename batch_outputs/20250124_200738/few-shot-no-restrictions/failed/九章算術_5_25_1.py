"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a basin-shaped pond. The top width is 6 zhang, the top length is 8 zhang. 
The bottom width is 4 zhang, the bottom length is 6 zhang. The depth is 2 zhang.
Question: what is the total volume?

The procedure for calculating the volume of irregular shapes such as basin-shaped ponds, curved ponds, or valleys is the same.
The procedure says: Double the top length, and add the bottom length to it. 
Also double the bottom length, and add the top length to it. 
Multiply each by their respective widths. Add these two results together, and multiply by the height or depth. 
Finally, divide by 6 to get the volume.

Answer: *a* chi³.
"""

from fractions import Fraction

# 上廣 6 丈
上廣 = 6

# 上袤 8 丈
上袤 = 8

# 下廣 4 丈
下廣 = 4

# 下袤 6 丈
下袤 = 6

# 深 2 丈
深 = 2

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

# Convert the result to chi³ (1 丈 = 10 尺, so 1 丈³ = 1000 尺³)
a_in_chi_cubed = a * 1000

a_in_chi_cubed#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 212000/3, Actual: 212/3"""
