"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤兩率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a石 兩 b錢 其 c鈞 兩 d錢 
"""

"""
This problem involves calculating the price per unit weight (in terms of *shi* and *jun*) for a given amount of silk purchased with a specific amount of money. Here's the solution encoded in Python:


"""

#----- content starts here -----

"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
Question: What are the rates of price per shi and per jun?

The procedure says: Place the weights (shi, jun, jin, liang) as the divisor.
Multiply the total money by the respective rates to obtain the dividend.
Divide the dividend by the divisor to get the result.
If the dividend does not fully divide the divisor, subtract the remainder from the divisor.
The divisor gives the cheaper rate, and the dividend gives the more expensive rate.

The answer says: the rate per shi is *a* qian, and the rate per jun is *b* qian.
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

# 將所有重量轉換為最小單位（銖）
# 1 石 = 120 鈞, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖
總銖 = (石 * 120 * 30 * 16 * 24) + (鈞 * 30 * 16 * 24) + (斤 * 16 * 24) + (兩 * 24) + 銖

# 計算每石的價格
# 各置所買石鈞斤兩以為法
法_石 = 石 * 120 * 30 * 16 * 24

# 以所率乘錢數為實
實_石 = 錢數 * 法_石

# 實如法而一
a = Fraction(錢數, 石)

# 計算每鈞的價格
法_鈞 = 鈞 * 30 * 16 * 24
實_鈞 = 錢數 * 法_鈞
b = Fraction(錢數, 鈞)

print(f"其 {a} 石 兩 {b} 錢")
#----- content ends here -----


"""
 

This code calculates the price per *shi* and *jun* based on the given weights and total cost. The results are expressed as fractions for precision.
"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 13970
Variable 'b' has wrong value. Expected: 4, Actual: 6985
Missing variable in output: 'c'
Missing variable in output: 'd'"""
