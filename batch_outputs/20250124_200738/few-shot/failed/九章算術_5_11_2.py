"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is an autumn project requiring 300 chi of work per person. 
Question: how many total person-work units are needed?

Answer: 33,582 person-work units, with 14 chi and 4 cun remaining.

If 1,000 workers arrive first, question: how much length (mao) should they complete?

The procedure says: Multiply the number of chi of work per person by the number of workers who arrive first, obtaining the dividend.
Add the upper and lower widths of the channel and halve it, then multiply by the depth, obtaining the divisor.
Divide the dividend by the divisor to obtain the length in chi.

Answer: *a* zhang.
"""

from fractions import Fraction

# 秋程人功三百尺
人功 = 300

# 一千人先到
先到人數 = 1000

# 以一人功尺數，乘先到人數為實
實 = 人功 * 先到人數

# 渠上下廣而半之 (assume upper width = 2 chi, lower width = 2 chi)
上廣 = 2
下廣 = 2
平均廣 = Fraction(上廣 + 下廣, 2)

# 以深乘之為法 (assume depth = 1 chi)
深 = 1
法 = 平均廣 * 深

# 實如法得袤尺
袤尺 = Fraction(實, 法)

# Convert to 丈 (1 丈 = 10 尺)
a = 袤尺 / 10#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 12500/81, Actual: 15000"""
