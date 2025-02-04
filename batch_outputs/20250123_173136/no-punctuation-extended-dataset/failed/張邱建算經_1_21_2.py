"""
今有甲貸乙絹三疋約限至不還疋日息三尺今過限七日取絹二疋償錢三百問一疋直錢㡬何
術曰以過限日息尺數減取絹疋尺數餘為法以償錢乗一疋尺數為實實如法而一
答曰 a錢
"""

"""
Suppose person A lends person B 3 bolts of silk, with the agreement that if the repayment is overdue, the daily interest is 3 chi per bolt.
Now, 7 days have passed beyond the limit. B repays 2 bolts of silk and 300 qian in money.
Question: how much is one bolt of silk worth in qian?

The procedure says: Take the overdue days and multiply by the interest rate in chi per day, then subtract the chi value of the silk bolts repaid. The remainder is the divisor.
Take the repayment money and multiply it by the chi value of one bolt of silk. This is the dividend.
Divide the dividend by the divisor to obtain the value of one bolt of silk.

Answer: *a* qian.
"""

from fractions import Fraction

# 甲貸乙絹三疋
貸絹 = 3

# 疋日息三尺
日息 = 3

# 過限七日
過限日 = 7

# 取絹二疋
取絹 = 2

# 償錢三百
償錢 = 300

# 一疋尺數
一疋尺數 = 1

# 以過限日息尺數
過限息尺數 = 過限日 * 日息 * 貸絹

# 減取絹疋尺數
取絹尺數 = 取絹 * 日息 * 一疋尺數
餘法 = 過限息尺數 - 取絹尺數

# 以償錢乘一疋尺數為實
實 = 償錢 * 一疋尺數

# 實如法而一
a = Fraction(實, 餘法)
"""
Variable 'a' has wrong value. Expected: 12000/17, Actual: 100/19"""
