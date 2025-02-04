"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a(=12893/9216)石 ，兩 b(=4)錢 。其 c(=3871/2880)鈞 ，兩 d(=5)錢 。
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,970 qian to purchase 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu of silk.
It is desired to calculate the price per unit for both shi and jun.

The procedure says: Place the quantities of shi, jun, jin, and liang as the divisor.
Multiply the total money by the respective rates to obtain the dividend.
Perform the division to calculate the price per unit.
If the dividend does not fully divide the divisor, subtract the remainder from the divisor.
The divisor corresponds to the cheaper rate, and the dividend corresponds to the more expensive rate.

Answer: The price per shi is *a*(=12893/9216) qian, with a remainder of *b*(=4) qian.
The price per jun is *c*(=3871/2880) qian, with a remainder of *d*(=5) qian.
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

# 將所有單位轉換為最小單位（銖），以便計算
# 1 石 = 1200 銖, 1 鈞 = 100 銖, 1 斤 = 16 銖, 1 兩 = 1 銖
總銖 = 石 * 1200 + 鈞 * 100 + 斤 * 16 + 兩 * 1 + 銖

# 計算每石的價格
石法 = 石 * 1200  # 每石的銖數
石實 = 錢數 * 石法  # 實數
石價 = Fraction(石實, 總銖)  # 每石的價格
a = 石價  # 每石的價格
b = 石價.numerator % 石價.denominator  # 餘數

# 計算每鈞的價格
鈞法 = 鈞 * 100  # 每鈞的銖數
鈞實 = 錢數 * 鈞法  # 實數
鈞價 = Fraction(鈞實, 總銖)  # 每鈞的價格
c = 鈞價  # 每鈞的價格
d = 鈞價.numerator % 鈞價.denominator  # 餘數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 523875/58
Variable 'b' has wrong value. Expected: 4, Actual: 19
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 174625/116
Variable 'd' has wrong value. Expected: 5, Actual: 45"""
