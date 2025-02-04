"""
今有程耕，一人一日發七畝，一人一日耕三畝，一人一日耰種五畝。今令一人一日自發、耕、耰種之，問︰治田幾何？
術曰：置發、耕、耰畝數，令互乘人數，并以為法。畝數相乘為實。實如法得一畝。
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is a task of farming:
- One person can clear 7 mu of land in one day.
- One person can plow 3 mu of land in one day.
- One person can harrow and sow 5 mu of land in one day.

Now, let one person perform all three tasks (clearing, plowing, and harrowing/sowing) in one day.
Question: how much land can they manage in one day?

The procedure says:
- Place the mu numbers for clearing, plowing, and harrowing/sowing.
- Multiply them with each other to obtain the numerator (實).
- Add the mu numbers together to form the denominator (法).
- Divide the numerator by the denominator to obtain the result.

Answer: *a* mu.
"""

# 一人一日發七畝
發 = 7

# 一人一日耕三畝
耕 = 3

# 一人一日耰種五畝
耰 = 5

# 畝數相乘為實
實 = 發 * 耕 * 耰

# 畝數相加為法
法 = 發 + 耕 + 耰

# 實如法得一畝
a = Fraction(實, 法)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 105/71, Actual: 7"""
