"""
今有出錢六百一十，買羽二千一百翭。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a翭 ， b翭 一錢 其 c翭 ， d翭 一錢
"""

"""
Suppose there is an expenditure of 610 qian to purchase 2100 feathers. It is desired to determine the rates of their relative value (expensive and cheap feathers). 
Question: what are the rates of the expensive and cheap feathers?

The procedure for reversing the rates says: Take the total amount of money as the divisor (法), and the total number of feathers as the dividend (實). Divide the dividend by the divisor to obtain the rate (1 qian per number of feathers). 
If the dividend does not fully divide the divisor, reverse the calculation by subtracting the dividend from the divisor. The divisor decreases, and the dividend increases. 
For the two types of items (expensive and cheap feathers), multiply their respective quantities by the divisor and dividend to determine their rates.

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
貴率 = 基準率 + 1  # 貴羽率 (expensive feathers rate)
賤率 = 基準率 - 1  # 賤羽率 (cheap feathers rate)

# 二物各以所得多少之數乘法實，即物數
貴羽數 = Fraction(法, 貴率)
賤羽數 = Fraction(法, 賤率)

# Assign results
a = 貴羽數
b = 貴率
c = 賤羽數
d = 賤率
"""
Variable 'a' has wrong value. Expected: 1140, Actual: 37210/271
Variable 'b' has wrong value. Expected: 3, Actual: 271/61
Variable 'c' has wrong value. Expected: 960, Actual: 37210/149
Variable 'd' has wrong value. Expected: 4, Actual: 149/61"""
