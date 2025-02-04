"""
今有出錢六百一十，買羽二千一百翭。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a翭 ， b翭 一錢 其 c翭 ， d翭 一錢
"""

"""
Suppose there is an expenditure of 610 qian to buy 2100 feathers.
It is desired to determine the rates of their relative value (expensive and cheap feathers).
Question: how much is each rate?

The procedure for reversing the rates says: Take the total amount of money as the divisor (法), and take the total number of feathers as the dividend (實).
Divide the dividend by the divisor to obtain the base rate (實如法而一).
If the dividend does not divide evenly into the divisor, subtract the remainder from the divisor, making the divisor smaller and the dividend larger.
For the two types of feathers, multiply their respective quantities by the adjusted divisor and dividend to determine the number of feathers per qian.

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
基準率 = Fraction(實, 法)

# 不滿法者反以實減法，法少，實多
餘數 = 實 % 法
if 餘數 != 0:
    法 -= 餘數
    實 += 餘數

# 二物各以所得多少之數乘法實，即物數
a = 法  # Expensive feathers
b = Fraction(實, 法)  # Expensive feathers per qian
c = 實 - 法  # Cheap feathers
d = Fraction(法, 實 - 法)  # Cheap feathers per qian
"""
Variable 'a' has wrong value. Expected: 1140, Actual: 340
Variable 'b' has wrong value. Expected: 3, Actual: 237/34
Variable 'c' has wrong value. Expected: 960, Actual: 2030
Variable 'd' has wrong value. Expected: 4, Actual: 34/203"""
