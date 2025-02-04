"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
荅曰：一千七萬四千五百八十五尺六寸。
秋程人功三百尺，問︰用徒幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a人 功。內少 b尺 。
"""

#----- content starts here -----
"""
Suppose there is a canal with an upper width of 1 zhang 8 chi, a lower width of 3 chi 6 cun, a depth of 1 zhang 8 chi, and a length of 51824 chi.
Question: what is the volume?

Answer: 174585.6 cubic chi.

If one person can dig 300 cubic chi in a day, how many workers are needed?

The procedure says: Multiply the number of chi a person can dig in a day by the number of workers already present, obtaining the dividend.
Add the upper and lower widths of the canal and halve the result. Multiply this by the depth to obtain the divisor.
Divide the dividend by the divisor to obtain the length in chi.

Answer: *a* workers are needed, with *b* chi remaining.
"""

from fractions import Fraction

# Canal dimensions
上廣 = 1 * 10 + 8  # Convert zhang and chi to chi
下廣 = 3 * 10 + 6  # Convert chi and cun to chi
深 = 1 * 10 + 8  # Convert zhang and chi to chi
袤 = 51824  # Length in chi

# Calculate the volume of the canal
平均廣 = Fraction(上廣 + 下廣, 2)  # Average width
積 = 平均廣 * 深 * 袤  # Volume in cubic chi

# Worker productivity
人功 = 300  # One person can dig 300 cubic chi per day

# Calculate the number of workers needed
a = 積 // 人功  # Number of workers needed
b = 積 % 人功  # Remaining cubic chi

a = int(a)
b = float(b)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 33582, Actual: 83954
Variable 'b' has wrong value. Expected: 72/5, Actual: 264.0"""
