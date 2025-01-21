"""
今有曲池上中周二丈外周四丈廣一丈下中周一丈四尺外周二丈四尺廣五尺深一丈問積幾何
芻童曲池盤池冥谷皆同術術曰倍上袤下袤從之亦倍下袤上袤從之各以其廣乘之并以高若深乘之皆六而一其曲池者并上中外周而半之以為上袤亦并下中外周而半之以為下袤
荅曰 a尺 
"""

"""
Suppose there is a curved pond. Its upper middle circumference is 2 zhang, its outer circumference is 4 zhang, and its width is 1 zhang.
Its lower middle circumference is 1 zhang 4 chi, its outer circumference is 2 zhang 4 chi, and its width is 5 chi.
Its depth is 1 zhang.
Question: what is the volume?

The procedure for curved ponds, circular ponds, and deep valleys is the same:
Double the upper length and the lower length, and multiply them together.
Also double the lower length and the upper length, and multiply them together.
Multiply each by their respective widths, sum them, and then multiply by the height or depth.
Divide the result by 6.
For curved ponds, sum the upper, middle, and outer circumferences and halve them to get the upper length.
Similarly, sum the lower, middle, and outer circumferences and halve them to get the lower length.

The answer says: *a* chi³.
"""

# 上中周二丈
上中周 = 2 * 10  # Convert zhang to chi

# 外周四丈
上外周 = 4 * 10  # Convert zhang to chi

# 廣一丈
上廣 = 1 * 10  # Convert zhang to chi

# 下中周一丈四尺
下中周 = 1 * 10 + 4  # Convert zhang to chi and add chi

# 外周二丈四尺
下外周 = 2 * 10 + 4  # Convert zhang to chi and add chi

# 廣五尺
下廣 = 5  # Already in chi

# 深一丈
深 = 1 * 10  # Convert zhang to chi

# 并上中外周而半之，以為上袤
上袤 = (上中周 + 上外周) / 2

# 并下中外周而半之，以為下袤
下袤 = (下中周 + 下外周) / 2

# 倍上袤下袤從之
倍上袤下袤 = 2 * 上袤 * 下袤

# 倍下袤上袤從之
倍下袤上袤 = 2 * 下袤 * 上袤

# 各以其廣乘之
上積 = 倍上袤下袤 * 上廣
下積 = 倍下袤上袤 * 下廣

# 并以高若深乘之
總積 = (上積 + 下積) * 深

# 皆六而一
a = Fraction(總積, 6)  # Volume in chi³
"""
Code error: both arguments should be Rational instances"""
