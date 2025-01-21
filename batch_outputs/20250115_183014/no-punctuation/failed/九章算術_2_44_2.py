"""
今有出錢六百一十買羽二千一百翭欲其貴賤率之問各幾何
反其率術曰以錢數為法所率為實實如法而一不滿法者反以實減法法少實多二物各以所得多少之數乘法實即物數
荅曰其 a翭  b翭 一錢 其 c翭  d翭 一錢
"""

"""
Suppose there is an expenditure of 610 qian to buy 2100 feathers. It is desired to determine the rates of their relative value.
Question: how many feathers correspond to each rate of value?

The procedure for reversing the rates says: Take the total amount of money as the divisor (法). Take the total number of feathers as the dividend (實). Divide the dividend by the divisor, obtaining the rate. If the result is not an integer, reverse the calculation by subtracting the remainder from the divisor. If the divisor becomes smaller or the dividend becomes larger, multiply each of the two items by the corresponding adjusted divisor or dividend to determine the number of feathers for each rate.

Answer: *a* feathers and *b* feathers per qian for one rate, and *c* feathers and *d* feathers per qian for the other rate.
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
每錢羽數 = Fraction(實, 法)

# 不滿法者反
整羽數 = 每錢羽數.numerator
整錢數 = 每錢羽數.denominator

# 以實減法，法少實多
a = 整羽數 // 整錢數
b = 整羽數 % 整錢數
c = 整錢數
d = 1
"""
Variable 'a' has wrong value. Expected: 1140, Actual: 3
Variable 'b' has wrong value. Expected: 3, Actual: 27
Variable 'c' has wrong value. Expected: 960, Actual: 61
Variable 'd' has wrong value. Expected: 4, Actual: 1"""
