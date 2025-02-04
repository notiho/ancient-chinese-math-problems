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
Answer: 174585 chi 6 cun.

Question 2: If one worker can dig 300 chi³, how many workers are needed, and how much work remains?

The procedure says:
- Multiply the number of chi³ one worker can dig by the number of workers already present, obtaining the dividend.
- Add the top and bottom widths, then halve the sum. Multiply this by the depth, obtaining the divisor.
- Divide the dividend by the divisor to obtain the length of the canal dug.
- Finally, calculate the number of workers needed and the remaining work.

Answer: *a* workers are needed, with *b* chi³ remaining.
"""

from fractions import Fraction

# Dimensions of the canal
上廣 = 1 * 10 + 8  # Convert 1 zhang 8 chi to chi
下廣 = 3 + Fraction(6, 10)  # Convert 3 chi 6 cun to chi
深 = 1 * 10 + 8  # Convert 1 zhang 8 chi to chi
袤 = 51824  # Length in chi

# Step 1: Calculate the total volume of the canal
# Add the top and bottom widths, then halve the sum
平均廣 = (上廣 + 下廣) / 2

# Multiply by depth and length to get the total volume
積 = 平均廣 * 深 * 袤

# Convert the total volume to chi and cun
積整數 = int(積)  # Integer part in chi
積餘數 = (積 - 積整數) * 10  # Fractional part in cun

# Total volume answer
總積 = f"{積整數} chi {積餘數} cun"

# Step 2: Calculate the number of workers needed
一人功 = 300  # One worker can dig 300 chi³

# Divide the total volume by the work per worker to get the number of workers
所需工人 = 積 // 一人功
剩餘工作 = 積 % 一人功

# Final answers
a = int(所需工人)  # Number of workers needed
b = 剩餘工作  # Remaining work in chi³

# Output results
總積, a, b
"""
Variable 'a' has wrong value. Expected: 33582, Actual: 33581
Variable 'b' has wrong value. Expected: 72/5, Actual: 1428/5"""
