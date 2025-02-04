"""
今有程耕，一人一日發七畝，一人一日耕三畝，一人一日耰種五畝。今令一人一日自發、耕、耰種之，問︰治田幾何？
術曰：置發、耕、耰畝數，令互乘人數，并以為法。畝數相乘為實。實如法得一畝。
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is a farming task. One person can clear 7 mu in a day, one person can plow 3 mu in a day, and one person can harrow and sow 5 mu in a day.
Now, if one person is tasked to clear, plow, and harrow/sow by themselves in one day, how much land can they cultivate?

The procedure says: Place the mu numbers for clearing, plowing, and harrowing/sowing.
Let them multiply each other as if they represent the number of people, and sum them to form the divisor.
Multiply the mu numbers with each other to form the dividend.
Divide the dividend by the divisor to obtain the number of mu cultivated in one day.

The answer says: *a* mu.
"""

# 一人一日發七畝
發 = 7

# 一人一日耕三畝
耕 = 3

# 一人一日耰種五畝
耰 = 5

# 令互乘人數，并以為法
法 = (發 * 耕) + (發 * 耰) + (耕 * 耰)

# 畝數相乘為實
實 = 發 * 耕 * 耰

# 實如法得一畝
a = Fraction(實, 法)#----- content ends here -----

"""
"""
