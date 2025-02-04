"""
今有窖上廣四尺下廣七尺上袤五尺下袤八尺深一丈問受粟幾何
術曰倍上袤下袤從之亦倍下袤上袤從之各以其廣乘之併以深乘之六而一所得為實實如斛法而一得斛數
答曰得 a斛
"""

#----- content starts here -----
"""
Suppose there is a pit with an upper width of 4 chi, a lower width of 7 chi, an upper length of 5 chi, a lower length of 8 chi, and a depth of 1 zhang.
Question: how much millet can it hold?

The procedure says: Double the upper length and add it to the lower length. Also double the lower length and add it to the upper length.
Multiply each by its respective width. Add these results together and multiply by the depth.
Divide by 6 to obtain the volume.
Divide the result by the volume of one hu to obtain the number of hu.

Answer: it holds *a* hu.
"""

from fractions import Fraction

# 上廣四尺
上廣 = 4

# 下廣七尺
下廣 = 7

# 上袤五尺
上袤 = 5

# 下袤八尺
下袤 = 8

# 深一丈 (1 丈 = 10 尺)
深 = 10

# 倍上袤下袤從之
倍上袤 = 2 * 上袤 + 下袤

# 倍下袤上袤從之
倍下袤 = 2 * 下袤 + 上袤

# 各以其廣乘之
上積 = 倍上袤 * 上廣
下積 = 倍下袤 * 下廣

# 併以深乘之
總積 = (上積 + 下積) * 深

# 六而一所得為實
實 = Fraction(總積, 6)

# 斛法 (1 斛 = 10 尺³)
斛法 = 10

# 實如斛法而一得斛數
a = Fraction(實, 斛法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 18250/81, Actual: 73/2"""
