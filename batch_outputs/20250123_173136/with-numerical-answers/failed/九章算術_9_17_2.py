"""
今有邑，東西七里，南北九里，各中開門。出東門十五里有木。問︰出南門幾何步而見木？
術曰：東門南至隅步數，以乘南門東至隅步數為實。以木去門步數為法。實如法而一。
荅曰： a(=315)步 。
"""

"""
Suppose there is a city, 7 li from east to west, and 9 li from south to north, with gates in the middle of each side.
15 li east of the east gate, there is a tree.
Question: how many steps south of the south gate must one go to see the tree?

The procedure says: Multiply the number of steps from the east gate to the southeast corner by the number of steps from the south gate to the southeast corner, obtaining the dividend.
Use the number of steps from the tree to the east gate as the divisor.
Divide the dividend by the divisor to obtain the result.

The answer says: *a*(=315) steps.
"""

# 城東西七里，南北九里
東西 = 7
南北 = 9

# 出東門十五里有木
木去東門 = 15

# 里轉換為步 (1里 = 300步)
步每里 = 300
東西步 = 東西 * 步每里
南北步 = 南北 * 步每里
木去東門步 = 木去東門 * 步每里

# 東門南至隅步數
東門南至隅步數 = 南北步 / 2

# 南門東至隅步數
南門東至隅步數 = 東西步 / 2

# 以乘為實
實 = 東門南至隅步數 * 南門東至隅步數

# 以木去門步數為法
法 = 木去東門步

# 實如法而一
a = Fraction(實, 法) # 315 steps
"""
Code error: both arguments should be Rational instances"""
