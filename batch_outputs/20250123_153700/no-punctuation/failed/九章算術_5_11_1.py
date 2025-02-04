"""
秋程人功三百尺問用徒幾何
荅曰三萬三千五百八十二人功內少一十四尺四寸
一千人先到問當受袤幾何
術曰以一人功尺數乘先到人數為實并渠上下廣而半之以深乘之為法實如法得袤尺
荅曰 a丈 
"""

"""
Suppose there is an autumn project requiring 300 chi of work per person.
Question: how many workers are needed?

Answer: 33,582 person-work units, with 14 chi and 4 cun remaining.

If 1,000 workers arrive first, how much length should they complete?

The procedure says: Multiply the number of chi per person-work by the number of workers who arrive first, obtaining the dividend.
Add the upper and lower widths, divide by 2, and multiply by the depth, obtaining the divisor.
Divide the dividend by the divisor to get the length in chi.

Answer: *a* zhang.
"""

# 秋程人功三百尺
人功尺數 = 300

# 一千人先到
先到人數 = 1000

# 以一人功尺數乘先到人數，為實
實 = 人功尺數 * 先到人數

# 渠上下廣而半之
上下廣 = 2  # Assuming the upper and lower widths are equal to 2 chi each
渠廣 = Fraction(上下廣 + 上下廣, 2)

# 以深乘之，為法
深 = 1  # Assuming the depth is 1 chi
法 = 渠廣 * 深

# 實如法得袤尺
袤尺 = Fraction(實, 法)

# Convert to 丈 (1 丈 = 10 尺)
a = 袤尺 / 10
"""
Variable 'a' has wrong value. Expected: 12500/81, Actual: 15000"""
