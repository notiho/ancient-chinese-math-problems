"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤兩率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a石 兩 b錢 其 c鈞 兩 d錢 
"""

#----- content starts here -----
This problem involves calculating the price per unit weight (e.g., per shi and per jun) when buying silk. Let's break it down step by step and encode it into Python.

"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
Question: What are the rates (price per shi and price per jun)?

The procedure says: Place the weights (shi, jun, jin, liang) as the divisor.
Multiply the total money by the respective rates to obtain the dividend.
Divide the dividend by the divisor to get the rate.
If the dividend is less than the divisor, subtract the dividend from the divisor.
The divisor gives the cheaper rate, and the dividend gives the more expensive rate.

The answer says: The rate per shi is *a* qian, and the rate per jun is *b* qian.
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

# 將所有重量轉換為銖 (1 石 = 120 鈞, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖)
總銖 = (
    石 * 120 * 30 * 16 * 24
    + 鈞 * 30 * 16 * 24
    + 斤 * 16 * 24
    + 兩 * 24
    + 銖
)

# 計算每石的價格
石法 = 石 * 120 * 30 * 16 * 24  # 每石的銖數
石實 = 錢數 * 石法  # 實 = 錢數 * 石法
a = Fraction(石實, 總銖)  # 每石的價格

# 計算每鈞的價格
鈞法 = 鈞 * 30 * 16 * 24  # 每鈞的銖數
鈞實 = 錢數 * 鈞法  # 實 = 錢數 * 鈞法
b = Fraction(鈞實, 總銖)  # 每鈞的價格

a, b#----- content ends here -----

"""
Code error: unterminated string literal (detected at line 2) (<string>, line 2)"""
