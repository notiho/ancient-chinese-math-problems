"""
今有戸出銀一斤八兩一十二銖今以家有貧富不等令戸别作差品通融出之最下戸出銀八兩以次戸差各多三兩問戸㡬何
術曰置一戸出銀斤兩銖數以最下戸出銀兩銖數減之餘倍之以差多兩銖數加之為實以差兩銖數為法實如法而一
答曰 a戸
"""

"""
Suppose there is a household contributing 1 jin, 8 liang, and 12 zhu of silver. 
Now, due to the varying wealth of households, it is ordered that each household contributes differently, with the poorest household contributing 8 liang. 
Each subsequent household contributes 3 liang more than the previous one.
Question: how many households are there?

The procedure says: Place the total silver contribution in jin, liang, and zhu. 
Subtract the silver contribution of the poorest household in liang and zhu, and multiply the remainder by 2. 
Add the difference in contribution (in liang and zhu) to this result, obtaining the dividend. 
Use the difference in contribution as the divisor. 
Divide the dividend by the divisor to obtain the number of households.

Answer: *a* households.
"""

from fractions import Fraction

# 戸出銀一斤八兩一十二銖
total_silver_jin = 1
total_silver_liang = 8
total_silver_zhu = 12

# Convert total silver to zhu (1 jin = 16 liang, 1 liang = 24 zhu)
total_silver = (total_silver_jin * 16 * 24) + (total_silver_liang * 24) + total_silver_zhu

# 最下戸出銀八兩
lowest_household_liang = 8
lowest_household_zhu = 0

# Convert lowest household contribution to zhu
lowest_household = (lowest_household_liang * 24) + lowest_household_zhu

# 差多三兩 (difference in contribution between households)
difference_liang = 3
difference_zhu = 0

# Convert difference to zhu
difference = (difference_liang * 24) + difference_zhu

# 以最下戸出銀兩銖數減之
remainder = total_silver - lowest_household

# 餘倍之
remainder_doubled = 2 * remainder

# 以差多兩銖數加之為實
dividend = remainder_doubled + difference

# 以差兩銖數為法
divisor = difference

# 實如法而一
a = Fraction(dividend, divisor)  # Number of households
"""
"""
