"""
今有共買豕，人出一百，盈一百；人出九十，適足。問︰人數、豕價各幾何？
盈、適足，不足、適足術曰：以盈及不足之數為實。置所出率，以少減多，餘為法。實如法得一人。其求物價者，以適足乘人數得物價。
荅曰： a人 ，豕價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys a pig. If each person contributes 100, there is a surplus of 100. If each person contributes 90, the amount is exactly sufficient.
Question: how many people are there, and what is the price of the pig?

The procedure says: Take the surplus and the deficit amounts as the dividend.
Place the contribution rates, subtract the smaller from the larger, and the remainder is the divisor.
Divide the dividend by the divisor to obtain the number of people.
To find the price of the pig, multiply the exact contribution rate by the number of people.

Answer: *a* people, and the price of the pig is *b*.
"""

from fractions import Fraction

# 盈一百 (surplus of 100)
盈 = 100

# 出率 100 (contribution rate when surplus)
出率_盈 = 100

# 出率 90 (contribution rate when exact)
出率_適足 = 90

# 以盈及不足之數為實 (take surplus as the dividend)
實 = 盈

# 置所出率，以少減多，餘為法 (subtract smaller rate from larger rate for divisor)
法 = 出率_盈 - 出率_適足

# 實如法得一人 (divide dividend by divisor to get the number of people)
人數 = Fraction(實, 法)

# 其求物價者，以適足乘人數得物價 (multiply exact contribution rate by number of people to get the price of the pig)
豕價 = 出率_適足 * 人數

a = 人數
b = 豕價

print(f"人數: {a} 人")
print(f"豕價: {b} 單位")#----- content ends here -----

"""
"""
