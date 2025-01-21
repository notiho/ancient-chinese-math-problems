"""
今有程耕一人一日發七畝一人一日耕三畝一人一日耰種五畝今令一人一日自發耕耰種之問治田幾何
術曰置發耕耰畝數令互乘人數并以為法畝數相乘為實實如法得一畝
荅曰 a畝 
"""

"""
Suppose there is a system where:
- One person in one day can clear 7 mu,
- One person in one day can plow 3 mu,
- One person in one day can sow 5 mu.

Now, let one person in one day perform all three tasks (clearing, plowing, and sowing) by themselves.
Question: how much land can they manage in one day?

The procedure says: Place the mu numbers for clearing, plowing, and sowing.
Let them multiply with each other, and sum the results to form the divisor.
Multiply the mu numbers with each other to form the dividend.
Divide the dividend by the divisor to obtain the number of mu.

The answer says: *a* mu.
"""

# 發一日七畝
發 = 7

# 耕一日三畝
耕 = 3

# 耰種一日五畝
耰 = 5

# 令互乘人數并，以為法
法 = (發 * 耕) + (發 * 耰) + (耕 * 耰)

# 畝數相乘，為實
實 = 發 * 耕 * 耰

# 實如法，得一畝
a = Fraction(實, 法)
"""
"""
