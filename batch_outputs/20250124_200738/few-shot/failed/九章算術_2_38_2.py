"""
今有出錢一千一百二十，買絲一石二鈞十八斤。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，斤 b錢 。其 c石 ，斤 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight (jin) for silk based on the total cost and the weight purchased. Here's the step-by-step translation of the procedure into Python code:


"""

#----- content starts here -----

"""
Suppose there is an expenditure of 1120 qian to buy 1 shi, 2 jun, and 18 jin of silk.
It is desired to determine the price per jin for each unit of weight (shi, jun, jin).
Question: what is the price per jin for each?

The procedure says: Place the number of shi, jun, jin, and liang as the divisor.
Multiply the total money by the respective rates to obtain the dividend.
Divide the dividend by the divisor to obtain the price per jin.
If the dividend is less than the divisor, subtract the dividend from the divisor.
The divisor represents the cheaper rate, and the dividend represents the more expensive rate.

Answer: the price per jin for 1 jun is *a* qian, *b* qian per jin.
The price per jin for 1 shi is *c* qian, *d* qian per jin.
"""

from fractions import Fraction

# 出錢一千一百二十
錢數 = 1120

# 買絲一石二鈞十八斤
石 = 1
鈞 = 2
斤 = 18

# 1 石 = 4 鈞, 1 鈞 = 30 斤
總斤數 = 石 * 4 * 30 + 鈞 * 30 + 斤

# 各置所買石、鈞、斤以為法
石法 = 石 * 4 * 30  # 1 石 = 4 鈞 = 120 斤
鈞法 = 鈞 * 30      # 1 鈞 = 30 斤
斤法 = 斤            # 斤 remains as is

# 以所率乘錢數為實
石實 = 錢數 * 石法
鈞實 = 錢數 * 鈞法
斤實 = 錢數 * 斤法

# 實如法而一
石價 = Fraction(石實, 總斤數)
鈞價 = Fraction(鈞實, 總斤數)
斤價 = Fraction(錢數, 總斤數)

# Results
a = 鈞價  # Price per jin for 1 jun
b = 斤價  # Price per jin
c = 石價  # Price per jin for 1 shi
d = 斤價  # Price per jin
#----- content ends here -----


"""
 

This code calculates the price per jin for each unit of weight (shi, jun, and jin) based on the total cost and the total weight purchased.
"""


"""
Variable 'a' has wrong value. Expected: 34/15, Actual: 11200/33
Variable 'b' has wrong value. Expected: 5, Actual: 560/99
Variable 'c' has wrong value. Expected: 13/12, Actual: 22400/33
Variable 'd' has wrong value. Expected: 6, Actual: 560/99"""
