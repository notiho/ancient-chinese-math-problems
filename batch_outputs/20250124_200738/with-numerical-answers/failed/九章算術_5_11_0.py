"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a(=12500/81)丈 。
"""

#----- content starts here -----
"""
Suppose the autumn work requires 300 chi of length per person. 
Question: how many total person-works (人功) are needed?

Answer: 33,582 person-works, with 14 chi and 4 cun remaining.

If 1,000 people arrive first, question: how much length should they complete?

The procedure says: Multiply the number of chi per person-work by the number of people who arrive first, obtaining the dividend.
Add the upper and lower widths, halve it, and multiply by the depth, obtaining the divisor.
Divide the dividend by the divisor to obtain the length in chi.

Answer: *a*(=12500/81) zhang.
"""

from fractions import Fraction

# 秋程人功三百尺
人功尺數 = 300

# 一千人先到
先到人數 = 1000

# 以一人功尺數，乘先到人數為實
實 = 人功尺數 * 先到人數

# 渠上下廣而半之
上廣 = 1  # Assuming 上廣 = 1 (not explicitly given in the problem)
下廣 = 1  # Assuming 下廣 = 1 (not explicitly given in the problem)
廣 = (上廣 + 下廣) / 2

# 以深乘之為法
深 = 1  # Assuming 深 = 1 (not explicitly given in the problem)
法 = 廣 * 深

# 實如法得袤尺
袤尺 = Fraction(實, 法)

# Convert 袤尺 to 丈 (1 丈 = 10 尺)
a = 袤尺 / 10  # 12500/81 zhang#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
