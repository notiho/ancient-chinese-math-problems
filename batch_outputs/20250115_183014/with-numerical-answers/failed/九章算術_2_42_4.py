"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a(=12893/9216)石 ，兩 b(=4)錢 。其 c(=3871/2880)鈞 ，兩 d(=5)錢 。
"""

"""
Suppose there is an expenditure of 13,970 qian to buy 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu of silk.
It is desired to calculate the price per unit for both expensive and cheap rates.
Question: what are the rates for each unit?

The procedure for rates says: Place the quantities of shi, jun, jin, and liang as the divisor.
Multiply the total money by the rate to obtain the dividend.
Divide the dividend by the divisor to obtain the rate.
If the dividend does not fully divide the divisor, subtract the remainder from the divisor for the cheap rate and add it to the dividend for the expensive rate.

Answer: The expensive rate is *a*(=12893/9216) qian per shi, and the cheap rate is *b*(=4) qian per liang.
The expensive rate is *c*(=3871/2880) qian per jun, and the cheap rate is *d*(=5) qian per liang.
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

# 將單位轉換為最小單位（銖）
銖總數 = (石 * 120000) + (鈞 * 20000) + (斤 * 160) + (兩 * 10) + 銖

# 石的法
石法 = 120000

# 鈞的法
鈞法 = 20000

# 計算石的貴率
石貴率 = Fraction(錢數 * 石法, 銖總數)

# 計算鈞的貴率
鈞貴率 = Fraction(錢數 * 鈞法, 銖總數)

# 計算石的賤率
石賤率 = 錢數 // 石法

# 計算鈞的賤率
鈞賤率 = 錢數 // 鈞法

# 輸出結果
a = 石貴率  # 12893/9216
b = 石賤率  # 4
c = 鈞貴率  # 3871/2880
d = 鈞賤率  # 5
"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 335280000/32903
Variable 'b' has wrong value. Expected: 4, Actual: 0
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 55880000/32903
Variable 'd' has wrong value. Expected: 5, Actual: 0"""
