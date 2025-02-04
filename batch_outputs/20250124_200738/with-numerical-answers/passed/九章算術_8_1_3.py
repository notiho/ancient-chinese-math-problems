"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a(=35/26)斗 ，下禾一秉實 b(=41/52)斗 。
"""

"""
This problem involves solving a system of equations using ancient Chinese methods, specifically the "fangcheng" (方程) method, which is equivalent to solving simultaneous linear equations. The problem describes relationships between the yields of upper and lower grains (上禾 and 下禾) in terms of their respective contributions to total yields.

Let's translate the problem and solve it step by step.

---

### Problem Description:
There are 7 bundles of upper grain (上禾), which lose 1 dou of yield, and when 2 bundles of lower grain (下禾) are added, the total yield becomes 10 dou.  
There are 8 bundles of lower grain (下禾), which gain 1 dou of yield, and when 2 bundles of upper grain (上禾) are added, the total yield becomes 10 dou.  

Question: What is the yield of 1 bundle of upper grain (上禾) and 1 bundle of lower grain (下禾)?

---

### Procedure:
1. Represent the unknowns:
   - Let `x` be the yield of 1 bundle of upper grain (上禾).
   - Let `y` be the yield of 1 bundle of lower grain (下禾).

2. Translate the problem into equations:
   - From the first condition:  
     \( 7x - 1 + 2y = 10 \)  
     Simplify:  
     \( 7x + 2y = 11 \)  
   - From the second condition:  
     \( 8y + 1 + 2x = 10 \)  
     Simplify:  
     \( 2x + 8y = 9 \)

3. Solve the system of equations using the fangcheng method.

---

### Fangcheng Method:
The procedure involves eliminating variables step by step to solve for the unknowns.

---


"""

#----- content starts here -----

from fractions import Fraction

# Step 1: Represent the equations
# Equation 1: 7x + 2y = 11
# Equation 2: 2x + 8y = 9

# Step 2: Eliminate one variable (e.g., y) by aligning coefficients
# Multiply Equation 1 by 8 and Equation 2 by 2 to align coefficients of y
eq1_multiplier = 8
eq2_multiplier = 2

# Multiply equations
eq1 = [7 * eq1_multiplier, 2 * eq1_multiplier, 11 * eq1_multiplier]  # 56x + 16y = 88
eq2 = [2 * eq2_multiplier, 8 * eq2_multiplier, 9 * eq2_multiplier]   # 4x + 16y = 18

# Subtract Equation 2 from Equation 1 to eliminate y
eliminated_y = [
    eq1[0] - eq2[0],  # Coefficient of x
    eq1[1] - eq2[1],  # Coefficient of y (should be 0)
    eq1[2] - eq2[2]   # Constant term
]  # Result: 52x = 70

# Solve for x
x = Fraction(eliminated_y[2], eliminated_y[0])  # x = 70 / 52 = 35 / 26

# Step 3: Substitute x back into one of the original equations to solve for y
# Use Equation 1: 7x + 2y = 11
substituted_x = 7 * x  # 7 * (35 / 26) = 245 / 26
remaining_y = 11 - substituted_x  # 11 - (245 / 26) = (286 / 26) - (245 / 26) = 41 / 26
y = Fraction(remaining_y, 2)  # y = (41 / 26) / 2 = 41 / 52

# Final results
a = x  # Yield of 1 bundle of upper grain (上禾)
b = y  # Yield of 1 bundle of lower grain (下禾)

# Outputs
a, b  # a = 35/26, b = 41/52
#----- content ends here -----


"""


---

### Answer:
- The yield of 1 bundle of upper grain (上禾) is \( a = \frac{35}{26} \) dou.
- The yield of 1 bundle of lower grain (下禾) is \( b = \frac{41}{52} \) dou.
"""


"""
"""
