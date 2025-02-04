"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤兩率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a石 兩 b錢 其 c鈞 兩 d錢 
"""

#----- content starts here -----
This problem involves calculating the price per unit weight (both per *shi* and per *jun*) for a given amount of silk purchased with a specific amount of money. Let's translate the procedure into Python code:

"""
Suppose there is an expenditure of 13,970 qian to purchase 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu of silk.
Question: What are the rates (price per shi and price per jun)?

The procedure says: Place the quantities of shi, jun, jin, and liang as the divisor.
Multiply the total money by the respective rates to get the dividend.
Divide the dividend by the divisor to get the rate.
If there is a remainder, subtract the remainder from the divisor.
The divisor gives the cheaper rate, and the dividend gives the more expensive rate.

Answer: The price per shi is *a* qian, and the price per jun is *b* qian.
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
石銖 = 120 * 30 * 16 * 24  # 1 石的銖數
a = Fraction(錢數 * 石銖, 総銖)

# 計算每鈞的價格
鈞銖 = 30 * 16 * 24  # 1 鈞的銖數
b = Fraction(錢數 * 鈞銖, 總銖)

a石_兩b錢 = a
c鈞_兩d錢 = b#----- content ends here -----

"""
Code error: unterminated string literal (detected at line 2) (<string>, line 2)"""
