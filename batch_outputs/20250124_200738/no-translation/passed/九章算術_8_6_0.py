"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

"""
This problem is a classic system of linear equations, and the solution can be derived using the method described in the "方程術" (method of solving simultaneous equations). Here's how we can translate the procedure into Python code:


"""

#----- content starts here -----

from fractions import Fraction

# 牛五、羊二，直金十兩
牛1 = 5
羊1 = 2
金1 = 10

# 牛二、羊五，直金八兩
牛2 = 2
羊2 = 5
金2 = 8

# Step 1: Solve for 牛 and 羊 using elimination
# Multiply the first equation by 羊2 and the second equation by 羊1 to align the coefficients of 羊
eq1_multiplier = 羊2
eq2_multiplier = 羊1

牛1_new = 牛1 * eq1_multiplier
羊1_new = 羊1 * eq1_multiplier
金1_new = 金1 * eq1_multiplier

牛2_new = 牛2 * eq2_multiplier
羊2_new = 羊2 * eq2_multiplier
金2_new = 金2 * eq2_multiplier

# Subtract the second equation from the first to eliminate 羊
牛_diff = 牛1_new - 牛2_new
金_diff = 金1_new - 金2_new

# Solve for 牛 (price of one 牛)
牛_price = Fraction(金_diff, 牛_diff)

# Substitute 牛_price back into one of the original equations to solve for 羊
金_remaining = 金1 - 牛1 * 牛_price
羊_price = Fraction(金_remaining, 羊1)

# Results
a = 牛_price
b = 羊_price

# Output
print(f"牛一，直金 {a} 兩，羊一，直金 {b} 兩。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input the equations**: The problem gives two equations:
   - \( 5x + 2y = 10 \)
   - \( 2x + 5y = 8 \)
   Here, \( x \) is the price of one 牛 (牛_price), and \( y \) is the price of one 羊 (羊_price).

2. **Elimination method**: Multiply the equations to align the coefficients of \( y \) (羊), then subtract one equation from the other to eliminate \( y \) and solve for \( x \) (牛_price).

3. **Substitution**: Substitute \( x \) (牛_price) back into one of the original equations to solve for \( y \) (羊_price).

4. **Output the results**: The prices of 牛 and 羊 are expressed as fractions for precision.

### Final Answer:
- 牛一，直金 \( a \) 兩。
- 羊一，直金 \( b \) 兩。
"""


"""
"""
