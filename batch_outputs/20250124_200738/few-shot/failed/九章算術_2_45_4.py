"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a枚 ， b枚 一錢 其 c枚 ， d枚 一錢
"""

#----- content starts here -----
"""
Suppose 980 qian (money) is spent to buy 5820 arrows. It is desired to determine the rates of expensive and cheap arrows.
Question: how many are expensive, and how many are cheap, and what are their respective rates?

The procedure for reversing the rates says: Take the total amount of money as the divisor. The total number of items is the dividend. Divide the dividend by the divisor to get the base rate (1 qian per x items). If the dividend is not divisible by the divisor, subtract the remainder from the divisor, making the divisor smaller and the dividend larger. For the two types of items, multiply the total number of items by the adjusted divisor and dividend to determine the counts of each type.

Answer: *a* arrows at *b* arrows per qian, and *c* arrows at *d* arrows per qian.
"""

from fractions import Fraction

# 出錢九百八十
錢數 = 980

# 買矢簳五千八百二十枚
矢簳數 = 5820

# 以錢數為法
法 = 錢數

# 所率為實
實 = 矢簳數

# 實如法而一
基準率 = Fraction(實, 法)

# 不滿法者反以實減法，法少，實多
餘數 = 實 % 法
調整法 = 法 - 餘數
調整實 = 實 + 餘數

# 二物各以所得多少之數乘法實，即物數
貴矢數 = Fraction(調整法, 法) * 矢簳數
賤矢數 = Fraction(餘數, 法) * 矢簳數

# 貴矢率
貴矢率 = Fraction(調整法, 法) * 基準率.denominator

# 賤矢率
賤矢率 = Fraction(餘數, 法) * 基準率.denominator

a = 貴矢數
b = 貴矢率
c = 賤矢數
d = 賤矢率#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 300, Actual: 17460/49
Variable 'b' has wrong value. Expected: 5, Actual: 3
Variable 'c' has wrong value. Expected: 5520, Actual: 267720/49
Variable 'd' has wrong value. Expected: 6, Actual: 46"""
