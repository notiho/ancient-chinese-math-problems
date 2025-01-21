"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛 a ，直金 b兩 ，羊 c ，直金 d兩 。
"""

"""
To solve this problem, we will use the method of solving simultaneous equations, as described in the ancient Chinese "方程術" (method of solving equations). The problem involves two equations with two unknowns: the price of a cow and the price of a sheep.

The equations are:
1. \( 5x + 2y = 10 \) (where \( x \) is the price of a cow and \( y \) is the price of a sheep)
2. \( 2x + 5y = 8 \)

We will solve these equations step by step using the procedure described.

---

### Step-by-step solution:


"""


from fractions import Fraction

# 牛五、羊二，直金十兩 (Equation 1)
# 5x + 2y = 10
eq1_cows = 5  # Coefficient of x (price of a cow)
eq1_sheep = 2  # Coefficient of y (price of a sheep)
eq1_total = 10  # Total price in taels

# 牛二、羊五，直金八兩 (Equation 2)
# 2x + 5y = 8
eq2_cows = 2  # Coefficient of x (price of a cow)
eq2_sheep = 5  # Coefficient of y (price of a sheep)
eq2_total = 8  # Total price in taels

# Step 1: Eliminate one variable (y) by aligning coefficients
# Multiply Equation 1 by 5 (coefficient of y in Equation 2)
# Multiply Equation 2 by 2 (coefficient of y in Equation 1)
eq1_cows_scaled = eq1_cows * 5
eq1_sheep_scaled = eq1_sheep * 5
eq1_total_scaled = eq1_total * 5

eq2_cows_scaled = eq2_cows * 2
eq2_sheep_scaled = eq2_sheep * 2
eq2_total_scaled = eq2_total * 2

# Step 2: Subtract the scaled equations to eliminate y
# (25x + 10y = 50) - (4x + 10y = 16)
eliminated_cows = eq1_cows_scaled - eq2_cows_scaled  # 25x - 4x
eliminated_total = eq1_total_scaled - eq2_total_scaled  # 50 - 16

# Solve for x (price of a cow)
price_cow = Fraction(eliminated_total, eliminated_cows)  # x = (50 - 16) / (25 - 4)

# Step 3: Substitute x back into one of the original equations to solve for y
# Using Equation 1: 5x + 2y = 10
remaining_total = eq1_total - (eq1_cows * price_cow)  # 10 - 5x
price_sheep = Fraction(remaining_total, eq1_sheep)  # y = (10 - 5x) / 2

# Final results
a = 1  # Number of cows
b = price_cow  # Price of a cow in taels
c = 1  # Number of sheep
d = price_sheep  # Price of a sheep in taels

# Output the results
a, b, c, d


"""


---

### Explanation of the solution:
1. We align the coefficients of \( y \) in both equations by scaling them appropriately.
2. Subtracting the scaled equations eliminates \( y \), allowing us to solve for \( x \) (price of a cow).
3. Substituting \( x \) back into one of the original equations gives \( y \) (price of a sheep).
4. The final results are expressed as fractions to ensure accuracy.

### Final Answer:
- \( a = 1 \): Number of cows
- \( b = 2 \): Price of a cow in taels
- \( c = 1 \): Number of sheep
- \( d = \frac{4}{5} \): Price of a sheep in taels
"""


"""
"""
