"""
今有程耕，一人一日發七畝，一人一日耕三畝，一人一日耰種五畝。今令一人一日自發、耕、耰種之，問︰治田幾何？
術曰：置發、耕、耰畝數，令互乘人數，并以為法。畝數相乘為實。實如法得一畝。
荅曰： a(=105/71)畝 。
"""

"""
Suppose there is a farming task. One person can clear 7 mu in one day, one person can plow 3 mu in one day, and one person can harrow and sow 5 mu in one day.
Now, let one person perform all three tasks (clearing, plowing, and harrowing/sowing) in one day.
Question: how much land can they manage?

The procedure says: Place the mu numbers for clearing, plowing, and harrowing/sowing, and let them multiply each other as if they were the number of people.
Add these products together to form the divisor.
Multiply the mu numbers with each other to form the dividend.
Divide the dividend by the divisor to obtain the number of mu managed in one day.

Answer: *a*(=105/71) mu.
"""

# 發、耕、耰畝數
發 = 7
耕 = 3
耰 = 5

# 令互乘人數，并以為法
法 = (發 * 耕) + (耕 * 耰) + (耰 * 發)

# 畝數相乘為實
實 = 發 * 耕 * 耰

# 實如法得一畝
a = Fraction(實, 法) # 105/71
"""
"""
