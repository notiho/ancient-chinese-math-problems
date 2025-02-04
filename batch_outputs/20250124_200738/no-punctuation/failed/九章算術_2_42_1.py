"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤兩率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a石 兩 b錢 其 c鈞 兩 d錢 
"""

"""
This problem involves calculating the price per unit weight of silk, given a total amount of money and a total weight. The goal is to determine the price per shi (石) and per jun (鈞). Here's the solution encoded in Python:


"""

#----- content starts here -----

"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
Question: what are the rates (price per shi and price per jun)?

The procedure says: Place the amounts of shi, jun, jin, and liang as the divisor.
Multiply the total money by the respective rates to obtain the dividend.
Divide the dividend by the divisor to obtain the rate.
If there is a remainder less than the divisor, subtract it from the dividend.
The divisor corresponds to the cheaper rate, and the dividend corresponds to the more expensive rate.

Answer: the rate per shi is *a* qian, and the rate per jun is *b* qian.
"""

from fractions import Fraction

# Total money spent
錢數 = 13970

# Total weight in shi, jun, jin, liang, and zhu
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Conversion factors
斤每石 = 120  # 1 石 = 120 斤
兩每斤 = 16   # 1 斤 = 16 兩
銖每兩 = 24   # 1 兩 = 24 銖

# Convert total weight to a single unit (liang)
總兩 = (石 * 斤每石 * 兩每斤 + 鈞 * 兩每斤 * 兩每斤 + 斤 * 兩每斤 + 兩) + Fraction(銖, 銖每兩)

# Rate per shi
法石 = 石 * 斤每石 * 兩每斤  # Total liang in 1 shi
實石 = 錢數 * 法石
a = Fraction(實石, 總兩)

# Rate per jun
法鈞 = 鈞 * 兩每斤 * 兩每斤  # Total liang in 1 jun
實鈞 = 錢數 * 法鈞
b = Fraction(實鈞, 總兩)

# Output the results
print(f"Rate per shi: {a} qian")
print(f"Rate per jun: {b} qian")
#----- content ends here -----


"""
 

This code calculates the price per shi and per jun based on the given total weight and money spent. It uses fractions to ensure precision in the calculations.
"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 643737600/69197
Variable 'b' has wrong value. Expected: 4, Actual: 171663360/69197
Missing variable in output: 'c'
Missing variable in output: 'd'"""
