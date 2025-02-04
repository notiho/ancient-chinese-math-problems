"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a(=12500/81)丈 。
"""

"""
Suppose there is an autumn project where the total labor is 300 chi. 
Question: how many workers are needed?

Answer: 33,582 person-labor units, with 14 chi and 4 cun less.

If 1,000 workers arrive first, question: how much length (mao) should they complete?

The procedure says: Multiply the number of chi per person-labor unit by the number of workers who arrive first to get the dividend.
Add the upper and lower widths of the channel and halve it. Multiply this by the depth to get the divisor.
Divide the dividend by the divisor to find the length in chi.

Answer: *a*(=12500/81) zhang.
"""

from fractions import Fraction

# 秋程人功三百尺
總人功 = 300

# 先到一千人
先到人數 = 1000

# 以一人功尺數，乘先到人數為實
一人功尺數 = Fraction(33_582, 總人功)  # 每人功尺數
實 = 一人功尺數 * 先到人數

# 渠上下廣而半之
渠上廣 = 1  # 假設值
渠下廣 = 1  # 假設值
平均廣 = Fraction(渠上廣 +渠
"""
Code error: '(' was never closed (<string>, line 32)"""
