"""
今有出錢六百一十買羽二千一百翭欲其貴賤率之問各幾何
反其率術曰以錢數為法所率為實實如法而一不滿法者反以實減法法少實多二物各以所得多少之數乘法實即物數
荅曰其 a翭  b翭 一錢 其 c翭  d翭 一錢
"""

"""
Suppose there is a total of 610 qian spent to buy 2100 feathers (huo). 
It is desired to determine the rates of their relative value (expensive and cheap feathers).
Question: how many feathers correspond to each rate?

The procedure for reversing the rates says: Take the total money as the divisor (法). 
The total number of feathers is the dividend (實). 
Divide the dividend by the divisor to obtain the base rate. 
If the result is not an integer, reverse the calculation by subtracting the remainder from the divisor. 
If the divisor is smaller and the dividend is larger, multiply the divisor and dividend by the respective quantities of the two items to determine their counts.

Answer: *a* feathers and *b* feathers per qian for the expensive rate, and *c* feathers and *d* feathers per qian for the cheap rate.
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

# 不滿法者反以實減法
餘數 = 實 % 法
反法 = 法 - 餘數

# 法少實多，二物各以所得多少之數乘法實，即物數
貴羽 = Fraction(實, 反法)
賤羽 = Fraction(實, 法)

# Simplify the rates for expensive and cheap feathers
a, b = 貴羽.numerator, 貴羽.denominator
c, d = 賤羽.numerator, 賤羽.denominator
"""
Variable 'a' has wrong value. Expected: 1140, Actual: 105
Variable 'b' has wrong value. Expected: 3, Actual: 17
Variable 'c' has wrong value. Expected: 960, Actual: 210
Variable 'd' has wrong value. Expected: 4, Actual: 61"""
