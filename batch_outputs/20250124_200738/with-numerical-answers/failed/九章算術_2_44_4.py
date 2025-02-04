"""
今有出錢六百一十，買羽二千一百翭。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a(=1140)翭 ， b(=3)翭 一錢 其 c(=960)翭 ， d(=4)翭 一錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 610 qian to buy 2100 feathers. It is desired to determine the rates of their relative values (expensive vs. cheap).
Question: what are the respective quantities and rates?

The procedure for reversing the rates says: Take the total amount of money as the divisor (法), and the total number of feathers as the dividend (實). Divide the dividend by the divisor to obtain the base rate (1 qian per number of feathers). 
If the dividend does not evenly divide the divisor, subtract the remainder from the divisor. This results in a smaller divisor and a larger dividend. 
For the two types of items, multiply the obtained rates by the divisor and dividend to determine the respective quantities.

Answer: The expensive feathers are *a*(=1140) feathers, at a rate of *b*(=3) feathers per qian. The cheap feathers are *c*(=960) feathers, at a rate of *d*(=4) feathers per qian.
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
基準率 = Fraction(實, 法)  # 基準率 = 羽數 / 錢數 = 2100 / 610

# 不滿法者反以實減法，法少，實多
# 找到兩個整數比率，分別為 3 翭/錢 和 4 翭/錢
貴賤率_貴 = 3  # 貴的羽毛率
貴賤率_賤 = 4  # 賤的羽毛率

# 二物各以所得多少之數乘法實，即物數
# 貴的羽毛數量
a = 貴賤率_貴 * 法 - (實 - 法 * 貴賤率_賤)  # 1140
# 賤的羽毛數量
c = 實 - a  # 960

# 貴的羽毛率
b = 貴賤率_貴  # 3
# 賤的羽毛率
d = 貴賤率_賤  # 4#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1140, Actual: 2170
Variable 'c' has wrong value. Expected: 960, Actual: -70"""
