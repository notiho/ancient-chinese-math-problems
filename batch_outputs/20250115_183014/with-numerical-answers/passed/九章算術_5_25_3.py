"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a(=212000/3)尺 。
"""

"""
Suppose there is a pan-shaped pond. The upper width is 6 zhang, the upper length is 8 zhang.
The lower width is 4 zhang, the lower length is 6 zhang, and the depth is 2 zhang.
Question: what is the volume?

The procedure for a shepherd's pond, curved pond, pan-shaped pond, and dark valley is the same.
The procedure says: Double the upper length, and add the lower length to it.
Also double the lower length, and add the upper length to it.
Multiply each by their respective widths, and add the results together.
Multiply this sum by the height or depth, and divide the result by 6.
For curved ponds, add the upper middle and outer perimeters together, halve it to get the upper length.
Do the same for the lower middle and outer perimeters to get the lower length.

Answer: *a*(=212000/3) chi³.
"""

# 上廣六丈
上廣 = 6 * 10  # Convert to chi

# 袤八丈
上袤 = 8 * 10  # Convert to chi

# 下廣四丈
下廣 = 4 * 10  # Convert to chi

# 袤六丈
下袤 = 6 * 10  # Convert to chi

# 深二丈
深 = 2 * 10  # Convert to chi

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
a = Fraction(體積, 6)  # 212000/3 chi³
"""
"""
