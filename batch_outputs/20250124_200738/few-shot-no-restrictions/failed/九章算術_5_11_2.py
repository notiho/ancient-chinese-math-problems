"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose the total work for an autumn project is 300 chi. 
Question: how many person-days are required?

Answer: 33,582 person-days, with 14 chi and 4 cun remaining.

If 1,000 workers arrive first, question: how much length (mao) should they complete?

The procedure says: Multiply the number of chi per person-day by the number of workers who arrived first to get the dividend.
Add the upper and lower widths of the project, divide by 2, and multiply by the depth to get the divisor.
Divide the dividend by the divisor to get the length (mao) in chi.

Answer: *a* zhang.
"""

from fractions import Fraction

# 秋程人功三百尺
總工程 = 300  # chi

# 總人功：33,582人功，餘14尺4寸
總人功 = 33582 + Fraction(14, 10)  # Convert 4 cun to chi (1 chi = 10 cun)

# 一千人先到
先到人數 = 1000

# 每人功尺數
每人功 = 總工程 / 總人功  # chi per person-day

# 以一人功尺數，乘先到人數為實
實 = 每人功 * 先到人數  # Dividend

# 假設渠的上下廣與深
渠上廣 = 4  # chi (example value)
渠下廣 = 6  # chi (example value)
渠深 = 2  # chi (example value)

# 并渠上下廣而半之，以深乘之為法
法 = ((渠上廣 + 渠下廣) / 2) * 渠深  # Divisor

# 實如法得袤尺
袤尺 = Fraction(實, 法)

# Convert to zhang (1 zhang = 10 chi)
a = 袤尺 / 10  # Convert chi to zhang

a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
