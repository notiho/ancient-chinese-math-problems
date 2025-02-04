"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

"""
This problem involves solving a system of linear equations, which is described in the ancient Chinese mathematical text as "方程術" (method of solving simultaneous equations). The problem can be expressed as:

1. \( 5x + 2y = 10 \) (five cows and two sheep cost 10 liang of gold)
2. \( 2x + 5y = 8 \) (two cows and five sheep cost 8 liang of gold)

Here, \( x \) represents the price of one cow in liang, and \( y \) represents the price of one sheep in liang. The solution will follow the described procedure.

---

### 方程術 (Method of Solving Simultaneous Equations)

1. Place the coefficients of the equations in rows (as described in the text).
2. Use elimination to reduce the system step by step.
3. Solve for the unknowns.

---


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# Equation 1: 5x + 2y = 10
# Equation 2: 2x + 5y = 8

# 上禾 (first row coefficients)
上禾_x = 5
上禾_y = 2
上禾_常數 = 10

# 中禾 (second row coefficients)
中禾_x = 2
中禾_y = 5
中禾_常數 = 8

# Step 1: Eliminate x from the second equation
# Multiply the first row by 中禾_x and the second row by 上禾_x
上禾_x_倍 = 中禾_x
中禾_x_倍 = 上禾_x

# Update the rows
上禾_y_新 = 上禾_y * 上禾_x_倍
上禾_常數_新 = 上禾_常數 * 上禾_x_倍

中禾_y_新 = 中禾_y * 中禾_x_倍
中禾_常數_新 = 中禾_常數 * 中禾_x_倍

# Subtract the updated rows to eliminate x
下禾_y = 中禾_y_新 - 上禾_y_新
下禾_常數 = 中禾_常數_新 - 上禾_常數_新

# Step 2: Solve for y
y = Fraction(下禾_常數, 下禾_y)

# Step 3: Solve for x using the first equation
x = Fraction(上禾_常數 - 上禾_y * y, 上禾_x)

# Results
a = x  # Price of one cow in liang
b = y  # Price of one sheep in liang

# Output
a, b
#----- content ends here -----


"""


### Explanation of the Code

1. **Coefficients Setup**:
   - The coefficients of the two equations are set up as variables.
   - \( 5x + 2y = 10 \) is the first equation (上禾).
   - \( 2x + 5y = 8 \) is the second equation (中禾).

2. **Elimination**:
   - The first equation is multiplied by the coefficient of \( x \) in the second equation, and the second equation is multiplied by the coefficient of \( x \) in the first equation.
   - Subtracting these scaled equations eliminates \( x \), leaving an equation in terms of \( y \).

3. **Solve for \( y \)**:
   - The resulting equation is solved for \( y \) by dividing the constant term by the coefficient of \( y \).

4. **Solve for \( x \)**:
   - Substituting \( y \) back into the first equation allows solving for \( x \).

5. **Output**:
   - The values of \( x \) (price of one cow) and \( y \) (price of one sheep) are stored in variables \( a \) and \( b \), respectively.

---

### Answer:
The price of one cow is \( a \) liang, and the price of one sheep is \( b \) liang.
"""


"""
"""
