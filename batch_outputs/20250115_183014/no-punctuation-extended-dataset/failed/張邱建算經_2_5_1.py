"""
今有甲日行七十里乙日行九十里甲日以五分之一乃發乙日以三分之二乃發問乙行㡬何里及甲
術曰以五分日之一減三分日之二餘以甲日行里數乗之又以乙日行里數乗之為實以甲乙行里數相減餘以乗二分母為法實如法而一
答曰 a里
"""

"""
Suppose person A travels 70 li per day, and person B travels 90 li per day.
Person A starts after 1/5 of a day, and person B starts after 2/3 of a day.
Question: how far does person B travel, and how far does person A travel?

The procedure says: Subtract 1/5 of a day from 2/3 of a day.
Take the remainder and multiply it by the distance person A travels in a day.
Also multiply it by the distance person B travels in a day, obtaining the dividend.
Subtract the daily distances of A and B, and multiply the remainder by the product of the two denominators, obtaining the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: *a* li.
"""

from fractions import Fraction

# 甲日行七十里
甲日行里數 = 70

# 乙日行九十里
乙日行里數 = 90

# 甲日以五分之一乃發
甲發 = Fraction(1, 5)

# 乙日以三分之二乃發
乙發 = Fraction(2, 3)

# 以五分日之一減三分日之二
時間差 = 乙發 - 甲發

# 餘以甲日行里數乘之
甲實 = 甲日行里數 * 時間差

# 又以乙日行里數乘之
乙實 = 乙日行里數 * 時間差

# 為實
實 = 乙實 - 甲實

# 以甲乙行里數相減
行里數差 = 乙日行里數 - 甲日行里數

# 餘以乘二分母為法
法 = 行里數差 * (甲發.denominator * 乙發.denominator)

# 實如法而一
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 147, Actual: 7/225"""
