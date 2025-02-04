"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a丈 。
"""

#----- content starts here -----
### First part: Calculating total person-work for 秋程人功三百尺

# 秋程人功三百尺
秋程人功 = 300

# Total person-work is given as 33,582 person-units, with 14尺4寸 less
總人功 = 33582
少尺 = 14 + Fraction(4, 10)  # Convert 4寸 to fractional 尺

# Adjust total person-work
總人功 -= 少尺

### Second part: Calculating 袤 for 1,000 people arriving first

# 一千人先到
先到人數 = 1000

# 一人功尺數 (秋程人功)
一人功 = 秋程人功

# 以一人功尺數，乘先到人數為實
實 = 一人功 * 先到人數

# 并渠上下廣而半之
渠上廣 = 1  # Assume 上廣 = 1 尺
渠下廣 = 1  # Assume 下廣 = 1 尺
平均廣 = Fraction(渠上廣 + 渠下廣, 2)

# 以深乘之為法
深 = 1  # Assume 深 = 1 尺
法 = 平均廣 * 深

# 實如法得袤尺
袤 = Fraction(實, 法)

# Convert 袤 to 丈 (1 丈 = 10 尺)
a = Fraction(袤, 10)  # Convert 尺 to 丈#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 12500/81, Actual: 30000"""
