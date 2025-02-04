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

# 城的東西長度和南北長度
東西 = 7  # 里
南北 = 9  # 里

# 木距離東門的距離
木距東門 = 15  # 里

# 東門到東南隅的步數（東西長度的一半）
東門到東南隅 = Fraction(東西, 2)  # 里

# 南門到東南隅的步數（南北長度的一半）
南門到東南隅 = Fraction(南北, 2)  # 里

# 計算實（東門到東南隅 * 南門到東南隅）
實 = 東門到東南隅 * 南門到東南隅

# 以木去門步數為法
法 = 木距東門

# 實如法而一
a = Fraction(實, 法) * 300  # 1里 = 300步

a#----- content ends here -----

"""
"""
