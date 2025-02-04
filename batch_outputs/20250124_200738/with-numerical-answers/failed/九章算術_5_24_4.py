"""
今有曲池，上中周二丈，外周四丈，廣一丈，下中周一丈四尺，外周二丈四尺，廣五尺，深一丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a(=5650/3)尺 。
"""

#----- content starts here -----
"""
Suppose there is a curved pond. 
The upper middle circumference is 2 zhang, the outer circumference is 4 zhang, and the width is 1 zhang. 
The lower middle circumference is 1 zhang 4 chi, the outer circumference is 2 zhang 4 chi, and the width is 5 chi. 
The depth is 1 zhang.
Question: what is the volume?

The procedure for curved ponds, circular ponds, and valleys is the same. 
The procedure says: Double the upper length, and take the lower length as it is. 
Also, double the lower length, and take the upper length as it is. 
Multiply each by its width, add them together, and multiply by the height or depth. 
Divide the result by 6. 
For curved ponds, add the upper middle and outer circumferences together and halve them to get the upper length. 
Similarly, add the lower middle and outer circumferences together and halve them to get the lower length.

Answer: *a*(=5650/3) chi³.
"""

from fractions import Fraction

# 上中周二丈
上中周 = 2 * 10  # Convert zhang to chi

# 外周四丈
上外周 = 4 * 10  # Convert zhang to chi

# 廣一丈
上廣 = 1 * 10  # Convert zhang to chi

# 下中周一丈四尺
下中周 = 1 * 10 + 4  # Convert zhang and chi to chi

# 外周二丈四尺
下外周 = 2 * 10 + 4  # Convert zhang and chi to chi

# 廣五尺
下廣 = 5  # Already in chi

# 深一丈
深 = 1 * 10  # Convert zhang to chi

# 并上中、外周而半之，以為上袤
上袤 = (上中周 + 上外周) / 2

# 并下中、外周而半之，以為下袤
下袤 = (下中周 + 下外周) / 2

# 倍上袤，下袤從之
倍上袤 = 2 * 上袤

# 亦倍下袤，上袤從之
倍下袤 = 2 * 下袤

# 各以其廣乘之
上積 = 倍上袤 * 上廣
下積 = 倍下袤 * 下廣

# 并
總積 = 上積 + 下積

# 以高若深乘之
體積 = 總積 * 深

# 皆六而一
a = Fraction(體積, 6)  # 5650/3 chi³#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
