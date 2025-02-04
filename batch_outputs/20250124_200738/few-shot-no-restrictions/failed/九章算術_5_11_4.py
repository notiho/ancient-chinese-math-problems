"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose the autumn work requires 300 chi of volume (e.g., digging or construction). 
Question: how many total person-days are required?

Answer: 33,582 person-days, with 14 chi and 4 cun remaining.

If 1,000 workers arrive first, question: how much length (袤) should they complete?

The procedure says: Multiply the number of chi per person-day by the number of workers who arrived first to obtain the dividend.
Add the upper and lower widths, divide by 2, and multiply by the depth to obtain the divisor.
Divide the dividend by the divisor to obtain the length in chi.

Answer: *a* zhang.
"""

from fractions import Fraction

# 秋程人功三百尺
秋程 = 300  # in chi

# 總人功：33,582人功，內少14尺4寸
總人功 = 33582
剩餘尺 = 14 + Fraction(4, 10)  # 4寸 = 4/10尺

# 一千人先到
先到人數 = 1000

# 每人功尺數
每人功尺數 = Fraction(秋程, 總人功)

# 以一人功尺數，乘先到人數為實
實 = 每人功尺數 * 先到人數

# 假設上下廣為10尺，深為2尺（需要具體數據，但這裡假設）
上下廣 = 10  # in chi
深 = 2  # in chi

# 并渠上下廣而半之，以深乘之為法
法 = (上下廣 / 2) * 深

# 實如法得袤尺
袤尺 = 實 / 法

# 將袤尺轉換為丈
a = 袤尺 / 10  # 1丈 = 10尺

# Answer
a  # in zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 12500/81, Actual: 0.08933357155619082"""
