"""
今有程耕，一人一日發七畝，一人一日耕三畝，一人一日耰種五畝。今令一人一日自發、耕、耰種之，問︰治田幾何？
術曰：置發、耕、耰畝數，令互乘人數，并以為法。畝數相乘為實。實如法得一畝。
荅曰： a(=105/71)畝 。
"""

"""
Suppose there is a farming task. One person in one day can clear 7 mu, one person in one day can plow 3 mu, and one person in one day can harrow and sow 5 mu.
Now, let one person in one day perform all three tasks (clearing, plowing, and harrowing/sowing).
Question: how much land can be cultivated?

The procedure says: Place the mu numbers for clearing, plowing, and harrowing/sowing, and let them multiply with each other as if they were the number of people. Add these products together to form the divisor.
Multiply the mu numbers with each other to form the dividend.
Divide the dividend by the divisor to obtain the number of mu cultivated in one day.

Answer: *a*(=105/71) mu.
"""

# 一人一日發七畝
發畝 = 7

# 一人一日耕三畝
耕畝 = 3

# 一人一日耰種五畝
耰畝 = 5

# 畝數互乘人數，并以為法
法 = (發畝 * 耕畝) + (發畝 * 耰畝) + (耕畝 * 耰畝)

# 畝數相乘為實
實 = 發畝 * 耕畝 * 耰畝

# 實如法得一畝
a = Fraction(實, 法) # 105/71
"""
"""
