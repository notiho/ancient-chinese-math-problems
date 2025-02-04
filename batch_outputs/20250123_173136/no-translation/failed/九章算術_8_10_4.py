"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese mathematical methods, specifically the "方程術" (method of solving simultaneous equations). Below is the Python code to solve the problem step by step:


"""


from fractions import Fraction

# Problem setup:
# Let 馬價 = x (price of a horse in 錢)
# Let 牛價 = y (price of a cow in 錢)

# Equations:
# 2x + y = 10000 + x/2  (from "二馬、一牛價過一萬，如半馬之價")
# x + 2y = 10000 - y/2  (from "一馬、二牛價不滿一萬，如半牛之價")

# Rewrite the equations to standard form:
# 4x + 2y = 20000  (multiply the first equation by 2 to eliminate the fraction)
# 2x + 5y = 20000  (multiply the second equation by 2 to eliminate the fraction)

# Coefficients for the equations:
# Equation 1: 4x + 2y = 20000
# Equation 2: 2x + 5y = 20000

# Step 1: Eliminate one variable using 方程術
# Multiply the first equation by 5 and the second equation by 2 to align coefficients of y:
# 20x + 10y = 100000  (first equation multiplied by 5)
# 4x + 10y = 40000    (second equation multiplied by 2)

# Subtract the second equation from the first:
# (20x + 10y) - (4x + 10y) = 100000 - 40000
# 16x = 60000
x = Fraction(60000, 16)  # Solve for x (price of a horse)
x = x.limit_denominator()  # Simplify the fraction if necessary

# Step 2: Substitute x into one of the original equations to solve for y
# Use the first equation: 4x + 2y = 20000
# 2y = 20000 - 4x
y = Fraction(20000 - 4 * x, 2)  # Solve for y (price of a cow)
y = y.limit_denominator()  # Simplify the fraction if necessary

# Results:
a = x  # 馬價 (price of a horse)
b = y  # 牛價 (price of a cow)

# Output the results
a, b


"""


### Explanation of the Code:
1. **Equations Setup**: The problem is translated into two linear equations based on the given conditions.
2. **Elimination Method**: The 方程術 (method of solving simultaneous equations) is used to eliminate one variable by aligning coefficients and subtracting equations.
3. **Substitution**: Once one variable is solved, it is substituted back into one of the original equations to solve for the other variable.
4. **Fraction Handling**: The `Fraction` class is used to ensure precise calculations and to represent the results as fractions if necessary.

### Final Answer:
- 馬價 \(a = x\) 錢
- 牛價 \(b = y\) 錢
"""


"""
Variable 'a' has wrong value. Expected: 60000/11, Actual: 3750
Variable 'b' has wrong value. Expected: 20000/11, Actual: 2500"""
