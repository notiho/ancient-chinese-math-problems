"""
今有程耕，一人一日發七畝，一人一日耕三畝，一人一日耰種五畝。今令一人一日自發、耕、耰種之，問︰治田幾何？
術曰：置發、耕、耰畝數，令互乘人數，并以為法。畝數相乘為實。實如法得一畝。
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is a task of farming:
- One person can clear (fa) 7 mu of land in one day.
- One person can plow (geng) 3 mu of land in one day.
- One person can harrow and sow (youzhong) 5 mu of land in one day.

Now, suppose one person is tasked to clear, plow, and harrow/sow the land in one day.
Question: how much land can they manage in one day?

The procedure says:
- Place the numbers of mu cleared, plowed, and harrowed/sown, and let them multiply with each other.
- Add them together to form the divisor (法).
- Multiply the mu numbers with each other to form the dividend (實).
- Divide the dividend by the divisor to obtain the result.

Answer: *a* mu.
"""

from fractions import Fraction

# 每日發、耕、耰種的畝數
發 = 7  # Clearing (fa)
耕 = 3  # Plowing (geng)
耰種 = 5  # Harrowing and sowing (youzhong)

# 令互乘人數，并以為法
法 = (發 * 耕) + (耕 * 耰種) + (發 * 耰種)

# 畝數相乘為實
實 = 發 * 耕 * 耰種

# 實如法得一畝
a = Fraction(實, 法)

a  # This is the result in mu.#----- content ends here -----

"""
"""
