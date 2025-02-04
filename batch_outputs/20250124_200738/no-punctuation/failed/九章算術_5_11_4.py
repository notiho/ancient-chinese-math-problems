"""
秋程人功三百尺問用徒幾何
荅曰三萬三千五百八十二人功內少一十四尺四寸
一千人先到問當受袤幾何
術曰以一人功尺數乘先到人數為實并渠上下廣而半之以深乘之為法實如法得袤尺
荅曰 a丈 
"""

#----- content starts here -----
"""
Suppose there is an autumn project requiring 300 chi of work per person. 
Question: how many workers are needed?

Answer: 33,582 person-chi, with 14 chi and 4 cun remaining.

If 1,000 workers arrive first, question: how much length should they complete?

The procedure says: Multiply the number of chi per person by the number of workers who arrived first, obtaining the dividend.
Add the upper and lower widths of the channel, and halve it.
Multiply this by the depth, obtaining the divisor.
Divide the dividend by the divisor, obtaining the length in chi.

Answer: *a* zhang.
"""

# 秋程人功三百尺
人功 = 300

# 一千人先到
先到人數 = 1000

# 渠上下廣 (assumed values for the problem)
渠上廣 = 10  # 上廣 in chi
渠下廣 = 8   # 下廣 in chi

# 渠深 (assumed value for the problem)
渠深 = 5  # 深 in chi

# 以一人功尺數乘先到人數，為實
實 = 人功 * 先到人數

# 并渠上下廣而半之
平均廣 = (渠上廣 + 渠下廣) / 2

# 以深乘之，為法
法 = 平均廣 * 渠深

# 實如法得袤尺
袤尺 = Fraction(實, 法)

# Convert 袤尺 to 丈 (1 丈 = 10 尺)
a = 袤尺 / 10#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
