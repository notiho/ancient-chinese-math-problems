"""
今有邑，東西七里，南北九里，各中開門。出東門十五里有木。問︰出南門幾何步而見木？
術曰：東門南至隅步數，以乘南門東至隅步數為實。以木去門步數為法。實如法而一。
荅曰： a(=315)步 。
"""

"""
Suppose there is a city, 7 li from east to west, and 9 li from south to north, with gates in the middle of each side.
There is a tree 15 li east of the east gate.
Question: how many bu must one walk south from the south gate to see the tree?

The procedure says: Take the number of bu from the east gate south to the corner and multiply it by the number of bu from the south gate east to the corner, obtaining the dividend.
Take the number of bu from the tree to the gate as the divisor.
Divide the dividend by the divisor to obtain the result.

The answer says: *a*(=315) bu.
"""

# 城東西七里，南北九里
東西 = 7  # li
南北 = 9  # li

# 出東門十五里有木
木去東門 = 15  # li

# 1 里 = 300 步
里到步 = 300

# 將里轉換為步
東西步 = 東西 * 里到步
南北步 = 南北 * 里到步
木去東門步 = 木去東門 * 里到步

# 東門南至隅步數
東門南至隅步數 = 南北步 // 2

# 南門東至隅步數
南門東至隅步數 = 東西步 // 2

# 以乘為實
實 = 東門南至隅步數 * 南門東至隅步數

# 以木去門步數為法
法 = 木去東門步

# 實如法而一
a = Fraction(實, 法)  # 315 bu
"""
"""
