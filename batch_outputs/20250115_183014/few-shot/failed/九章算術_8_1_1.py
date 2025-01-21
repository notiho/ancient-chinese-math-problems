"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
This problem involves solving a system of equations to determine the yield of one sheaf of upper and lower millet. The ancient Chinese method described here is a form of elimination, similar to Gaussian elimination in modern algebra. Below is the Python implementation of the solution:


"""


from fractions import Fraction

# Problem setup:
# 上禾 (upper millet) = x (yield per sheaf in dou)
# 下禾 (lower millet) = y (yield per sheaf in dou)

# Equation 1: 7x - 1 + 2y = 10
# Simplify: 7x + 2y = 11

# Equation 2: 8y + 1 + 2x = 10
# Simplify: 2x + 8y = 9

# Coefficients of the equations:
# 7x + 2y = 11
# 2x + 8y = 9

# Step 1: Eliminate one variable (e.g., x) using the elimination method.
# Multiply the first equation by 2 and the second equation by 7 to align coefficients of x:
# 14x + 4y = 22
# 14x + 56y = 63

# Subtract the first equation from the second:
# (14x + 56y) - (14x + 4y) = 63 - 22
# 52y = 41
y = Fraction(41, 52)  # Lower millet yield per sheaf

# Step 2: Solve for x using the first equation (7x + 2y = 11):
# 7x + 2(Fraction(41, 52)) = 11
# 7x = 11 - 2(Fraction(41, 52))
# 7x = Fraction(572, 52) - Fraction(82, 52)
# 7x = Fraction(490, 52)
x = Fraction(490, 52) / 7  # Upper millet yield per sheaf
x = Fraction(70, 52)

# Simplify the fractions:
x = x.limit_denominator()  # Upper millet yield per sheaf
y = y.limit_denominator()  # Lower millet yield per sheaf

# Results:
a = 7  # Number of upper millet sheaves
b = x   # Yield per upper millet sheaf in dou
c = 8  # Number of lower millet sheaves
d = y   # Yield per lower millet sheaf in dou

print(f"上禾 {a}秉 實 {b}斗 ，下禾 {c}秉 實 {d}斗 。")


"""


### Explanation of the Code:
1. **Equations Setup**: The problem is translated into two linear equations:
   - \( 7x + 2y = 11 \)
   - \( 2x + 8y = 9 \)
   Here, \( x \) is the yield per sheaf of upper millet, and \( y \) is the yield per sheaf of lower millet.

2. **Elimination Method**: The equations are manipulated to eliminate one variable (in this case, \( x \)) by aligning the coefficients of \( x \) and subtracting the equations.

3. **Solve for \( y \)**: After eliminating \( x \), the value of \( y \) (lower millet yield per sheaf) is calculated.

4. **Solve for \( x \)**: The value of \( x \) (upper millet yield per sheaf) is calculated by substituting \( y \) back into one of the original equations.

5. **Simplify Fractions**: The results are expressed as fractions using the `Fraction` class to ensure precision.

6. **Output**: The results are printed in the required format.

### Final Answer:
- \( a = 7 \), \( b = \frac{35}{26} \) dou
- \( c = 8 \), \( d = \frac{41}{52} \) dou
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 7
Variable 'c' has wrong value. Expected: 1, Actual: 8"""
