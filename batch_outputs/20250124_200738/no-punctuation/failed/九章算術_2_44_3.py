"""
今有出錢六百一十買羽二千一百翭欲其貴賤率之問各幾何
反其率術曰以錢數為法所率為實實如法而一不滿法者反以實減法法少實多二物各以所得多少之數乘法實即物數
荅曰其 a翭  b翭 一錢 其 c翭  d翭 一錢
"""

#----- content starts here -----
"""
Suppose there is 610 qian used to buy 2100 feathers. It is desired to know the rates of their relative value (expensive and cheap feathers).
Question: how many feathers correspond to each rate?

The procedure for reversing rates says: Take the amount of money as the divisor (法), and the quantity being rated as the dividend (實).
Divide the dividend by the divisor, obtaining the rate. If the result is not an integer, reverse the process by subtracting the dividend from the divisor.
If the divisor becomes smaller than the dividend, or the dividend becomes larger than the divisor, multiply the divisor and dividend by the respective quantities of the two goods.
The result gives the quantities of each good.

Answer: *a* feathers and *b* feathers per qian for one rate, and *c* feathers and *d* feathers per qian for the other rate.
"""

# 出錢六百一十
錢數 = 610

# 買羽二千一百翭
羽數 = 2100

# 貴賤率反其率術
# 以錢數為法
法 = 錢數

# 所率為實
實 = 羽數

# 實如法而一
貴率 = Fraction(實, 法)

# 不滿法者反以實減法
賤率 = Fraction(法, 實)

# 法少實多，二物各以所得多少之數乘法實即物數
a = 貴率.numerator
b = 貴率.denominator
c = 賤率.numerator
d = 賤率.denominator#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1140, Actual: 210
Variable 'b' has wrong value. Expected: 3, Actual: 61
Variable 'c' has wrong value. Expected: 960, Actual: 61
Variable 'd' has wrong value. Expected: 4, Actual: 210"""
