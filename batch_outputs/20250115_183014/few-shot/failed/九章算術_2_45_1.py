"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a枚 ， b枚 一錢 其 c枚 ， d枚 一錢
"""

This problem involves determining the price ratio of two types of arrows (expensive and cheap) based on the total cost and total number of arrows. Let's carefully follow the procedure described in the problem.

"""
Suppose there is an expenditure of 980 qian to buy 5820 arrows.
It is desired to determine the price ratio of expensive and cheap arrows.
Question: what are the respective rates?

The procedure for reversing the rate says: Take the amount of money as the divisor, and the total number of arrows as the dividend.
Divide the dividend by the divisor to obtain the rate.
If the dividend is not divisible by the divisor, subtract the divisor from the dividend repeatedly.
The divisor decreases, and the dividend increases.
For the two types of items, multiply the amount of each by the divisor and the dividend to determine the number of each type.

Answer: *a* arrows at *b* arrows per qian, and *c* arrows at *d* arrows per qian.
"""

# 出錢九百八十
錢數 = 980

# 買矢簳五千八百二十枚
矢簳數 = 5820

# 以錢數為法
法 = 錢數

# 所率為實
實 = 矢簳數

# 實如法而一
每錢矢簳 = Fraction(實, 法)

# 不滿法者反以實減法，法少，實多
# Simplify the fraction to find the rates
b, d = 每錢矢簳.denominator, 每錢矢簳.numerator

# 二物各以所得多少之數乘法實，即物數
a = b * 法
c = d * 法

# Final results
a = Fraction(a, b + d)

"""
Code error: unterminated string literal (detected at line 2) (<string>, line 2)"""
