"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose the total work for an autumn project is 300 chi (cubic feet of earthwork). 
Question: how many person-days of labor are required?

The answer says: 33,582 person-days of labor, with 14 chi and 4 cun remaining.

If 1,000 workers arrive first, question: how much length (袤) should they complete?

The procedure says: Multiply the number of chi of work per person by the number of workers who arrive first, obtaining the dividend.
Add the upper and lower widths, divide by 2, and multiply by the depth to obtain the divisor.
Divide the dividend by the divisor to obtain the length (袤).

The answer says: *a* zhang.
"""

from fractions import Fraction

# 秋程人功三百尺
總功 = 300  # Total work in cubic chi

# 每人功數
每人功 = Fraction(300, 33582)  # Each person's contribution in chi

# 內少一十四尺四寸
剩餘功 = Fraction(14, 1) + Fraction(4, 10)  # Remaining work in chi

# 一千人先到
先到人數 = 1000

# 以一人功尺數，乘先到人數為實
實 = 每人功 * 先到人數

# 渠上下廣而半之 (assuming width is uniform for simplicity)
上廣 = 1  # Upper width in chi
下廣 = 1  # Lower width in chi
平均廣 = Fraction(上廣 + 下廣, 2)  # Average width in chi

# 深度
深 = 1  # Depth in chi (assumed)

# 以深乘之為法
法 = 平均廣 * 深

# 實如法得袤尺
袤尺 = 實 / 法

# Convert 袤尺 to 丈 (1 丈 = 10 尺)
a = 袤尺 / 10  # Length in zhang

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 12500/81, Actual: 5000/5597"""
