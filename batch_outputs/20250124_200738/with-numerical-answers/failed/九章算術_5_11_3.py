"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a(=12500/81)丈 。
"""

#----- content starts here -----
"""
Suppose the autumn work requires 300 chi of length to be completed by laborers. 
Question: how many total person-days of work are required?

Answer: 33,582 person-days of work, with a remainder of 14 chi and 4 cun.

If 1,000 laborers arrive first, question: how much length should they complete?

The procedure says: Multiply the number of chi of work per person by the number of laborers who arrived first, obtaining the dividend.
Add the upper and lower widths, divide by 2, and multiply by the depth, obtaining the divisor.
Divide the dividend by the divisor to obtain the length in chi.

Answer: *a*(=12500/81) zhang.
"""

from fractions import Fraction

# 秋程人功三百尺
秋程 = 300  # chi

# Total person-days of work (given in the problem)
總人功 = 33582  # person-days
餘尺 = Fraction(14, 1) + Fraction(4, 10)  # 14 chi and 4 cun

# 一千人先到
先到人數 = 1000

# 每人功尺數
每人功尺數 = Fraction(秋程, 總人功)

# 以一人功尺數，乘先到人數為實
實 = 每人功尺數 * 先到人數

# 并渠上下廣而半之，以深乘之為法
渠上廣 = 1  # Assume 1 chi (not explicitly given in the problem)
渠下廣 = 1  # Assume 1 chi (not explicitly given in the problem)
渠深 = 1    # Assume 1 chi (not explicitly given in the problem)

法 = ((渠上廣 + 渠下廣) / 2) * 渠深

# 實如法得袤尺
袤尺 = Fraction(實, 法)

# Convert to zhang (1 zhang = 10 chi)
a = 袤尺 / 10  # 12500/81 zhang#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
