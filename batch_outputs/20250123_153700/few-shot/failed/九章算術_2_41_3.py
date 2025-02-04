"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，斤 b錢 。其 c斤 ，斤 d錢 。
"""

"""
Suppose there is an expenditure of 13,970 qian to buy 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu of silk.
It is desired to calculate the price per jin (unit rate). 
Question: what is the price per jin for each unit of measurement?

The procedure for rates says: Place the quantities of shi, jun, jin, and liang as the divisor (法).
Multiply the total money (錢數) by the respective unit rate to obtain the dividend (實).
Divide the dividend by the divisor to obtain the unit price.
If the dividend is less than the divisor, subtract the dividend from the divisor. The divisor becomes cheaper, and the dividend becomes more expensive.

Answer: The price per shi is *a* qian per jin. The price per jin is *b* qian. The price per jin for individual jin is *c* qian, and the price per liang is *d* qian.
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

# 1 石 = 120 斤
石_to_斤 = 120
# 1 鈞 = 30 斤
鈞_to_斤 = 30
# 1 斤 = 16 兩
斤_to_兩 = 16
# 1 兩 = 24 銖
兩_to_銖 = 24

# Convert everything to 銖 for total weight
總銖 = (
    石 * 石_to_斤 * 斤_to_兩 * 兩_to_銖
    + 鈞 * 鈞_to_斤 * 斤_to_兩 * 兩_to_銖
    + 斤 * 斤_to_兩 * 兩_to_銖
    + 兩 * 兩_to_銖
    + 銖
)

# Convert 銖 back to 斤 for easier calculations
總斤 = Fraction(總銖, 斤_to_兩 * 兩_to_銖)

# Calculate price per 石
石_總斤 = 石 * 石_to_斤
a = Fraction(錢數, 石_總斤)

# Calculate price per 斤
b = Fraction(錢數, 總斤)

# Calculate price per individual 斤
c = b  # Same as above since it's already per 斤

# Calculate price per 兩
總兩 = 總斤 * 斤_to_兩
d = Fraction(錢數, 總兩)
"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 1397/12
Variable 'b' has wrong value. Expected: 67, Actual: 5364480/79949
Variable 'c' has wrong value. Expected: 7897/384, Actual: 5364480/79949
Variable 'd' has wrong value. Expected: 68, Actual: 335280/79949"""
