"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
荅曰：本 a錢 。利 b錢 。
"""

"""
Suppose someone holds money to trade with a profit rate of 13%. They return the following amounts over five repayments:
First repayment: 14,000
Second repayment: 13,000
Third repayment: 12,000
Fourth repayment: 11,000
Fifth repayment: 10,000
In total, the principal and interest are fully repaid.

Question: What are the principal (original money) and the total interest?

Answer: The principal is *a* qian, and the interest is *b* qian.
"""

# 利率 (profit rate)
利率 = Fraction(13, 100)

# 五次返歸的總和
總返歸 = 14000 + 13000 + 12000 + 11000 + 10000

# 本金和利息的關係
# 本金 + 本金 * 利率 = 總返歸
# 本金 * (1 + 利率) = 總返歸
本金 = Fraction(總返歸, 1 + 利率)

# 利息
利息 = 本金 * 利率

# 答案
a = 本金
b = 利息
"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 6000000/113
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 780000/113"""
