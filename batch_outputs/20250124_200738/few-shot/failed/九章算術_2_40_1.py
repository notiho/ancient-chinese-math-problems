"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight (jin and jun) based on the total cost and the total weight of silk purchased. Here's the step-by-step breakdown and Python implementation:


"""

#----- content starts here -----

"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
It is desired to calculate the price per jun and per jin.

The procedure says: Place the quantities of shi, jun, jin, and liang as the divisor.
Multiply the total money by the respective rates to obtain the dividend.
Divide the dividend by the divisor to calculate the price per unit.
If the divisor is not fully divisible, subtract the remainder from the divisor, indicating a cheaper rate for the divisor and a more expensive rate for the dividend.

Answer: The price per jin is *a* qian, and the price per jun is *b* qian.
The price per shi is *c* qian, and the price per jun is *d* qian.
"""

from fractions import Fraction

# Total money spent
錢數 = 13970

# Total weight of silk purchased
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Convert all weights to jin (1 shi = 120 jin, 1 jun = 30 jin, 1 liang = 1/16 jin, 1 zhu = 1/384 jin)
總斤 = 石 * 120 + 鈞 * 30 + 斤 + Fraction(兩, 16) + Fraction(銖, 384)

# Calculate the price per jin
a = Fraction(錢數, 總斤)

# Calculate the price per jun (1 jun = 30 jin)
b = a * 30

# Calculate the price per shi (1 shi = 120 jin)
c = a * 120

# The price per jun (already calculated as b)
d = b

# Outputs
print(f"Price per jin: {a} qian")
print(f"Price per jun: {b} qian")
print(f"Price per shi: {c} qian")
print(f"Price per jun (again): {d} qian")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Weight Conversion**: The total weight is converted into jin using the relationships:
   - 1 shi = 120 jin
   - 1 jun = 30 jin
   - 1 liang = 1/16 jin
   - 1 zhu = 1/384 jin

2. **Price per Unit**:
   - The price per jin is calculated by dividing the total money by the total weight in jin.
   - The price per jun is then derived by multiplying the price per jin by 30 (since 1 jun = 30 jin).
   - Similarly, the price per shi is derived by multiplying the price per jin by 120 (since 1 shi = 120 jin).

3. **Output**:
   - The results are displayed for the price per jin, per jun, and per shi.

This implementation adheres to the procedure described in the problem.
"""


"""
Variable 'a' has wrong value. Expected: 979/128, Actual: 5364480/79949
Variable 'b' has wrong value. Expected: 2012, Actual: 160934400/79949
Variable 'c' has wrong value. Expected: 19253/11520, Actual: 643737600/79949
Variable 'd' has wrong value. Expected: 2013, Actual: 160934400/79949"""
