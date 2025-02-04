"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
荅曰：一千七萬四千五百八十五尺六寸。
秋程人功三百尺，問︰用徒幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a人 功。內少 b尺 。
"""

"""
Suppose there is a canal with an upper width of 1 zhang 8 chi, a lower width of 3 chi 6 cun, a depth of 1 zhang 8 chi, and a length of 51824 chi.
Question: what is the total volume?

The answer says: 174585.6 cubic chi.

If one worker can dig 300 cubic chi, how many workers are needed?

The procedure says: Multiply the number of cubic chi a single worker can dig by the number of workers already present, obtaining the dividend.
Add the upper and lower widths of the canal and halve the result. Multiply this by the depth to obtain the divisor.
Divide the dividend by the divisor to obtain the length in chi.

The answer says: *a* workers are needed, with *b* cubic chi remaining.
"""

from fractions import Fraction

# Canal dimensions
上廣 = 1 * 10 + 8  # Convert 1丈8尺 to 尺
下廣 = 3 * 10 + 6  # Convert 3尺6寸 to 尺
深 = 1 * 10 + 8    # Convert 1丈8尺 to 尺
袤 = 51824         # Length in 尺

# Add upper and lower widths and halve
平均廣 = Fraction(上廣 + 下廣, 2)

# Compute the total volume
積 = 平均廣 * 深 * 袤

# Worker capacity
人功 = 300  # One worker can dig 300 cubic chi

# Compute the number of workers needed
a = 積 // 人功  # Integer division to find the number of full workers
b = 積 % 人功  # Remainder to find the leftover cubic chi

a = int(a)
b = float(b)
"""
Variable 'a' has wrong value. Expected: 33582, Actual: 83954
Variable 'b' has wrong value. Expected: 72/5, Actual: 264.0"""
