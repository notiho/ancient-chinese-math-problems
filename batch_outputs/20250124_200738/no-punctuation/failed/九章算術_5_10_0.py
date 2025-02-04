"""
今有穿渠上廣一丈八尺下廣三尺六寸深一丈八尺袤五萬一千八百二十四尺問積幾何
荅曰一千七萬四千五百八十五尺六寸
秋程人功三百尺問用徒幾何
術曰以一人功尺數乘先到人數為實并渠上下廣而半之以深乘之為法實如法得袤尺
荅曰 a人 功內少 b尺 
"""

#----- content starts here -----
"""
Suppose there is a canal with the following dimensions:
- Top width: 1 zhang 8 chi
- Bottom width: 3 chi 6 cun
- Depth: 1 zhang 8 chi
- Length: 51824 chi

Question 1: What is the total volume of the canal?
Answer: 174585 chi 6 cun.

Question 2: If one worker can dig 300 chi^3, how many workers are needed, and how much work remains?

The procedure says:
- Multiply the number of chi^3 one worker can dig by the number of workers already calculated, obtaining the dividend.
- Add the top and bottom widths, then halve the result. Multiply this by the depth to obtain the divisor.
- Divide the dividend by the divisor to obtain the length in chi.
- Calculate the number of workers and the remaining work.

Answer: *a* workers are needed, with *b* chi^3 remaining.
"""

from fractions import Fraction

# Dimensions of the canal
上廣 = 1 * 10 + 8  # Convert zhang and chi to chi
下廣 = 3 + Fraction(6, 10)  # Convert chi and cun to chi
深 = 1 * 10 + 8  # Convert zhang and chi to chi
袤 = 51824  # Length in chi

# Calculate the average width
平均廣 = (上廣 + 下廣) / 2

# Calculate the total volume of the canal
積 = 平均廣 * 深 * 袤

# Convert the volume to chi and cun
積整數部分 = int(積)
積小數部分 = 積 - 積整數部分
積寸 = 積小數部分 * 10  # Convert fractional chi to cun

# Total volume in chi and cun
積總 = (積整數部分, 積寸)

# Worker capacity
一人功 = 300

# Calculate the number of workers needed
a = 積整數部分 // 一人功
剩餘尺 = 積整數部分 % 一人功

# Remaining work in chi
b = 剩餘尺

# Final results
積結果 = f"{積整數部分} chi {積寸} cun"
a結果 = a
b結果 = b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 33582, Actual: 33581
Variable 'b' has wrong value. Expected: 72/5, Actual: 285"""
