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

Question 2: If one worker can excavate 300 chi³, how many workers are needed, and how much volume remains unexcavated?

The procedure says:
- Multiply the number of chi³ one worker can excavate by the number of workers already accounted for to get the dividend.
- Add the top and bottom widths, then halve the result. Multiply this by the depth to get the divisor.
- Divide the dividend by the divisor to get the length of the canal excavated by the workers.
- The remaining length of the canal is calculated from the total length.

Answer: *a* workers are needed, and *b* chi³ remain unexcavated.
"""

# Dimensions of the canal
上廣 = 1 * 10 + 8  # Convert zhang and chi to chi
下廣 = 3 + Fraction(6, 10)  # Convert chi and cun to chi
深 = 1 * 10 + 8  # Convert zhang and chi to chi
袤 = 51824  # Length in chi

# Calculate the cross-sectional area of the canal
# (上廣 + 下廣) / 2 * 深
橫截面積 = Fraction(上廣 + 下廣, 2) * 深

# Calculate the total volume of the canal
積 = 橫截面積 * 袤

# Convert the total volume to chi and cun
積整數部分 = int(積)  # Integer part in chi³
積小數部分 = (積 - 積整數部分) * 10  # Fractional part in cun³

# Total volume in chi and cun
總積 = (積整數部分, 積小數部分)

# Worker capacity
一人功 = 300  # chi³ per worker

# Calculate the number of workers needed
a = 積整數部分 // 一人功  # Number of full workers
b = 積整數部分 % 一人功  # Remaining volume in chi³

# Final answers
總積_in_chi_cun = f"{積整數部分} chi {積小數部分} cun"
a_workers = a
b_remaining_volume = b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 33582, Actual: 33581
Variable 'b' has wrong value. Expected: 72/5, Actual: 285"""
