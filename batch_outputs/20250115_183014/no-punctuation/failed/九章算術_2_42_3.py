"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤兩率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a石 兩 b錢 其 c鈞 兩 d錢 
"""

"""
This problem involves calculating the price per unit weight (in terms of *shi* and *jun*) for a given amount of money and silk. The procedure is as follows:

"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
Question: what are the rates of price per shi and per jun?

The procedure says: Place the weights (shi, jun, jin, liang) as the divisor.
Multiply the total money by the respective weights to obtain the dividend.
Divide the dividend by the divisor to obtain the rate.
If there is a remainder, subtract it from the divisor.
The divisor gives the cheaper rate, and the dividend gives the more expensive rate.

Answer: The rate per *shi* is *a* qian, and the rate per *jun* is *b* qian.
"""


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

# 將所有重量轉換為銖（最小單位）
# 1 石 = 1200 斤, 1 鈞 = 100 斤, 1 斤 = 16 兩, 1 兩 = 24 銖
總銖 = 石 * 1200 * 16 * 24 + 鈞 * 100 * 16 * 24 + 斤 * 16 * 24 + 兩 * 24 + 銖

# 計算每石的價格
# 以所率乘錢數為實
石銖 = 石 * 1200 * 16 * 24
石實 = 錢數 * 石銖

# 實如法而一
a = Fraction(石實, 總銖)

# 計算每鈞的價格
# 以所率乘錢數為實
鈞銖 = 鈞 * 100 * 16 * 24
鈞實 = 錢數 * 鈞銖

# 實如法而一
b = Fraction(鈞實, 總銖)

# 答案
print(f"其 {a} 石 兩 {b} 錢")


"""

"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 6437376000/548429
Variable 'b' has wrong value. Expected: 4, Actual: 1072896000/548429
Missing variable in output: 'c'
Missing variable in output: 'd'"""
