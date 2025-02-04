"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a(=212000/3)尺 。
"""

#----- content starts here -----
"""
Suppose there is a pan-shaped pond. The top has a width of 6 zhang and a length of 8 zhang.
The bottom has a width of 4 zhang and a length of 6 zhang. The depth is 2 zhang.
Question: what is the volume?

The procedure for a shepherd's pond, curved pond, pan-shaped pond, and dark valley is the same.
The procedure says: Double the top length, and add the bottom length to it.
Also, double the bottom length, and add the top length to it.
Multiply each by their respective widths, and add the results.
Multiply the sum by the height or depth, and divide by 6.
For curved ponds, add the top inner, middle, and outer perimeters, and halve them to get the top length.
Similarly, add the bottom inner, middle, and outer perimeters, and halve them to get the bottom length.

Answer: *a*(=212000/3) chi³.
"""

# 上廣六丈，袤八丈
上廣 = 6 * 10  # Convert zhang to chi
上袤 = 8 * 10  # Convert zhang to chi

# 下廣四丈，袤六丈
下廣 = 4 * 10  # Convert zhang to chi
下袤 = 6 * 10  # Convert zhang to chi

# 深二丈
深 = 2 * 10  # Convert zhang to chi

# 倍上袤，下袤從之
倍上袤 = 2 * 上袤 + 下袤

# 倍下袤，上袤從之
倍下袤 = 2 * 下袤 + 上袤

# 各以其廣乘之，并
積和 = (倍上袤 * 上廣) + (倍下袤 * 下廣)

# 以高若深乘之
積 = 積和 * 深

# 皆六而一
a = Fraction(積, 6)  # 212000/3 chi³#----- content ends here -----

"""
"""
