"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a丈 。
"""

#----- content starts here -----
### First part: Calculating total 人功 and remaining 尺數

# 秋程人功三百尺
人功 = 300

# 總人功為三萬三千五百八十二人功
總人功 = 33582

# 內少一十四尺四寸
少尺 = 14 + Fraction(4, 10)  # 4寸 = 4/10尺

# 總尺數
總尺數 = 總人功 * 人功 - 少尺

### Second part: Calculating 袤 (length) for 1000 people

# 一千人先到
先到人數 = 1000

# 以一人功尺數，乘先到人數為實
實 = 人功 * 先到人數

# 渠上下廣而半之
上下廣 = 2  # Assuming 上下廣 is 2 (not explicitly given in the problem)
半廣 = Fraction(上下廣, 2)

# 以深乘之為法
深 = 1  # Assuming 深 is 1 (not explicitly given in the problem)
法 = 半廣 * 深

# 實如法得袤尺
袤尺 = Fraction(實, 法)

# Convert 袤尺 to 丈 (1丈 = 10尺)
a = 袤尺 / 10#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 12500/81, Actual: 30000"""
