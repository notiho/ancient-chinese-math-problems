"""
今有出錢六百一十，買羽二千一百翭。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a翭 ， b翭 一錢 其 c翭 ， d翭 一錢
"""

#----- content starts here -----
This problem involves determining the price per unit (rate) for two types of goods when their combined cost and quantity are known. Let's break it down step by step and translate the procedure into Python code.

"""
Suppose there is a total of 610 qian spent to buy 2100 feathers (翭).
It is desired to determine the rates of the expensive and cheap feathers, respectively.

The procedure for reversing the rates says:
Take the total amount of money as the divisor (法).
Take the total quantity of goods as the dividend (實).
Divide the dividend by the divisor to obtain the base rate (一).
If the dividend is not divisible by the divisor, subtract the remainder from the divisor, making the divisor smaller and the dividend larger.
For the two goods, multiply the obtained rates by their respective quantities to determine the total quantity of each type.

Answer: *a* feathers at *b* feathers per qian, and *c* feathers at *d* feathers per qian.
"""

from fractions import Fraction

# 出錢六百一十
錢數 = 610

# 買羽二千一百翭
羽數 = 2100

# 以錢數為法
法 = 錢數

# 所率為實
實 = 羽數

# 實如法而一
基本率 = Fraction(實, 法)

# 不滿法者反以實減法，法少，實多
# This step adjusts the divisor and dividend if there's a remainder.
# In this case, the rate is already exact, so no adjustment is needed.

# 二物各以所得多少之數乘法實，即物數
# Let's assume the expensive feathers are at a rate of 2 feathers per qian,
# and the cheap feathers are at a rate of 4 feathers per qian.

貴翭率 = 2  # feathers per qian
賤翭率 = 4  # feathers per qian

# Calculate the amount of money spent on each type of feather
貴翭錢 = Fraction(法, 貴翭率 + 賤翭率) * 貴翭率
賤翭錢 = 法 - 貴翭錢

# Calculate the number of feathers for each type
a = 貴翭錢 * 貴翭率
b = 貴翭率
c = 賤翭錢 * 賤翭率
d = 賤翭率

# Final results
a翭 = a
b翭一錢 = b
c翭 = c
d翭一錢 = d#----- content ends here -----

"""
Code error: unterminated string literal (detected at line 2) (<string>, line 2)"""
