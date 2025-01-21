"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a(=12893/9216)石 ，兩 b(=4)錢 。其 c(=3871/2880)鈞 ，兩 d(=5)錢 。
"""

"""
Suppose there is an expenditure of 13,970 qian to purchase silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
It is desired to calculate the price per unit weight for both shi and jun.
Question: what are the rates for each?

The procedure says: Place the quantities of shi, jun, jin, and liang as the divisor.
Multiply the total money by the respective rate to obtain the dividend.
Divide the dividend by the divisor to obtain the rate.
If the dividend does not fully divide the divisor, subtract the remainder from the divisor.
The divisor corresponds to the cheaper rate, and the dividend corresponds to the more expensive rate.

Answer: The rate per shi is *a*(=12893/9216) qian, with a remainder of *b*(=4) qian.
The rate per jun is *c*(=3871/2880) qian, with a remainder of *d*(=5) qian.
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

# 將所有單位轉換為銖 (1 石 = 120 鈞, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖)
總銖 = (石 * 120 * 30 * 16 * 24) + (鈞 * 30 * 16 * 24) + (斤 * 16 * 24) + (兩 * 24) + 銖

# 計算每石的價格
石銖 = 120 * 30 * 16 * 24  # 1 石的銖數
石實 = 錢數 * 石銖  # 實 = 錢數 * 石的銖數
石率 = Fraction(石實, 總銖)  # 每石的價格
石餘 = 石率.denominator - 石率.numerator % 石率.denominator  # 餘數

# 計算每鈞的價格
鈞銖 = 30 * 16 * 24  # 1 鈞的銖數
鈞實 = 錢數 * 鈞銖  # 實 = 錢數 * 鈞的銖數
鈞率 = Fraction(鈞實, 總銖)  # 每鈞的價格
鈞餘 = 鈞率.denominator - 鈞率.numerator % 鈞率.denominator  # 餘數

# 答案
a = 石率  # 每石的價格
b = 石餘  # 每石的餘數
c = 鈞率  # 每鈞的價格
d = 鈞餘  # 每鈞的餘數
"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 19312128000/1416269
Variable 'b' has wrong value. Expected: 4, Actual: 116084
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 160934400/1416269
Variable 'd' has wrong value. Expected: 5, Actual: 520266"""
