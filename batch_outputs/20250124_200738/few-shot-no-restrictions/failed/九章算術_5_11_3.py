"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose the autumn work requires 300 chi of work. 
Question: how many total person-days are required?

Answer: 33,582 person-days, with 14 chi and 4 cun remaining.

If 1,000 people arrive first, question: how much length (mao) should they complete?

The procedure says: Take the number of chi of work per person and multiply it by the number of people who arrived first to get the dividend.
Add the upper and lower widths, divide by 2, and multiply by the depth to get the divisor.
Divide the dividend by the divisor to get the length in chi.

Answer: *a* zhang.
"""

from fractions import Fraction

# 秋程人功三百尺
秋程 = 300  # Total work in chi

# 總人功：三萬三千五百八十二人功，內少一十四尺四寸
總人功 = 33582  # Total person-days
剩餘尺 = 14 + Fraction(4, 10)  # Remaining work in chi (14 chi and 4 cun)

# 一千人先到
先到人數 = 1000

# 每人功尺數
每人功 = Fraction(秋程, 總人功)  # Work per person in chi

# 以一人功尺數，乘先到人數為實
實 = 每人功 * 先到人數

# 假設渠上下廣為 1 丈，深為 1 丈
渠上廣 = 10  # Upper width in chi (1 zhang = 10 chi)
渠下廣 = 10  # Lower width in chi
渠深 = 10  # Depth in chi

# 并渠上下廣而半之
平均廣 = (渠上廣 + 渠下廣) / 2

# 以深乘之為法
法 = 平均廣 * 渠深

# 實如法得袤尺
袤尺 = Fraction(實, 法)

# Convert 袤尺 to 丈 (1 丈 = 10 尺)
a = 袤尺 / 10  # Length in zhang

# Output the result
a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
