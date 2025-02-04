"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉 a升 ，下禾一秉 b升 。
"""

"""
This is a classic simultaneous equations problem from ancient Chinese mathematics, solved using a method similar to Gaussian elimination. Let's break it down and translate it into Python code.

---

### Problem:
There are two types of grain, "upper grain" (上禾) and "lower grain" (下禾).  
- 5 bundles of upper grain and 7 bundles of lower grain lose 1 dou and 1 sheng (11 sheng in total).  
- 7 bundles of upper grain and 5 bundles of lower grain lose 2 dou and 5 sheng (25 sheng in total).  

Question: How much grain does one bundle of upper grain (上禾) and one bundle of lower grain (下禾) yield?

---

### Procedure:
1. Represent the problem as two equations:
   - \( 5x + 7y = 11 \)  
   - \( 7x + 5y = 25 \)  
   Here, \(x\) is the yield of one bundle of upper grain (上禾), and \(y\) is the yield of one bundle of lower grain (下禾).

2. Solve the equations using the elimination method (方程術). This involves:
   - Eliminating one variable by multiplying and subtracting the equations.
   - Solving for the remaining variable.
   - Back-substituting to find the other variable.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# Equation 1: 5x + 7y = 11
# Equation 2: 7x + 5y = 25

# Convert dou and sheng to sheng (1 dou = 10 sheng)
eq1_constant = 1 * 10 + 1  # 1 dou 1 sheng = 11 sheng
eq2_constant = 2 * 10 + 5  # 2 dou 5 sheng = 25 sheng

# Coefficients of x (upper grain) and y (lower grain)
a1, b1 = 5, 7  # Coefficients for equation 1
a2, b2 = 7, 5  # Coefficients for equation 2

# Step 1: Eliminate one variable (use elimination method)
# Multiply equations to align coefficients of x
eq1_mult = a2  # Multiply equation 1 by a2 (7)
eq2_mult = a1  # Multiply equation 2 by a1 (5)

# New equations after multiplication
new_a1, new_b1, new_c1 = eq1_mult * a1, eq1_mult * b1, eq1_mult * eq1_constant
new_a2, new_b2, new_c2 = eq2_mult * a2, eq2_mult * b2, eq2_mult * eq2_constant

# Subtract the equations to eliminate x
b_final = new_b1 - new_b2
c_final = new_c1 - new_c2

# Solve for y (lower grain yield per bundle)
y = Fraction(c_final, b_final)

# Step 2: Back-substitute to solve for x (upper grain yield per bundle)
x = Fraction(eq1_constant - b1 * y, a1)

# Convert results to sheng
a = x  # Upper grain yield per bundle
b = y  # Lower grain yield per bundle

# Print results
print(f"上禾一秉 yields {a} 升 (sheng)")
print(f"下禾一秉 yields {b} 升 (sheng)")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Equation Setup**: The two equations are set up based on the problem description. Constants are converted to sheng for consistency.
2. **Elimination Method**: The equations are multiplied to align the coefficients of \(x\), and one variable is eliminated by subtraction.
3. **Solve for \(y\)**: After eliminating \(x\), \(y\) (lower grain yield per bundle) is solved.
4. **Back-Substitution for \(x\)**: The value of \(y\) is substituted back into one of the original equations to solve for \(x\) (upper grain yield per bundle).
5. **Fraction Handling**: The `Fraction` class ensures precise calculations without floating-point errors.

---

### Answer:
The output will be:
```
上禾一秉 yields a 升 (sheng)
下禾一秉 yields b 升 (sheng)
```
Where \(a\) and \(b\) are the exact yields of one bundle of upper and lower grain, respectively.
"""


"""
Variable 'b' has wrong value. Expected: 2, Actual: -2"""
