"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤石率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a鈞 石 b錢 其 c石 石 d錢 
"""

"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
It is desired to calculate the price per shi and the price per unit weight.

The procedure says: Place the weights of shi, jun, jin, and liang as the divisor.
Multiply the total expenditure by the respective rates to obtain the dividend.
Divide the dividend by the divisor to calculate the price per unit.
If the remainder is less than the divisor, subtract the remainder from the divisor to adjust the calculation.
The divisor corresponds to the cheaper rate, and the dividend corresponds to the more expensive rate.

Answer: The price per jun is *a* qian and *b* fen. The price per shi is *c* qian and *d* fen.
"""

# 出錢 13,970
錢數 = 13970

# 買絲重量：1 石, 2 鈞, 28 斤, 3 兩, 5 銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# 將重量轉換為銖 (1 石 = 120 鈞, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖)
總銖 = (石 * 120 * 30 * 16 * 24) + (鈞 * 30 * 16 * 24) + (斤 * 16 * 24) + (兩 * 24) + 銖

# 計算每石的價格
石法 = 120 * 30 * 16 * 24  # 1 石的銖數
石實 = 錢數 * 石法
石價格 = Fraction(石實, 總銖)

# 計算每鈞的價格
鈞法 = 30 * 16 * 24  # 1 鈞的銖數
鈞實 = 錢數 * 鈞法
鈞價格 = Fraction(鈞實, 總銖)

# 將價格轉換為整數部分和餘數
a = 鈞價格.numerator // 鈞價格.denominator  # 每鈞的整數部分
b = 鈞價格.numerator % 鈞價格.denominator  # 每鈞的餘數

c = 石價格.numerator // 石價格.denominator  # 每石的整數部分
d = 石價格.numerator % 石價格.denominator  # 每石的餘數
"""
Variable 'a' has wrong value. Expected: 979/960, Actual: 113
Variable 'b' has wrong value. Expected: 8051, Actual: 896003
Variable 'c' has wrong value. Expected: 68201/46080, Actual: 13635
Variable 'd' has wrong value. Expected: 8052, Actual: 1300185"""
