"""
今有穿渠上廣一丈八尺下廣三尺六寸深一丈八尺袤五萬一千八百二十四尺問積幾何
荅曰一千七萬四千五百八十五尺六寸
秋程人功三百尺問用徒幾何
術曰以一人功尺數乘先到人數為實并渠上下廣而半之以深乘之為法實如法得袤尺
荅曰 a人 功內少 b尺 
"""

"""
Suppose there is a canal with the following dimensions:
- Top width: 1 zhang 8 chi
- Bottom width: 3 chi 6 cun
- Depth: 1 zhang 8 chi
- Length: 51824 chi

Question 1: What is the total volume of the canal?
Answer: 174585 chi^3 6 cun^3.

Question 2: If one worker can dig 300 chi^3, how many workers are needed, and how much volume remains after assigning the work?

The procedure says:
- Multiply the number of chi^3 one worker can dig by the number of workers already assigned to get the dividend.
- Add the top and bottom widths, then halve the sum.
- Multiply this by the depth to get the divisor.
- Divide the dividend by the divisor to get the length of the canal dug.
- For the remaining volume, subtract the total volume dug by the workers from the total canal volume.

Answer: *a* workers are needed, and *b* chi^3 remain.
"""

from fractions import Fraction

# Dimensions of the canal
上廣 = 1 * 10 + 8  # Convert 1 zhang 8 chi to chi
下廣 = 3 + Fraction(6, 10)  # Convert 3 chi 6 cun to chi
深 = 1 * 10 + 8  # Convert 1 zhang 8 chi to chi
袤 = 51824  # Length in chi

# Step 1: Calculate the total volume of the canal
# 并渠上下廣而半之
平均廣 = (上廣 + 下廣) / 2

# 以深乘之為法
截面積 = 平均廣 * 深

# 積 = 截面積 * 袤
積 = 截面積 * 袤

# Convert the total volume to chi^3 and cun^3
積整 = int(積)  # Whole chi^3
積餘 = (積 - 積整) * 10  # Remaining cun^3

# Total volume answer
總積 = (積整, 積餘)  # 174585 chi^3 6 cun^3

# Step 2: Calculate the number of workers and remaining volume
一人功 = 300  # One worker can dig 300 chi^3

# Calculate the number of workers needed
a = 積 // 一人功  # Number of workers
b = 積 % 一人功  # Remaining volume in chi^3

# Final answers
總積  # Total volume of the canal
a, b  # Number of workers and remaining volume
"""
Variable 'a' has wrong value. Expected: 33582, Actual: 33581
Variable 'b' has wrong value. Expected: 72/5, Actual: 1428/5"""
