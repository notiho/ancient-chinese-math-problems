"""
今有程耕，一人一日發七畝，一人一日耕三畝，一人一日耰種五畝。今令一人一日自發、耕、耰種之，問︰治田幾何？
術曰：置發、耕、耰畝數，令互乘人數，并以為法。畝數相乘為實。實如法得一畝。
荅曰： a畝 。
"""

"""
Suppose there is a task of farming. 
One person in one day can plow 7 mu, another person in one day can till 3 mu, and another person in one day can harrow and sow 5 mu.
Now, let one person in one day complete all three tasks (plowing, tilling, and harrowing/sowing).
Question: how much land can be farmed in one day?

The procedure says: Place the mu numbers for plowing, tilling, and harrowing/sowing.
Let them multiply each other, and sum them to form the divisor.
Multiply the mu numbers with each other to form the dividend.
Divide the dividend by the divisor to obtain the number of mu.

Answer: *a* mu.
"""

# 一人一日發七畝
發 = 7

# 一人一日耕三畝
耕 = 3

# 一人一日耰種五畝
耰 = 5

# 置發、耕、耰畝數，令互乘人數，并以為法
法 = (發 * 耕) + (發 * 耰) + (耕 * 耰)

# 畝數相乘為實
實 = 發 * 耕 * 耰

# 實如法得一畝
a = Fraction(實, 法)
"""
"""
