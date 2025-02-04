"""
今有出錢六百一十買羽二千一百翭欲其貴賤率之問各幾何
反其率術曰以錢數為法所率為實實如法而一不滿法者反以實減法法少實多二物各以所得多少之數乘法實即物數
荅曰其 a翭  b翭 一錢 其 c翭  d翭 一錢
"""

"""
Suppose there is 610 qian (money) used to buy 2100 hu (feathers). It is desired to know the rates of their relative value (expensive and cheap).
Question: what are the rates of the expensive and cheap feathers?

The procedure for reversing rates says: Take the total money as the divisor (法). Take the total feathers as the dividend (實). Divide the dividend by the divisor to obtain the rate. If the rate is not an integer, reverse the calculation by subtracting the dividend from the divisor. If the divisor becomes smaller or the dividend becomes larger, calculate the rates for the two types of feathers by multiplying the divisor and dividend by their respective amounts.

Answer: The expensive feathers are *a* hu and *b* hu per qian. The cheap feathers are *c* hu and *d* hu per qian.
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
率 = Fraction(實, 法)

# 不滿法者反以實減法
貴率 = 率
賤率 = Fraction(法, 實)

# 法少實多，二物各以所得多少之數乘法實即物數
a = 貴率.numerator
b = 貴率.denominator
c = 賤率.numerator
d = 賤率.denominator
"""
Variable 'a' has wrong value. Expected: 1140, Actual: 210
Variable 'b' has wrong value. Expected: 3, Actual: 61
Variable 'c' has wrong value. Expected: 960, Actual: 61
Variable 'd' has wrong value. Expected: 4, Actual: 210"""
