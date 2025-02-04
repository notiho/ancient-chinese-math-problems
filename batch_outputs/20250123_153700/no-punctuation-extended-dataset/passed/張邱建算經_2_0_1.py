"""
今有戸出銀一斤八兩一十二銖今以家有貧富不等令戸别作差品通融出之最下戸出銀八兩以次戸差各多三兩問戸㡬何
術曰置一戸出銀斤兩銖數以最下戸出銀兩銖數減之餘倍之以差多兩銖數加之為實以差兩銖數為法實如法而一
答曰 a戸
"""

"""
Suppose there is a household contributing 1 jin, 8 liang, and 12 zhu of silver. 
Now, due to varying wealth among households, it is ordered that each household contributes differently.
The poorest household contributes 8 liang, and each subsequent household contributes 3 liang more than the previous one.
Question: how many households are there?

The procedure says: Place the total silver contribution in jin, liang, and zhu.
Subtract the contribution of the poorest household in liang and zhu, and multiply the remainder by 2.
Add the difference in contribution (in liang and zhu) to this result, obtaining the dividend.
Take the difference in contribution (in liang and zhu) as the divisor.
Divide the dividend by the divisor to obtain the number of households.

Answer: there are *a* households.
"""

from fractions import Fraction

# Total contribution: 1 jin, 8 liang, 12 zhu
# 1 jin = 16 liang, 1 liang = 24 zhu
total_silver = (1 * 16 * 24) + (8 * 24) + 12  # Convert everything to zhu

# Contribution of the poorest household: 8 liang
poorest_household = 8 * 24  # Convert to zhu

# Difference in contribution between households: 3 liang
difference = 3 * 24  # Convert to zhu

# Subtract the poorest household's contribution
remainder = total_silver - poorest_household

# Multiply the remainder by 2 and add the difference
dividend = (2 * remainder) + difference

# Use the difference as the divisor
divisor = difference

# Divide to find the number of households
a = Fraction(dividend, divisor)  # Number of households in fractional form
"""
"""
