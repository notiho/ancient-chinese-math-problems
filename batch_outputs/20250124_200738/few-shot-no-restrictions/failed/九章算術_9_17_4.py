"""
今有邑，東西七里，南北九里，各中開門。出東門十五里有木。問︰出南門幾何步而見木？
術曰：東門南至隅步數，以乘南門東至隅步數為實。以木去門步數為法。實如法而一。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a city, 7 li from east to west, and 9 li from south to north, with gates in the middle of each side.
There is a tree 15 li east of the east gate.
Question: how many steps south of the south gate must one go to see the tree?

The procedure says: Multiply the number of steps from the east gate to the southeast corner by the number of steps from the south gate to the southeast corner, obtaining the dividend.
Use the distance from the tree to the east gate as the divisor.
Divide the dividend by the divisor to obtain the answer.

Answer: *a* bu.
"""

from fractions import Fraction

# 城市東西七里，南北九里
東西 = 7  # li
南北 = 9  # li

# 出東門十五里有木
木距東門 = 15  # li

# 東門南至隅步數 (半個南北距離)
東門南至隅 = 南北 / 2  # li

# 南門東至隅步數 (半個東西距離)
南門東至隅 = 東西 / 2  # li

# 術曰：以東門南至隅步數乘南門東至隅步數為實
實 = 東門南至隅 * 南門東至隅  # li^2

# 以木去門步數為法
法 = 木距東門  # li

# 實如法而一
a = Fraction(實, 法)  # li

# Convert the result from li to bu (1 li = 300 bu)
a_in_bu = a * 300

a_in_bu#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
