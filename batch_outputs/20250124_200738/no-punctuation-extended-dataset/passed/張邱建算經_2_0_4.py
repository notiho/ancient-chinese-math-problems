"""
今有戸出銀一斤八兩一十二銖今以家有貧富不等令戸别作差品通融出之最下戸出銀八兩以次戸差各多三兩問戸㡬何
術曰置一戸出銀斤兩銖數以最下戸出銀兩銖數減之餘倍之以差多兩銖數加之為實以差兩銖數為法實如法而一
答曰 a戸
"""

#----- content starts here -----
"""
Suppose there is a household contributing 1 jin, 8 liang, and 12 zhu of silver. 
Now, because households have varying levels of wealth, it is ordered that each household contributes differently.
The poorest household contributes 8 liang of silver, and each subsequent household contributes 3 liang more than the previous one.
Question: how many households are there?

The procedure says: Place the total silver contribution in jin, liang, and zhu. 
Subtract the contribution of the poorest household in liang and zhu. 
Take the remainder, double it, and add the difference in liang and zhu for each household. 
This becomes the dividend. 
Take the difference in liang and zhu as the divisor. 
Divide the dividend by the divisor, obtaining the number of households.

Answer: there are *a* households.
"""

from fractions import Fraction

# 戸出銀一斤八兩一十二銖
總銀 = 1 * 16 * 24 + 8 * 24 + 12  # Convert to zhu (1 jin = 16 liang, 1 liang = 24 zhu)

# 最下戸出銀八兩
最下銀 = 8 * 24  # Convert to zhu

# 差多三兩
差銀 = 3 * 24  # Convert to zhu

# 以最下戸出銀兩銖數減之
餘銀 = 總銀 - 最下銀

# 餘倍之
餘倍 = 2 * 餘銀

# 以差多兩銖數加之，為實
實 = 餘倍 + 差銀

# 以差兩銖數為法
法 = 差銀

# 實如法而一
a = Fraction(實, 法)  # Number of households#----- content ends here -----

"""
"""
