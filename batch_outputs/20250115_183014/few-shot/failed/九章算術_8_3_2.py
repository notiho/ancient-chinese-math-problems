"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 b升 ，下禾 c秉 d升 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, specifically the "fangcheng" (方程) method, which is an early form of matrix elimination. Let's translate the problem and solve it step by step.

### Problem Description:
We are given:
1. 5 bundles of upper millet lose 1 dou and 1 sheng of grain when compared to 7 bundles of lower millet.
2. 7 bundles of upper millet lose 2 dou and 5 sheng of grain when compared to 5 bundles of lower millet.

We need to determine the amount of grain in one bundle of upper millet and one bundle of lower millet.

### Procedure:
The procedure involves setting up two equations and solving them using the fangcheng method:
1. Place the coefficients of the equations in a matrix-like structure.
2. Use elimination to solve for the unknowns.

---

### Step-by-Step Solution in Python:


"""


from fractions import Fraction

# Convert all units to sheng (1 dou = 10 sheng)
斗 = 10  # 1 dou = 10 sheng

# Equation 1: 5 upper millet bundles - 7 lower millet bundles = -1 dou - 1 sheng
上禾1 = 5
下禾1 = -7
損實1 = -(1 * 斗 + 1)  # Convert to sheng

# Equation 2: 7 upper millet bundles - 5 lower millet bundles = -2 dou - 5 sheng
上禾2 = 7
下禾2 = -5
損實2 = -(2 * 斗 + 5)  # Convert to sheng

# Step 1: Eliminate one variable (use 上禾 as the pivot)
# Multiply the first equation by 7 and the second equation by 5 to align 上禾 coefficients
上禾系數 = 上禾1 * 上禾2 - 上禾2 * 上禾1
下禾系數 = 下禾1 * 上禾2 - 下禾2 * 上禾1
損實系數 = 損實1 * 上禾2 - 損實2 * 上禾1

# Step 2: Solve for 下禾 (lower millet grain per bundle)
下禾實 = Fraction(損實系數, 下禾系數)

# Step 3: Substitute 下禾實 back into one of the original equations to solve for 上禾 (upper millet grain per bundle)
損實1_adjusted = 損實1 - 下禾1 * 下禾實
上禾實 = Fraction(損實1_adjusted, 上禾1)

# Convert results back to dou and sheng
a_dou = 上禾實 // 斗
a_sheng = 上禾實 % 斗

c_dou = 下禾實 // 斗
c_sheng = 下禾實 % 斗

# Final Answer
a = a_dou
b = a_sheng
c = c_dou
d = c_sheng

print(f"上禾 {a}斗 {b}升 ，下禾 {c}斗 {d}升 。")


"""


---

### Explanation of the Code:
1. **Unit Conversion**: All quantities are converted to `sheng` for consistency since 1 dou = 10 sheng.
2. **Matrix Elimination**: The coefficients of the equations are manipulated to eliminate one variable (下禾 in this case), leaving a single equation to solve for 下禾.
3. **Back Substitution**: The value of 下禾 is substituted back into one of the original equations to solve for 上禾.
4. **Result Conversion**: The results are converted back into dou and sheng for the final answer.

### Final Answer:
The grain in one bundle of upper millet and one bundle of lower millet is expressed in dou and sheng.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: -1
Variable 'c' has wrong value. Expected: 1, Actual: -1
Variable 'd' has wrong value. Expected: 2, Actual: 8"""
