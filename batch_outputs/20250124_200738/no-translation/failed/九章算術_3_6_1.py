"""
今有稟粟五斛，五人分之，欲令三人得三，二人得二。問︰各幾何？
術曰：置三人，人三；二人，人二，為列衰。副并為法。以五斛乘未并者，各自為實。實如法得一斛。
荅曰： a人 ，人得 b斛 。 c人 ，人得 d斗 。
"""

#----- content starts here -----

# 稟粟五斛
稟粟 = 5

# 置三人，人三；二人，人二，為列衰
三人 = 3
二人 = 2
列衰 = [三人 * 3, 二人 * 2]

# 副并為法
法 = sum(列衰)

# 以五斛乘未并者，各自為實
實 = [稟粟 * i for i in 列衰]

# 實如法得一斛
三人得 = Fraction(實[0], 法)
二人得 = Fraction(實[1], 法)

# Convert to 斛 and 斗 (1 斛 = 10 斗)
a = 3  # 三人
b = 三人得  # 每人得 b 斛

c = 2  # 二人
d = 二人得 * 10  # 每人得 d 斗#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 15/13, Actual: 45/13
Variable 'd' has wrong value. Expected: 100/13, Actual: 200/13"""
