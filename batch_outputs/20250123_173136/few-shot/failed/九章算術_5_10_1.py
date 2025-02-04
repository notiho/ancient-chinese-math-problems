"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
荅曰：一千七萬四千五百八十五尺六寸。
秋程人功三百尺，問︰用徒幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a人 功。內少 b尺 。
"""

"""
Suppose there is a canal with the following dimensions:
- Top width: 1 zhang 8 chi
- Bottom width: 3 chi 6 cun
- Depth: 1 zhang 8 chi
- Length: 51824 chi

Question 1: What is the total volume?
Answer: 174585.6 cubic chi (or 1,000 zhang 7,458 chi 6 cun).

Question 2: If one worker can dig 300 cubic chi, how many workers are needed?
Procedure: Multiply the number of cubic chi a single worker can dig by the number of workers to get the total work done.
Add the top and bottom widths of the canal, divide by 2, and multiply by the depth to get the cross-sectional area.
Divide the total volume by the cross-sectional area to get the length of the canal that can be dug by the workers.
Answer: *a* workers are needed, with *b* cubic chi remaining.
"""

from fractions import Fraction

# Dimensions of the canal
上廣 = 1 * 10 + 8  # 1丈8尺 = 18尺
下廣 = 3 + Fraction(6, 10)  # 3尺6寸 = 3.6尺
深 = 1 * 10 + 8  # 1丈8尺 = 18尺
袤 = 51824  # Length of the canal in 尺

# Step 1: Calculate the cross-sectional area
# 并渠上下廣而半之
平均廣 = (上廣 + 下廣) / 2

# 以深乘之為法
截面積 = 平均廣 * 深

# Step 2: Calculate the total volume
積 = 截面積 * 袤  # Total volume in cubic 尺

# Step 3: Calculate the number of workers needed
一人功 = 300  # One worker can dig 300 cubic 尺

# Divide the total volume by the work of one worker
a = 積 // 一人功  # Number of full workers needed
b = 積 % 一人功  # Remaining cubic 尺

# Final results
a = int(a)  # Number of workers
b = float(b)  # Remaining cubic 尺
"""
Variable 'a' has wrong value. Expected: 33582, Actual: 33581
Variable 'b' has wrong value. Expected: 72/5, Actual: 285.6"""
