"""
今有甲日行七十里乙日行九十里甲日以五分之一乃發乙日以三分之二乃發問乙行㡬何里及甲
術曰以五分日之一減三分日之二餘以甲日行里數乗之又以乙日行里數乗之為實以甲乙行里數相減餘以乗二分母為法實如法而一
答曰 a里
"""

"""
Suppose there are two travelers, A and B. A travels 70 li per day, and B travels 90 li per day.
A starts after 1/5 of the day, and B starts after 2/3 of the day.
Question: how far has B traveled when they meet, and how far has A traveled?

The procedure says: Subtract 1/5 of the day from 2/3 of the day, and take the remainder.
Multiply this remainder by the distance A travels per day, and also multiply it by the distance B travels per day, obtaining the dividends.
Subtract the daily distances of A and B, and multiply the remainder by the product of the two denominators, obtaining the divisor.
Divide the dividends by the divisor to find the distances traveled by A and B.

Answer: B has traveled *a* li, and A has traveled *b* li.
"""

from fractions import Fraction

# 甲日行七十里
甲日行 = 70

# 乙日行九十里
乙日行 = 90

# 甲日以五分之一乃發
甲發 = Fraction(1, 5)

# 乙日以三分之二乃發
乙發 = Fraction(2, 3)

# 以五分日之一減三分日之二
餘 = 乙發 - 甲發

# 餘以甲日行里數乘之
甲實 = 餘 * 甲日行

# 又以乙日行里數乘之
乙實 = 餘 * 乙日行

# 以甲乙行里數相減
差 = 乙日行 - 甲日行

# 餘以乘二分母為法
法 = 差 * (甲發.denominator * 乙發.denominator)

# 實如法而一
a = Fraction(乙實, 法)
b = Fraction(甲實, 法)
"""
Variable 'a' has wrong value. Expected: 147, Actual: 7/50"""
