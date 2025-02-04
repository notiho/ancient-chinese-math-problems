"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
This problem involves calculating the price per unit weight (jin and jun) for silk based on the total cost and weight. Here's the solution translated into Python code:


"""

#----- content starts here -----

"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
It is desired to calculate the price per jun and per jin. What are they?

The procedure says: Place the quantities of shi, jun, jin, and liang as the divisor.
Multiply the total money by the respective rates to get the dividend.
Divide the dividend by the divisor to get the result.
If the divisor is not a whole number, subtract the remainder from the divisor. The divisor becomes cheaper, and the dividend becomes more expensive.

Answer: The price per jin is *a* qian, and the price per jun is *b* qian.
The price per shi is *c* qian, and the price per jun is *d* qian.
"""

from fractions import Fraction

# Total money spent
錢數 = 13970

# Weight of silk purchased
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Conversion factors
鈞_to_斤 = 30  # 1 鈞 = 30 斤
石_to_鈞 = 4   # 1 石 = 4 鈞
斤_to_兩 = 16  # 1 斤 = 16 兩
兩_to_銖 = 24  # 1 兩 = 24 銖

# Convert all weights to jin (斤)
總斤 = (石 * 石_to_鈞 * 鈞_to_斤) + (鈞 * 鈞_to_斤) + 斤 + (兩 / 斤_to_兩) + (銖 / (斤_to_兩 * 兩_to_銖))

# Calculate price per jin
a = Fraction(錢數, 總斤)

# Convert all weights to jun (鈞)
總鈞 = (石 * 石_to_鈞) + 鈞 + (斤 / 鈞_to_斤) + (兩 / (鈞_to_斤 * 斤_to_兩)) + (銖 / (鈞_to_斤 * 斤_to_兩 * 兩_to_銖))

# Calculate price per jun
b = Fraction(錢數, 総鈞)

# Calculate price per shi (石)
c = Fraction(錢數, 石)

# Calculate price per jun (鈞) again for clarity
d = b

# Output results
a_斤 = a
b_鈞 = b
c_石 = c
d_鈞 = d
#----- content ends here -----


"""


### Explanation:
1. **Conversion of weights**: The weights are converted into a single unit (jin or jun) using the given conversion factors.
2. **Price per unit**: The total money is divided by the total weight in the respective unit to calculate the price per jin, jun, or shi.
3. **Fractions**: The `Fraction` class is used to ensure exact calculations without rounding errors.

### Final Answer:
- The price per jin is `a` qian.
- The price per jun is `b` qian.
- The price per shi is `c` qian.
- The price per jun is `d` qian.
"""


"""
Code error: both arguments should be Rational instances"""
