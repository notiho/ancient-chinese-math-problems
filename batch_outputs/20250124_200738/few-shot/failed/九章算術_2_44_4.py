"""
今有出錢六百一十，買羽二千一百翭。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a翭 ， b翭 一錢 其 c翭 ， d翭 一錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 610 qian to purchase 2100 feathers (翭). It is desired to determine the rates of their value, distinguishing between expensive and cheap feathers.
Question: what are the rates of each?

The procedure for reversing the rates says: Take the total amount of money as the divisor (法), and the total number of feathers as the dividend (實). Perform the division to find the rate (number of feathers per qian). 
If the dividend does not fully divide the divisor, subtract the remainder from the divisor, making the divisor smaller and the dividend larger. 
For the two types of feathers, multiply the total number of feathers by the adjusted divisor and dividend to determine the quantities of each type.

Answer: *a* feathers at *b* feathers per qian, and *c* feathers at *d* feathers per qian.
"""

# 出錢六百一十
錢數 = 610

# 買羽二千一百翭
羽數 = 2100

# 以錢數為法
法 = 錢數

# 所率為實
實 = 羽數

# 實如法而一
貴率 = Fraction(實, 法)

# 不滿法者反以實減法，法少，實多
餘數 = 實 % 法
if 餘數 != 0:
    法 -= 餘數
    實 += 餘數

# 二物各以所得多少之數乘法實，即物數
貴羽數 = 法
賤羽數 = 實 - 法

# 貴賤率
貴率 = Fraction(貴羽數, 錢數)
賤率 = Fraction(賤羽數, 錢數)

a = 貴羽數
b = 貴率.denominator
c = 賤羽數
d = 賤率.denominator#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1140, Actual: 340
Variable 'b' has wrong value. Expected: 3, Actual: 61
Variable 'c' has wrong value. Expected: 960, Actual: 2030
Variable 'd' has wrong value. Expected: 4, Actual: 61"""
