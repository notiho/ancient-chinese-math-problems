"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤鈞率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a斤 鈞 b錢 其 c石 鈞 d錢 
"""

#----- content starts here -----
To solve this problem, we need to calculate the unit price (rate) of silk per *jin* and per *shi*. Here's the breakdown of the procedure:

"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
Question: What is the price per jun and per shi?

The procedure says: Place the weights of shi, jun, jin, liang, etc., as the divisor.
Multiply the total money by the respective rates to obtain the dividend.
Divide the dividend by the divisor to obtain the unit price.
If there is a remainder less than the divisor, subtract it from the dividend.
The divisor gives the cheaper rate, and the dividend gives the more expensive rate.

Answer: The price per *jin* is *a* qian, and the price per *shi* is *b* qian.
"""

# 出錢一萬三千九百七十
錢數 = 13970

# 買絲一石二鈞二十八斤三兩五銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# 將所有重量轉換為銖 (1 石 = 1200 斤, 1 鈞 = 100 斤, 1 斤 = 16 兩, 1 兩 = 24 銖)
總銖 = (石 * 1200 * 16 * 24) + (鈞 * 100 * 16 * 24) + (斤 * 16 * 24) + (兩 * 24) + 銖

# 每銖的價格
每銖價格 = Fraction(錢數, 總銖)

# 計算每斤的價格 (1 斤 = 16 兩 = 384 銖)
每斤價格 = 每銖價格 * 384

# 計算每石的價格 (1 石 = 1200 斤 = 460800 銖)
每石價格 = 每銖價格 * 460800

# 將結果分別賦值給 a 和 b
a = 每斤價格
b = 每石價格#----- content ends here -----

"""
Code error: unterminated string literal (detected at line 2) (<string>, line 2)"""
