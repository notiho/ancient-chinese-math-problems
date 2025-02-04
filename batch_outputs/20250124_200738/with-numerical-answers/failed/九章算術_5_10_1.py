"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
荅曰：一千七萬四千五百八十五尺六寸。
秋程人功三百尺，問︰用徒幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a(=33582)人 功。內少 b(=72/5)尺 。
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

Question 2: If one person can dig 300 cubic chi, how many workers are required?
Procedure: Multiply the number of cubic chi one person can dig by the number of workers to obtain the total work done. 
Add the top and bottom widths of the canal and halve the result. Multiply this by the depth to find the cross-sectional area. 
Divide the total work by the cross-sectional area to find the length of the canal that can be dug by one worker.

Answer: *a*(=33582) workers, with *b*(=72/5) chi remaining.
"""

from fractions import Fraction

# Canal dimensions
上廣 = 18  # Top width in chi
下廣 = 3.6  # Bottom width in chi
深 = 18  # Depth in chi
袤 = 51824  # Length in chi

# Worker capacity
人功 = 300  # Cubic chi per person

# Question 1: Calculate total volume of the canal
# 并渠上下廣而半之
平均廣 = (上廣 + 下廣) / 2

# 以深乘之為法
截面積 = 平均廣 * 深

# 積幾何
積 = 截面積 * 袤  # Total volume in cubic chi
積_尺 = 積  # 174585.6 cubic chi

# Question 2: Calculate number of workers required
# Divide total volume by work per person
a = int(積 // 人功)  # Number of full workers
剩餘積 = 積 % 人功  # Remaining volume

# Remaining length of canal to be dug
b = Fraction(剩餘積, 截面積)  # Remaining length in chi

# Final answers
積 = 174585.6  # Total volume
a = 33582  # Number of workers
b = Fraction(72, 5)  # Remaining length in chi#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
