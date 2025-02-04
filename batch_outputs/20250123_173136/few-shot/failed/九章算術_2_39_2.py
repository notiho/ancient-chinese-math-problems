"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤石率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，石 b錢 。其 c石 ，石 d錢 。
"""

"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
It is desired to calculate the price per shi (stone) and per jun (unit of weight).
Question: what is the price per shi and per jun?

The procedure says: Place the amounts of shi, jun, jin, and liang as the divisor.
Multiply the total expenditure by the respective weights to obtain the dividend.
Divide the dividend by the divisor to calculate the price per unit.
If the divisor is not fully divisible, subtract the remainder from the divisor. The divisor represents the cheaper price, and the dividend represents the more expensive price.

Answer: the price per jun is *a* qian, and the remainder is *b* qian.
The price per shi is *c* qian, and the remainder is *d* qian.
"""

# 出錢一萬三千九百七十
出錢 = 13970

# 買絲一石二鈞二十八斤三兩五銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# 將所有重量轉換為銖 (1 石 = 120 鈞, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖)
總銖 = (石 * 120 * 30 * 16 * 24) + (鈞 * 30 * 16 * 24) + (斤 * 16 * 24) + (兩 * 24) + 銖

# 計算每銖的價格
每銖價格 = Fraction(出錢, 總銖)

# 計算每鈞的價格 (1 鈞 = 30 斤 = 30 * 16 * 24 銖)
每鈞銖數 = 30 * 16 * 24
每鈞價格 = 每銖價格 * 每鈞銖數

# 計算每石的價格 (1 石 = 120 鈞 = 120 * 30 * 16 * 24 銖)
每石銖數 = 120 * 30 * 16 * 24
每石價格 = 每銖價格 * 每石銖數

# 計算鈞價格的整數部分和餘數
a = 每鈞價格.numerator // 每鈞價格.denominator  # 整數部分
b = 每鈞價格.numerator % 每鈞價格.denominator  # 餘數

# 計算石價格的整數部分和餘數
c = 每石價格.numerator // 每石價格.denominator  # 整數部分
d = 每石價格.numerator % 每石價格.denominator  # 餘數
"""
Variable 'a' has wrong value. Expected: 979/960, Actual: 113
Variable 'b' has wrong value. Expected: 8051, Actual: 896003
Variable 'c' has wrong value. Expected: 68201/46080, Actual: 13635
Variable 'd' has wrong value. Expected: 8052, Actual: 1300185"""
