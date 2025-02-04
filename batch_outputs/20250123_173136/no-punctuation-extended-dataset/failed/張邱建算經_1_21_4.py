"""
今有甲貸乙絹三疋約限至不還疋日息三尺今過限七日取絹二疋償錢三百問一疋直錢㡬何
術曰以過限日息尺數減取絹疋尺數餘為法以償錢乗一疋尺數為實實如法而一
答曰 a錢
"""

"""
Suppose person A lends person B 3 bolts of silk, with the agreement that if the repayment is overdue, the daily interest is 3 chi per bolt.
Now, 7 days have passed beyond the agreed limit, and B repays 2 bolts of silk and 300 qian in money.
Question: how much is one bolt of silk worth in qian?

The procedure says: Subtract the overdue daily interest (in chi) from the total chi of the silk taken as repayment. The remainder is the divisor.
Multiply the repayment money by the chi of one bolt of silk to get the dividend.
Divide the dividend by the divisor to find the value of one bolt of silk.

Answer: one bolt of silk is worth *a* qian.
"""

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
一疋尺數 = 240  # Assuming 1 bolt of silk = 240 chi (standard conversion in ancient Chinese math)

# 過限日息尺數
過限息尺數 = 貸絹 * 日息 * 過限日

# 取絹疋尺數
取絹尺數 = 取絹 * 一疋尺數

# 以過限日息尺數減取絹疋尺數，餘為法
法 = 過限息尺數 - 取絹尺數

# 以償錢乘一疋尺數，為實
實 = 償錢 * 一疋尺數

# 實如法而一
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 12000/17, Actual: -24000/139"""
