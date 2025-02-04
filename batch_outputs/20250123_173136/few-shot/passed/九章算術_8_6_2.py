"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

"""
This is a system of linear equations problem, where we need to solve for the price of one cow and one sheep. The procedure described corresponds to solving simultaneous linear equations using elimination or substitution. Let's translate this into Python code.

The equations are:
1. \( 5x + 2y = 10 \) (where \( x \) is the price of one cow and \( y \) is the price of one sheep)
2. \( 2x + 5y = 8 \)

We will solve this step by step according to the procedure.


"""


from fractions import Fraction

# 牛五、羊二，直金十兩
# Equation 1: 5x + 2y = 10
eq1_cows = 5  # Coefficient of x (cows) in equation 1
eq1_sheep = 2  # Coefficient of y (sheep) in equation 1
eq1_total = 10  # Total value in equation 1

# 牛二、羊五，直金八兩
# Equation 2: 2x + 5y = 8
eq2_cows = 2  # Coefficient of x (cows) in equation 2
eq2_sheep = 5  # Coefficient of y (sheep) in equation 2
eq2_total = 8  # Total value in equation 2

# Step 1: Eliminate one variable (e.g., y) by making the coefficients of y in both equations equal
# Multiply equation 1 by 5 (coefficient of y in equation 2)
# Multiply equation 2 by 2 (coefficient of y in equation 1)
eq1_cows_scaled = eq1_cows * 5
eq1_sheep_scaled = eq1_sheep * 5
eq1_total_scaled = eq1_total * 5

eq2_cows_scaled = eq2_cows * 2
eq2_sheep_scaled = eq2_sheep * 2
eq2_total_scaled = eq2_total * 2

# Subtract the scaled equations to eliminate y
# (25x + 10y = 50) - (4x + 10y = 16)
eliminated_cows = eq1_cows_scaled - eq2_cows_scaled
eliminated_total = eq1_total_scaled - eq2_total_scaled

# Step 2: Solve for x (price of one cow)
# eliminated_cows * x = eliminated_total
a = Fraction(eliminated_total, eliminated_cows)

# Step 3: Substitute x back into one of the original equations to solve for y (price of one sheep)
# Using equation 1: 5x + 2y = 10
remaining_total = eq1_total - (eq1_cows * a)
b = Fraction(remaining_total, eq1_sheep)

# Final answer
print(f"牛一，直金 {a} 兩，羊一，直金 {b} 兩。")


"""


### Explanation of the Code:
1. The coefficients of \( x \) (cows) and \( y \) (sheep) are extracted from the two equations.
2. The equations are scaled to make the coefficients of \( y \) equal, allowing elimination of \( y \).
3. After elimination, the resulting equation is solved for \( x \) (price of one cow).
4. The value of \( x \) is substituted back into one of the original equations to solve for \( y \) (price of one sheep).
5. The final result is printed as the price of one cow and one sheep.

### Answer:
The price of one cow is \( a \) taels, and the price of one sheep is \( b \) taels.
"""


"""
"""
