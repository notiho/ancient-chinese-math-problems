"""
今有曲池上中周二丈外周四丈廣一丈下中周一丈四尺外周二丈四尺廣五尺深一丈問積幾何
芻童曲池盤池冥谷皆同術術曰倍上袤下袤從之亦倍下袤上袤從之各以其廣乘之并以高若深乘之皆六而一其曲池者并上中外周而半之以為上袤亦并下中外周而半之以為下袤
荅曰 a尺 
"""

"""
Suppose there is a curved pond with the following dimensions:
- Upper middle circumference: 2 zhang
- Outer circumference: 4 zhang
- Width: 1 zhang
- Lower middle circumference: 1 zhang 4 chi
- Outer circumference: 2 zhang 4 chi
- Width: 5 chi
- Depth: 1 zhang

Question: What is the total volume?

The procedure for curved ponds, circular ponds, and dark valleys is the same:
Double the upper length and the lower length, and add them together. 
Also double the lower length and the upper length, and add them together. 
Multiply each by their respective widths, then add them together. 
Multiply the result by the height or depth. 
Finally, divide by 6.

For curved ponds:
Add the upper, middle, and outer circumferences together, then halve them to get the upper length.
Similarly, add the lower, middle, and outer circumferences together, then halve them to get the lower length.

Answer: *a* chi³.
"""

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

# 并上中外周而半之，以為上袤
上袤 = (上中周 + 上外周 + 上中周) / 2

# 并下中外周而半之，以為下袤
下袤 = (下中周 + 下外周 + 下中周) / 2

# 倍上袤下袤從之
倍上袤下袤 = 2 * 上袤 + 下袤

# 倍下袤上袤從之
倍下袤上袤 = 2 * 下袤 + 上袤

# 各以其廣乘之
上積 = 倍上袤下袤 * 上廣
下積 = 倍下袤上袤 * 下廣

# 并以高若深乘之
總積 = (上積 + 下積) * 深

# 皆六而一
a = Fraction(總積, 6)  # Final volume in chi³
"""
Code error: both arguments should be Rational instances"""
