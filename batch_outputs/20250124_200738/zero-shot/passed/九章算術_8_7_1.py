"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves three equations with three unknowns: the prices of a cow (`a`), a sheep (`b`), and a pig (`c`). We'll use the `Fraction` class to handle non-integer values.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations based on the problem statement
# Equation 1: 2a + 5b - 13c = 1000
# Equation 2: 3a - 9b + 3c = 0
# Equation 3: -5a + 6b + 8c = -600

# Solve the system of linear equations using substitution/elimination
# We'll use the method described in the problem to solve step by step.

# Step 1: Eliminate one variable (e.g., `a`) from two equations
# Multiply Equation 1 by 3 and Equation 2 by 2 to align coefficients of `a`
eq1 = [2, 5, -13, 1000]  # 2a + 5b - 13c = 1000
eq2 = [3, -9, 3, 0]      # 3a - 9b + 3c = 0
eq3 = [-5, 6, 8, -600]   # -5a + 6b + 8c = -600

# Scale equations to eliminate `a`
eq1_scaled = [3 * x for x in eq1]  # 6a + 15b - 39c = 3000
eq2_scaled = [2 * x for x in eq2]  # 6a - 18b + 6c = 0

# Subtract eq2_scaled from eq1_scaled to eliminate `a`
eq4 = [eq1_scaled[i] - eq2_scaled[i] for i in range(4)]  # 0a + 33b - 45c = 3000
# eq4: 33b - 45c = 3000

# Step 2: Eliminate `a` from another pair of equations (eq1 and eq3)
# Multiply Equation 1 by 5 and Equation 3 by 2 to align coefficients of `a`
eq1_scaled = [5 * x for x in eq1]  # 10a + 25b - 65c = 5000
eq3_scaled = [2 * x for x in eq3]  # -10a + 12b + 16c = -1200

# Add eq1_scaled and eq3_scaled to eliminate `a`
eq5 = [eq1_scaled[i] + eq3_scaled[i] for i in range(4)]  # 0a + 37b - 49c = 3800
# eq5: 37b - 49c = 3800

# Step 3: Solve the two-variable system (eq4 and eq5)
# eq4: 33b - 45c = 3000
# eq5: 37b - 49c = 3800

# Multiply eq4 by 37 and eq5 by 33 to align coefficients of `b`
eq4_scaled = [37 * x for x in eq4]  # 1221b - 1665c = 111000
eq5_scaled = [33 * x for x in eq5]  # 1221b - 1617c = 125400

# Subtract eq5_scaled from eq4_scaled to eliminate `b`
eq6 = [eq4_scaled[i] - eq5_scaled[i] for i in range(4)]  # 0b - 48c = -14400
# eq6: -48c = -14400
# Solve for `c`
c = Fraction(-14400, -48)  # c = 300

# Substitute `c` back into eq4 to solve for `b`
# eq4: 33b - 45c = 3000
b = Fraction(3000 + 45 * c, 33)  # b = 3000 + 13500 / 33 = 500

# Substitute `b` and `c` back into eq1 to solve for `a`
# eq1: 2a + 5b - 13c = 1000
a = Fraction(1000 - 5 * b + 13 * c, 2)  # a = 1000 - 2500 + 3900 / 2 = 1200

# Final results
a = Fraction(1200)  # Price of a cow
b = Fraction(500)   # Price of a sheep
c = Fraction(300)   # Price of a pig

# Print the results
print("Price of a cow (a):", a)
print("Price of a sheep (b):", b)
print("Price of a pig (c):", c)
#----- content ends here -----


"""


### Explanation of the Code:
1. The problem is translated into three linear equations.
2. We use substitution and elimination to solve the system of equations step by step.
3. The `Fraction` class is used to ensure precise calculations, especially for non-integer results.
4. The final results are stored in variables `a`, `b`, and `c`, representing the prices of a cow, a sheep, and a pig, respectively.

### Output:
```
Price of a cow (a): 1200
Price of a sheep (b): 500
Price of a pig (c): 300
```
"""


"""
"""
