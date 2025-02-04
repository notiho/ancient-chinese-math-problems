"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，斤 b錢 。其 c斤 ，斤 d錢 。
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,970 qian to buy 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu of silk.
It is desired to calculate the price per jin (unit rate). 
Question: what is the price per jin for each unit of weight?

The procedure for the rate says: Place the quantities of shi, jun, jin, and liang as the divisor.
Multiply the total expenditure by the rate to obtain the dividend.
Divide the dividend by the divisor to obtain the unit price.
If the dividend does not fully divide the divisor, subtract the remainder from the divisor to adjust the calculation. 
A smaller divisor results in a higher rate, and a larger divisor results in a lower rate.

Answer: The price per *a* shi is *b* qian. The price per *c* jin is *d* qian.
"""

from fractions import Fraction

# 出錢一萬三千九百七十
錢數 = 13970

# 買絲一石二鈞二十八斤三兩五銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# 將所有單位轉換為斤
# 1 石 = 120 斤, 1 鈞 = 30 斤, 1 兩 = 1/16 斤, 1 銖 = 1/384 斤
總斤數 = 石 * 120 + 鈞 * 30 + 斤 + Fraction(兩, 16) + Fraction(銖, 384)

# 以所率乘錢數為實
實 = 錢數

# 實如法而一
斤率 = Fraction(實, 總斤數)

# 計算每石的價格
每石價格 = 斤率 * 120

# 計算每斤的價格
每斤價格 = 斤率

# 答案
a = 石
b = 每石價格
c = 1  # 每斤
d = 每斤價格#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 1
Variable 'b' has wrong value. Expected: 67, Actual: 643737600/79949
Variable 'c' has wrong value. Expected: 7897/384, Actual: 1
Variable 'd' has wrong value. Expected: 68, Actual: 5364480/79949"""
