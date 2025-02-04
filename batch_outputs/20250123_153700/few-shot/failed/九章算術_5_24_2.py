"""
今有曲池，上中周二丈，外周四丈，廣一丈，下中周一丈四尺，外周二丈四尺，廣五尺，深一丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

"""
Suppose there is a curved pond. The upper middle circumference is 2 zhang, the outer circumference is 4 zhang, and the width is 1 zhang. 
The lower middle circumference is 1 zhang 4 chi, the outer circumference is 2 zhang 4 chi, and the width is 5 chi. 
The depth is 1 zhang. 
Question: what is the volume?

For curved ponds, the procedure is the same as for "Chutong," "Curved Ponds," "Pan Ponds," and "Dark Valleys." 
The procedure says: Double the upper length, and let the lower length follow it. 
Also, double the lower length, and let the upper length follow it. 
Multiply each by its width, add them together, and multiply by the height or depth. 
Divide the result by 6. 
For curved ponds, add the upper middle circumference and the outer circumference, then halve it to obtain the upper length. 
Similarly, add the lower middle circumference and the outer circumference, then halve it to obtain the lower length.

Answer: *a* chi.
"""

from fractions import Fraction

# 上中周二丈，外周四丈，廣一丈
上中周 = 2 * 10  # Convert zhang to chi
外周上 = 4 * 10  # Convert zhang to chi
廣上 = 1 * 10    # Convert zhang to chi

# 下中周一丈四尺，外周二丈四尺，廣五尺
下中周 = 1 * 10 + 4  # Convert zhang and chi to chi
外周下 = 2 * 10 + 4  # Convert zhang and chi to chi
廣下 = 5             # Already in chi

# 深一丈
深 = 1 * 10  # Convert zhang to chi

# 并上中、外周而半之，以為上袤
上袤 = Fraction(上中周 + 外周上, 2)

# 并下中、外周而半之，以為下袤
下袤 = Fraction(下中周 + 外周下, 2)

# 倍上袤，下袤從之
倍上袤 = 2 * 上袤
倍下袤 = 下袤

# 亦倍下袤，上袤從之
倍下袤_2 = 2 * 下袤
倍上袤_2 = 上袤

# 各以其廣乘之
積1 = 倍上袤 * 廣上
積2 = 倍下袤 * 廣下

# 并
總積 = 積1 + 積2

# 以高若深乘之
體積 = 總積 * 深

# 皆六而一
a = Fraction(體積, 6)  # Final volume in chi³
"""
Variable 'a' has wrong value. Expected: 5650/3, Actual: 3475/3"""
