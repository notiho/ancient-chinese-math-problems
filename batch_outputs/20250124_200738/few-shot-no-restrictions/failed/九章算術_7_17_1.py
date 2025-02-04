"""
今有黃金九枚，白銀一十一枚，稱之重適等。交易其一，金輕十三兩。問︰金、銀一枚各重幾何？
術曰：假令黃金三斤，白銀二斤、一十一分斤之五，不足四十九，於右行。令之黃金二斤，白銀一斤、一十一分斤之七，多一十五於左行。以分母各乘其行內之數，以盈不足維乘所出率，并以為實。并盈不足為法。實如法，得黃金重。分母乘法以除，得銀重。約之得分也。
荅曰：金重 a斤 ，銀重 b斤 。
"""

"""
This is a classic problem involving proportional weights of gold and silver. The problem states that 9 pieces of gold and 11 pieces of silver weigh the same. When one piece of gold is exchanged for one piece of silver, the gold becomes lighter by 13 liang. We are tasked with finding the weight of one piece of gold and one piece of silver.

The procedure involves setting up a system of equations based on the given conditions and solving for the weights of gold and silver. Here's the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
gold_pieces = 9  # Number of gold pieces
silver_pieces = 11  # Number of silver pieces
gold_lighter_by = 13  # Gold becomes lighter by 13 liang when one piece is exchanged

# Let the weight of one piece of gold be x (in jin) and one piece of silver be y (in jin)
# Equation 1: Total weight of gold = Total weight of silver
# 9x = 11y

# Equation 2: After exchanging one piece of gold for one piece of silver
# 8x + y = 11y - 13

# Solve the system of equations
# From Equation 1: x = (11/9)y
x = Fraction(11, 9)  # Weight of one piece of gold in terms of y

# Substitute x into Equation 2
# 8(11/9)y + y = 11y - 13
# (88/9)y + y = 11y - 13
# (88/9)y + (9/9)y = 11y - 13
# (97/9)y = 11y - 13
# (97/9)y - (99/9)y = -13
# (-2/9)y = -13
# y = (-13) / (-2/9)
y = Fraction(13 * 9, 2)  # Weight of one piece of silver

# Calculate x using x = (11/9)y
x = Fraction(11, 9) * y  # Weight of one piece of gold

# Simplify the results
a = x  # Weight of one piece of gold
b = y  # Weight of one piece of silver

# Output the results
print(f"金重 {a} 斤 ，銀重 {b} 斤 。")
#----- content ends here -----


"""


### Explanation of the Solution:
1. **Equation 1**: Since 9 pieces of gold weigh the same as 11 pieces of silver, we have \( 9x = 11y \), where \( x \) is the weight of one piece of gold and \( y \) is the weight of one piece of silver.
2. **Equation 2**: After exchanging one piece of gold for one piece of silver, the gold becomes lighter by 13 liang. This gives us \( 8x + y = 11y - 13 \).
3. Solve the system of equations:
   - From Equation 1, express \( x \) in terms of \( y \): \( x = \frac{11}{9}y \).
   - Substitute \( x \) into Equation 2 to solve for \( y \).
   - Once \( y \) is found, substitute it back into \( x = \frac{11}{9}y \) to find \( x \).
4. The results are expressed as fractions for precision.

### Answer:
The weight of one piece of gold is \( a \) jin, and the weight of one piece of silver is \( b \) jin.
"""


"""
Variable 'a' has wrong value. Expected: 143/64, Actual: 143/2
Variable 'b' has wrong value. Expected: 117/64, Actual: 117/2"""
