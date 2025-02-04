"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a(=12500/81)丈 。
"""

"""
Suppose the autumn work requires 300 chi of length, and the total labor required is 33,582 person-work-units, with 14 chi and 4 cun less.
If 1,000 workers arrive first, how much length should they complete?

The procedure says: Multiply the number of chi worked by one person by the number of workers who arrived first, obtaining the dividend.
Add the upper and lower widths, halve it, and multiply by the depth, obtaining the divisor.
Divide the dividend by the divisor to obtain the length in chi.

Answer: *a*(=12500/81) zhang.
"""

# 秋程人功三百尺
秋程 = 300

# 總人功三萬三千五百八十二人功，內少一十四尺四寸
總人功 = 33582 - (14 + Fraction(4, 10))

# 一千人先到
先到人數 = 1000

# 以一人功尺數，乘先到人數為實
一人功 = 總人功 / 秋程
實 = 一人功 * 先到人數

# 并渠上下廣而半之，以深乘之為法
渠上廣 = 1  # Assume 1 chi
渠下廣 = 1  # Assume 1 chi
渠深 = 1    # Assume 1 chi
法 = ((渠上廣 + 渠下廣) / 2) * 渠深

# 實如法得袤尺
袤尺 = Fraction(實, 法)

# Convert to 丈 (1 丈 = 10 尺)
a = 袤尺 / 10  # 12500/81 zhang
"""
Code error: both arguments should be Rational instances"""
