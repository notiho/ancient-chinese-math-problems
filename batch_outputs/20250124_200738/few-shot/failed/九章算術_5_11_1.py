"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose the autumn work requires 300 chi of labor. 
Question: how many person-days of labor are required?

Answer: 33,582 person-days of labor, with 14 chi and 4 cun remaining.

If 1,000 workers arrive first, question: how much length (mao) should they complete?

The procedure says: Multiply the number of chi of work per person by the number of workers who arrive first, obtaining the dividend.
Add the upper and lower widths of the channel, and halve it.
Multiply this by the depth, obtaining the divisor.
Divide the dividend by the divisor to obtain the length in chi.

Answer: *a* zhang.
"""

from fractions import Fraction

# 秋程人功三百尺
人功 = 300

# 總人功數
總人功 = 33582 + Fraction(14, 10)  # 14 chi and 4 cun (4 cun = 0.4 chi)

# 一千人先到
先到人數 = 1000

# 每人功尺數
每人功 = Fraction(總人功, 人功)

# 以一人功尺數，乘先到人數為實
實 = 每人功 * 先到人數

# 渠上下廣而半之
渠上廣 = 1  # Assume 1 chi for simplicity (not specified in the problem)
渠下廣 = 1  # Assume 1 chi for simplicity (not specified in the problem)
平均廣 = Fraction(渠上廣 + 渠下廣, 2)

# 以深乘之為法
深 = 1  # Assume 1 chi for simplicity (not specified in the problem)
法 = 平均廣 * 深

# 實如法得袤尺
袤尺 = Fraction(實, 法)

# Convert to zhang (1 zhang = 10 chi)
a = Fraction(袤尺, 10)  # Convert chi to zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 12500/81, Actual: 167917/15"""
