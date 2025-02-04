"""
今有甲貸乙絹三疋約限至不還疋日息三尺今過限七日取絹二疋償錢三百問一疋直錢㡬何
術曰以過限日息尺數減取絹疋尺數餘為法以償錢乗一疋尺數為實實如法而一
答曰 a錢
"""

"""
Suppose person A lends person B 3 bolts of silk, with the agreement that if the repayment is overdue, interest accrues at a rate of 3 chi per bolt per day.
Now, after being overdue for 7 days, B repays 2 bolts of silk and 300 qian in money.
Question: how much is one bolt of silk worth in qian?

The procedure says: Subtract the overdue interest (in chi) from the total chi of the silk taken as repayment. The remainder is the divisor.
Multiply the repayment money by the chi of one bolt of silk to obtain the dividend.
Divide the dividend by the divisor to find the value of one bolt of silk.

The answer says: *a* qian.
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

# 計算過限日息尺數
過限息尺數 = 過限日 * 日息 * 貸絹

# 計算取絹疋的尺數
取絹尺數 = 取絹 * 10  # 每疋為 10 尺

# 以過限日息尺數減取絹疋尺數，餘為法
法 = 過限息尺數 - 取絹尺數

# 以償錢乘一疋尺數為實
實 = 償錢 * 10  # 每疋為 10 尺

# 實如法而一
a = Fraction(實, 法)  # 一疋直錢 a 錢
"""
Variable 'a' has wrong value. Expected: 12000/17, Actual: 3000/43"""
