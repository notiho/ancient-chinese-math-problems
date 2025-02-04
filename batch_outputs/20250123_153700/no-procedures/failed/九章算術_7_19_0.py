"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
荅曰：本 a錢 。利 b錢 。
"""

"""
Suppose a person holds some amount of money as capital and earns a profit rate of 13%. 
They return the money in five installments: 14,000, 13,000, 12,000, 11,000, and 10,000. 
After these five returns, both the principal and the profit are fully repaid.

Question: What are the original principal (capital) and the total profit?

Answer: The principal is *a* qian, and the profit is *b* qian.
"""

# 利率 (profit rate)
利率 = Fraction(13, 100)

# 五次返歸的錢
返歸 = [14000, 13000, 12000, 11000, 10000]

# 計算總返歸的錢
總返歸 = sum(返歸)

# 本金 + 利息 = 總返歸 / (1 + 利率)
本金 = Fraction(總返歸, 1 + 利率)

# 利息 = 總返歸 - 本金
利息 = 總返歸 - 本金

# 答案
a = 本金
b = 利息
"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 6000000/113
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 780000/113"""
