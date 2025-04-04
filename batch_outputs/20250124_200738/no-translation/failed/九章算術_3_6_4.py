"""
今有稟粟五斛，五人分之，欲令三人得三，二人得二。問︰各幾何？
術曰：置三人，人三；二人，人二，為列衰。副并為法。以五斛乘未并者，各自為實。實如法得一斛。
荅曰： a人 ，人得 b斛 。 c人 ，人得 d斗 。
"""

#----- content starts here -----

# 稟粟五斛
粟 = 5  # 斛

# 三人，人三；二人，人二，為列衰
列衰 = [3, 3, 3, 2, 2]

# 副并為法
法 = sum(列衰)

# 以五斛乘未并者，各自為實
實 = [粟 * i for i in列衰]

# 實如法得一斛
分配 = [Fraction(i, 法) for i in 實]

# 三人，每人得
a = 3
b = 分配[0]

# 二人，每人得
c = 2
d = 分配[3] * 10  # 1斛 = 10斗#----- content ends here -----

"""
Code error: invalid syntax. Perhaps you forgot a comma? (<string>, line 13)"""
