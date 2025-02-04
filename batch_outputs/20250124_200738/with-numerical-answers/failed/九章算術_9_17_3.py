"""
今有邑，東西七里，南北九里，各中開門。出東門十五里有木。問︰出南門幾何步而見木？
術曰：東門南至隅步數，以乘南門東至隅步數為實。以木去門步數為法。實如法而一。
荅曰： a(=315)步 。
"""

#----- content starts here -----
"""
Suppose there is a city, 7 li from east to west, and 9 li from south to north, with gates in the middle of each side.
15 li east of the east gate, there is a tree.
Question: how many bu south of the south gate will the tree be visible?

The procedure says: Take the number of bu from the east gate south to the southeast corner, and multiply it by the number of bu from the south gate east to the southeast corner, obtaining the dividend.
Take the number of bu from the tree to the east gate as the divisor.
Divide the dividend by the divisor to obtain the result.

The answer says: *a*(=315) bu.
"""

# 城東西七里，南北九里
東西 = 7  # 里
南北 = 9  # 里

# 出東門十五里有木
木去東門 = 15  # 里

# 1 里 = 300 步
里_to_步 = 300

# 東門南至隅步數
東門南至隅 = (南北 / 2) * 里_to_步  # 南北的一半

# 南門東至隅步數
南門東至隅 = (東西 / 2) * 里_to_步  # 東西的一半

# 木去門步數
木去門步數 = 木去東門 * 里_to_步

# 以東門南至隅步數乘南門東至隅步數為實
實 = 東門南至隅 * 南門東至隅

# 實如法而一
a = Fraction(實, 木去門步數)  # 315 步#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
