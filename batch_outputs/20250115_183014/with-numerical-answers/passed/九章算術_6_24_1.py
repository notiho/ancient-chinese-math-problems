"""
今有程耕，一人一日發七畝，一人一日耕三畝，一人一日耰種五畝。今令一人一日自發、耕、耰種之，問︰治田幾何？
術曰：置發、耕、耰畝數，令互乘人數，并以為法。畝數相乘為實。實如法得一畝。
荅曰： a(=105/71)畝 。
"""

"""
Suppose there is a farming task. One person in one day can clear 7 mu, one person in one day can plow 3 mu, and one person in one day can harrow and sow 5 mu.
Now, let one person in one day perform all three tasks (clearing, plowing, and harrowing/sowing).
Question: how much land can be managed in one day?

The procedure says: Place the mu numbers for clearing, plowing, and harrowing/sowing.
Let them multiply each other’s person numbers, and add them together to form the divisor.
Multiply the mu numbers with each other to form the dividend.
Divide the dividend by the divisor to obtain the number of mu.

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
