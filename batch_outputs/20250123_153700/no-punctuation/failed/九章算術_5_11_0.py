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

If 1,000 workers arrive first, how much length of the project should they complete?

The procedure says: Multiply the number of chi of work per person by the number of workers who arrive first, obtaining the dividend.
Add the upper and lower widths of the project, and halve it.
Multiply this by the depth of the project, obtaining the divisor.
Divide the dividend by the divisor, obtaining the length in chi.

Answer: *a* zhang.
"""

# 秋程人功三百尺
人功 = 300

# 一千人先到
先到人數 = 1000

# 以一人功尺數乘先到人數，為實
實 = 人功 * 先到人數

# 渠上下廣
上廣 = 1  # Assume 1 chi (not specified in the problem)
下廣 = 1  # Assume 1 chi (not specified in the problem)

# 并渠上下廣而半之
平均廣 = (上廣 + 下廣) / 2

# 深
深 = 1  # Assume 1 chi (not specified in the problem)

# 以深乘之，為法
法 = 平均廣 * 深

# 實如法得袤尺
袤尺 = Fraction(實, 法)

# Convert to 丈 (1 丈 = 10 尺)
a = 袤尺 / 10
"""
Code error: both arguments should be Rational instances"""
