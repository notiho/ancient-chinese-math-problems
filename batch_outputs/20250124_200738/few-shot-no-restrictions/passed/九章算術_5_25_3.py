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

The procedure for calculating the volume of ponds (including curved ponds, pan-shaped ponds, and valleys) is the same:
Double the top length, and add it to the bottom length. 
Also, double the bottom length, and add it to the top length. 
Multiply each by their respective widths, then add the results together. 
Finally, multiply by the height (or depth) and divide by 6.

For curved ponds, the top length is calculated by summing the inner, middle, and outer perimeters of the top and halving it. 
Similarly, the bottom length is calculated by summing the inner, middle, and outer perimeters of the bottom and halving it.

Answer: *a* chi.
"""

# 上廣六丈，袤八丈
上廣 = 6  # zhang
上袤 = 8  # zhang

# 下廣四丈，袤六丈
下廣 = 4  # zhang
下袤 = 6  # zhang

# 深二丈
深 = 2  # zhang

# 將所有單位轉換為尺 (1丈 = 10尺)
上廣 *= 10
上袤 *= 10
下廣 *= 10
下袤 *= 10
深 *= 10

# 術曰：倍上袤，下袤從之
倍上袤 = 2 * 上袤 + 下袤

# 亦倍下袤，上袤從之
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

a#----- content ends here -----

"""
"""
