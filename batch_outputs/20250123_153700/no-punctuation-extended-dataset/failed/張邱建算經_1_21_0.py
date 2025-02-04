"""
今有甲貸乙絹三疋約限至不還疋日息三尺今過限七日取絹二疋償錢三百問一疋直錢㡬何
術曰以過限日息尺數減取絹疋尺數餘為法以償錢乗一疋尺數為實實如法而一
答曰 a錢
"""

"""
Suppose A lends B 3 bolts of silk, with the agreement that if the repayment is overdue, interest accrues at a rate of 3 chi per bolt per day.
Now, after being overdue for 7 days, B repays 2 bolts of silk and 300 qian in money.
Question: how much is one bolt of silk worth in qian?

The procedure says: Multiply the overdue days by the interest rate in chi per day per bolt, then subtract the chi equivalent of the silk bolts repaid.
The remainder is the divisor.
Multiply the repayment money by the chi equivalent of one bolt of silk to get the dividend.
Divide the dividend by the divisor to get the value of one bolt of silk.

Answer: *a* qian.
"""

from fractions import Fraction

# 甲貸乙絹三疋
貸絹 = 3

# 疋日息三尺
日息 = 3

# 今過限七日
過限日 = 7

# 取絹二疋
取絹 = 2

# 償錢三百
償錢 = 300

# 一疋尺數
一疋尺數 = 240  # 1 bolt = 240 chi (standard conversion)

# 以過限日息尺數
過限息尺數 = 過限日 * 日息 * 貸絹

# 減取絹疋尺數
取絹尺數 = 取絹 * 一疋尺數
餘法 = 過限息尺數 - 取絹尺數

# 以償錢乘一疋尺數為實
實 = 償錢 * 一疋尺數

# 實如法而一
a = Fraction(實, 餘法)  # 一疋直錢

"""
Variable 'a' has wrong value. Expected: 12000/17, Actual: -24000/139"""
