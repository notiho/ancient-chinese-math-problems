"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

"""
Suppose there is a pan-shaped pond. The top has a width of 6 zhang and a length of 8 zhang.
The bottom has a width of 4 zhang and a length of 6 zhang. The depth is 2 zhang.
Question: what is the volume?

For ponds of various shapes (e.g., pan-shaped, curved, etc.), the procedure is the same.
The procedure says: Double the top length, and add the bottom length to it. 
Also double the bottom length, and add the top length to it. 
Multiply each by their respective widths, sum the results, and multiply by the height (or depth). 
Finally, divide by 6.

For curved ponds, sum the inner, middle, and outer perimeters of the top and halve it to get the top length. 
Do the same for the bottom to get the bottom length.

Answer: *a* chi.
"""

# 上廣六丈，袤八丈
上廣 = 6
上袤 = 8

# 下廣四丈，袤六丈
下廣 = 4
下袤 = 6

# 深二丈
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
a = Fraction(體積, 6)  # Convert to chi

"""
Variable 'a' has wrong value. Expected: 212000/3, Actual: 212/3"""
