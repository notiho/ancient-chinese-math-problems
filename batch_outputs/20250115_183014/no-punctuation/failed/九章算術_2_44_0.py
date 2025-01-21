"""
今有出錢六百一十買羽二千一百翭欲其貴賤率之問各幾何
反其率術曰以錢數為法所率為實實如法而一不滿法者反以實減法法少實多二物各以所得多少之數乘法實即物數
荅曰其 a翭  b翭 一錢 其 c翭  d翭 一錢
"""

"""
Suppose there is an expenditure of 610 qian to purchase 2100 feathers (翭). 
It is desired to determine the rates of their relative value (贵 and 贱, expensive and cheap).
Question: how many feathers correspond to each rate?

The procedure for reversing rates says: Take the amount of money (钱数) as the divisor (法). 
Take the quantity being rated (所率) as the dividend (实). 
Divide the dividend by the divisor, obtaining the rate. 
If the dividend is less than the divisor, reverse the operation by subtracting the dividend from the divisor. 
If the divisor is smaller and the dividend larger, multiply the divisor and dividend by the respective quantities of the two items, obtaining the count of each item.

Answer: *a* feathers and *b* feathers per qian for one rate, and *c* feathers and *d* feathers per qian for the other rate.
"""

# 出錢六百一十
錢數 = 610

# 買羽二千一百翭
羽數 = 2100

# 貴賤率之
貴率 = Fraction(羽數, 錢數)
賤率 = Fraction(錢數, 羽數)

# 計算每一錢的翭數
a = 貴率.numerator
b = 貴率.denominator

c = 賤率.numerator
d = 賤率.denominator
"""
Variable 'a' has wrong value. Expected: 1140, Actual: 210
Variable 'b' has wrong value. Expected: 3, Actual: 61
Variable 'c' has wrong value. Expected: 960, Actual: 61
Variable 'd' has wrong value. Expected: 4, Actual: 210"""
