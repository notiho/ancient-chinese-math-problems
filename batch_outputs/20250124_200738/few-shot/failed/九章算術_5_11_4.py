"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose the autumn project requires 300 chi of work per person. 
Question: how many total person-work units are needed?

The answer says: 33,582 person-work units, with 14 chi and 4 cun less.

If 1,000 workers arrive first, question: how much length (mao) should they complete?

The procedure says: Multiply the number of chi per person-work unit by the number of workers who arrive first, obtaining the dividend.
Add the upper and lower widths, halve it, and multiply by the depth to obtain the divisor.
Divide the dividend by the divisor to find the length in chi.

The answer says: *a* zhang.
"""

from fractions import Fraction

# 秋程人功三百尺
人功尺數 = 300

# 總人功數
總人功 = 33582 * 人功尺數 - (14 + Fraction(4, 10))

# 一千人先到
先到人數 = 1000

# 以一人功尺數，乘先到人數為實
實 = 人功尺數 * 先到人數

# 假設渠上下廣為 2 尺，深為 1 尺 (需要具體數據)
上廣 = 2
下廣 = 2
深 = 1

# 并渠上下廣而半之
平均廣 = Fraction(上廣 + 下廣, 2)

# 以深乘之為法
法 = 平均廣 * 深

# 實如法得袤尺
袤尺 = Fraction(實, 法)

# 轉換為丈 (1 丈 = 10 尺)
a = Fraction(袤尺, 10)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 12500/81, Actual: 15000"""
