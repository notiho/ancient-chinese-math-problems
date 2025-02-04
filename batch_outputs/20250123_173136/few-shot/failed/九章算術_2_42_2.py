"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
It is desired to calculate the price per unit weight (shi and jun) for both the expensive and cheap rates.
Question: what are the rates for each?

The procedure says: Place the amounts of shi, jun, jin, and liang as the divisor.
Multiply the total money spent by the respective weights to obtain the dividend.
Divide the dividend by the divisor to obtain the rate per unit.
If the dividend is less than the divisor, subtract the dividend from the divisor to calculate the cheaper rate.

Answer: The expensive rate is *a* qian per shi, and *b* qian per liang. The cheaper rate is *c* qian per jun, and *d* qian per liang.
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

# 將所有重量轉換為最小單位（銖），1 石 = 1200 斤, 1 斤 = 16 兩, 1 兩 = 24 銖
總銖 = (石 * 1200 * 16 * 24) + (鈞 * 100 * 16 * 24) + (斤 * 16 * 24) + (兩 * 24) + 銖

# 其率術曰：各置所買石、鈞、斤、兩以為法
法 = 總銖

# 以所率乘錢數為實
實 = 錢數 * 法

# 實如法而一
貴率 = Fraction(實, 法)

# 不滿法者反以實減法，法賤實貴
賤率 = 法 - 貴率

# 將結果轉換回石、鈞、斤、兩的單位
a = 貴率
b = 賤率

c = 貴率
d =賤
"""
Code error: name '賤' is not defined"""
