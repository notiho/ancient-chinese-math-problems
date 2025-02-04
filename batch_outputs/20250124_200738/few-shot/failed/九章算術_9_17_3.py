"""
今有邑，東西七里，南北九里，各中開門。出東門十五里有木。問︰出南門幾何步而見木？
術曰：東門南至隅步數，以乘南門東至隅步數為實。以木去門步數為法。實如法而一。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a city. Its east-west length is 7 li, and its north-south length is 9 li. 
Each side has a gate located in the middle. 
There is a tree 15 li east of the east gate.
Question: how many steps south of the south gate must one go to see the tree?

The procedure says: Take the number of steps from the east gate southward to the corner and multiply it by the number of steps from the south gate eastward to the corner, obtaining the dividend.
Take the number of steps from the tree to the east gate as the divisor.
Divide the dividend by the divisor to obtain the result.

The answer says: *a* steps.
"""

# 城市東西七里，南北九里
東西 = 7  # 里
南北 = 9  # 里

# 出東門十五里有木
木去東門 = 15  # 里

# 轉換為步 (1 里 = 300 步)
東西步 = 東西 * 300
南北步 = 南北 * 300
木去東門步 = 木去東門 * 300

# 東門南至隅步數
東門南至隅步數 = 南北步 / 2

# 南門東至隅步數
南門東至隅步數 = 東西步 / 2

# 以乘為實
實 = 東門南至隅步數 * 南門東至隅步數

# 以木去門步數為法
法 = 木去東門步

# 實如法而一
a = Fraction(實, 法)  # 結果以步為單位#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
