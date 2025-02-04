"""
今有程耕，一人一日發七畝，一人一日耕三畝，一人一日耰種五畝。今令一人一日自發、耕、耰種之，問︰治田幾何？
術曰：置發、耕、耰畝數，令互乘人數，并以為法。畝數相乘為實。實如法得一畝。
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is a farming task. One person can clear 7 mu of land in one day, one person can plow 3 mu of land in one day, and one person can harrow and sow 5 mu of land in one day.
Now, let one person perform all three tasks (clearing, plowing, and harrowing/sowing) in one day.
Question: how much land can be cultivated in one day?

The procedure says: Place the mu numbers for clearing, plowing, and harrowing/sowing. Multiply them with each other, and sum them to form the divisor.
Multiply the mu numbers with each other to form the dividend.
Divide the dividend by the divisor to obtain the number of mu cultivated in one day.

Answer: *a* mu.
"""

from fractions import Fraction

# 每人每日的工作效率
發 = 7  # 清理土地（發）
耕 = 3  # 耕地
耰 = 5  # 耰種

# 令互乘人數，并以為法
法 = (發 * 耕) + (耕 * 耰) + (耰 * 發)

# 畝數相乘為實
實 = 發 * 耕 * 耰

# 實如法得一畝
a = Fraction(實, 法)

a  # 答案: 每人每日可以完成 a 畝的田地#----- content ends here -----

"""
"""
