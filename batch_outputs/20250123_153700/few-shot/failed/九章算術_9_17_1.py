"""
今有邑，東西七里，南北九里，各中開門。出東門十五里有木。問︰出南門幾何步而見木？
術曰：東門南至隅步數，以乘南門東至隅步數為實。以木去門步數為法。實如法而一。
荅曰： a步 。
"""

"""
Suppose there is a city. Its east-west length is 7 li, and its north-south length is 9 li. 
Each side has a gate in the middle. 
15 li east of the east gate, there is a tree. 
Question: how many steps south of the south gate must one go to see the tree?

The procedure says: Take the number of steps from the east gate south to the southeast corner and multiply it by the number of steps from the south gate east to the southeast corner, obtaining the dividend.
Take the number of steps from the tree to the east gate as the divisor.
Perform the division, obtaining the number of steps.

The answer says: *a* steps.
"""

# 城東西七里，南北九里
東西 = 7  # li
南北 = 9  # li

# 出東門十五里有木
木去東門 = 15  # li

# 1 里 = 300 步
步_per_里 = 300

# 東門南至隅步數
東門南至隅步數 = (南北 / 2) * 步_per_里

# 南門東至隅步數
南門東至隅步數 = (東西 / 2) * 步_per_里

# 以乘南門東至隅步數為實
實 = 東門南至隅步數 * 南門東至隅步數

# 以木去門步數為法
法 = 木去東門 * 步_per_里

# 實如法而一
a = Fraction(實, 法)  # Result in steps
"""
Code error: both arguments should be Rational instances"""
