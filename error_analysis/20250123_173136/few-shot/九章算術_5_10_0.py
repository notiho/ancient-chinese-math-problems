"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
荅曰：一千七萬四千五百八十五尺六寸。
秋程人功三百尺，問︰用徒幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a人 功。內少 b尺 。
"""

"""
Suppose there is a canal with an upper width of 1 zhang 8 chi, a lower width of 3 chi 6 cun, a depth of 1 zhang 8 chi, and a length of 51824 chi.
Question 1: What is the total volume?
Answer: 174585.6 cubic chi (or 1 zhang 7 qian 4 bai 5 shi 8 wu chi 6 cun).

Question 2: If one worker can dig 300 cubic chi, how many workers are needed?
The procedure says: Multiply the number of chi a single worker can dig by the number of workers already calculated to get the dividend.
Add the upper and lower widths of the canal, halve it, and multiply by the depth to get the divisor.
Divide the dividend by the divisor to get the length in chi.

Answer: *a* workers are needed, with *b* cubic chi remaining.
"""

from fractions import Fraction

# Canal dimensions
上廣 = 1 * 10 + 8  # Convert 1 zhang 8 chi to chi
下廣 = 3 + Fraction(6, 10)  # Convert 3 chi 6 cun to chi
深 = 1 * 10 + 8  # Convert 1 zhang 8 chi to chi
袤 = 51824  # Length in chi

# Calculate the total volume
平均廣 = (上廣 + 下廣) / 2  # Average width
積 = 平均廣 * 深 * 袤  # Total volume in cubic chi

# Worker capacity
人功 = 300  # One worker can dig 300 cubic chi

# Calculate the number of workers needed
#ERR: misunderstood expression
# 內少 -> cubic chi remaining
a = 積 // 人功  # Number of full workers needed
b = 積 % 人功  # Remaining cubic chi
a = (積 // 人功) + 1  # Number of full workers needed
b = 人功 * a - 積  # Remaining cubic chi

a = int(a)
#ERR: code error (fractions)
#b = float(b)
"""
Variable 'a' has wrong value. Expected: 33582, Actual: 33581
Variable 'b' has wrong value. Expected: 72/5, Actual: 285.6"""
