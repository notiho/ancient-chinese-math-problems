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
- Top width: 1 zhang 8 chi (18 chi)
- Bottom width: 3 chi 6 cun (3.6 chi)
- Depth: 1 zhang 8 chi (18 chi)
- Length: 51824 chi.

Question 1: What is the total volume of the canal?
Answer: 174585.6 cubic chi.

Question 2: If one worker can dig 300 cubic chi, how many workers are needed, and how much work remains?
Procedure:
1. Multiply the number of chi a single worker can dig (300 chi) by the number of workers already present to get the dividend.
2. Add the top and bottom widths, then halve the result. Multiply this by the depth to get the divisor.
3. Divide the dividend by the divisor to get the length of the canal dug by the workers.
4. Calculate the number of workers needed by dividing the total volume by the capacity of one worker.
5. Calculate the remaining volume after assigning workers.

Answer: *a* workers are needed, with *b* cubic chi remaining.
"""

from fractions import Fraction

# Canal dimensions
上廣 = 18  # Top width in chi
下廣 = 3.6  # Bottom width in chi
深 = 18  # Depth in chi
袤 = 51824  # Length in chi

# Worker capacity
一人功 = 300  # Volume one worker can dig in cubic chi

# Step 1: Calculate the total volume of the canal
# (上廣 + 下廣) / 2 * 深 * 袤
平均廣 = Fraction(上廣 + 下廣, 2)
積 = 平均廣 * 深 * 袤

# Step 2: Calculate the number of workers needed
# Total volume divided by one worker's capacity
所需人數 = 積 // 一人功

# Step 3: Calculate the remaining volume after assigning workers
剩餘積 = 積 % 一人功

# Final results
a = 所需人數
b = 剩餘積

# Outputs
a, b#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
