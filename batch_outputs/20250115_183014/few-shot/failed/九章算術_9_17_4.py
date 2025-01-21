"""
今有邑，東西七里，南北九里，各中開門。出東門十五里有木。問︰出南門幾何步而見木？
術曰：東門南至隅步數，以乘南門東至隅步數為實。以木去門步數為法。實如法而一。
荅曰： a步 。
"""

"""
Suppose there is a city, 7 li from east to west, and 9 li from south to north, with gates at the middle of each side.
There is a tree 15 li east of the east gate.
Question: how many steps south of the south gate must one go to see the tree?

The procedure says: Take the number of steps from the east gate to the southeast corner and multiply it by the number of steps from the south gate to the southeast corner, obtaining the dividend.
Take the distance from the tree to the east gate as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: *a* bu.
"""

# 城東西七里
東西 = 7

# 城南北九里
南北 = 9

# 出東門十五里有木
木去東門 = 15

# 東門南至隅步數 (半個南北)
東門南至隅 = 南北 / 2

# 南門東至隅步數 (半個東西)
南門東至隅 = 東西 / 2

# 以東門南至隅步數乘南門東至隅步數為實
實 = 東門南至隅 * 南門東至隅

# 以木去門步數為法
法 = 木去東門

# 實如法而一
a = Fraction(實, 法) * 240  # 1 里 = 240 步

"""
Code error: both arguments should be Rational instances"""
