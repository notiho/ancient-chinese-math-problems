"""
今有邑，東西七里，南北九里，各中開門。出東門十五里有木。問︰出南門幾何步而見木？
術曰：東門南至隅步數，以乘南門東至隅步數為實。以木去門步數為法。實如法而一。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a city, 7 li from east to west and 9 li from south to north, with gates in the middle of each side.
There is a tree 15 li east of the east gate.
Question: how many steps south of the south gate must one go to see the tree?

The procedure says: Multiply the number of steps from the east gate to the southeast corner by the number of steps from the south gate to the southeast corner, obtaining the dividend.
Use the distance from the tree to the east gate as the divisor.
Divide the dividend by the divisor to obtain the number of steps.

Answer: *a* steps.
"""

from fractions import Fraction

# 城市的東西和南北長度
東西 = 7  # 里
南北 = 9  # 里

# 木距離東門的距離
木距離東門 = 15  # 里

# 轉換為步數 (1 里 = 300 步)
里到步 = 300
東西步數 = 東西 * 里到步
南北步數 = 南北 * 里到步
木距離東門步數 = 木距離東門 * 里到步

# 東門到東南角的步數
東門到東南角步數 = 南北步數 // 2

# 南門到東南角的步數
南門到東南角步數 = 東西步數 // 2

# 計算實
實 = 東門到東南角步數 * 南門到東南角步數

# 計算步數
a = Fraction(實, 木距離東門步數)

a#----- content ends here -----

"""
"""
