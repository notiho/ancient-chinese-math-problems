"""
今有邑，東西七里，南北九里，各中開門。出東門十五里有木。問︰出南門幾何步而見木？
術曰：東門南至隅步數，以乘南門東至隅步數為實。以木去門步數為法。實如法而一。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a city, 7 li from east to west, and 9 li from south to north, with gates at the middle of each side.
There is a tree 15 li east of the east gate.
Question: how many steps south of the south gate must one go to see the tree?

The procedure says: Multiply the number of steps from the east gate to the southeast corner by the number of steps from the south gate to the southeast corner, obtaining the dividend.
Use the distance from the tree to the east gate as the divisor.
Divide the dividend by the divisor to get the answer.

Answer: *a* steps.
"""

from fractions import Fraction

# 城市東西七里，南北九里
東西 = 7  # li
南北 = 9  # li

# 出東門十五里有木
木距東門 = 15  # li

# 東門南至隅步數 (從東門到東南角的距離)
東門南至隅 = 南北 / 2  # li

# 南門東至隅步數 (從南門到東南角的距離)
南門東至隅 = 東西 / 2  # li

# 以東門南至隅步數乘南門東至隅步數為實
實 = 東門南至隅 * 南門東至隅

# 以木去門步數為法
法 = 木距東門

# 實如法而一
a = Fraction(實, 法) * 1000  # Convert li to steps (1 li = 1000 steps)

a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
