"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉 a升 ，下禾一秉 b升 。
"""

"""
This is a classical simultaneous equations problem from ancient Chinese mathematics, solved using a method akin to Gaussian elimination. Let's translate the problem and solution into Python code step by step.

### Problem Description:
We are given two relationships between the quantities of "upper grain" (上禾) and "lower grain" (下禾):
1. 5 bundles of upper grain lose 1 dou and 1 sheng of grain, equivalent to 7 bundles of lower grain.
2. 7 bundles of upper grain lose 2 dou and 5 sheng of grain, equivalent to 5 bundles of lower grain.

We are tasked to find the amount of grain in one bundle of upper grain (上禾) and one bundle of lower grain (下禾).

### Procedure:
The procedure involves setting up a system of linear equations and solving it using elimination. The steps are described in the "方程術" (method of solving equations).

---


"""

#----- content starts here -----

from fractions import Fraction

# Convert dou and sheng to a single unit (sheng)
# 1 dou = 10 sheng
損實1 = 1 * 10 + 1  # 1 dou 1 sheng = 11 sheng
損實2 = 2 * 10 + 5  # 2 dou 5 sheng = 25 sheng

# Coefficients for the equations
# Equation 1: 5上禾 - 7下禾 = 11
# Equation 2: 7上禾 - 5下禾 = 25
上禾1, 下禾1, 常數1 = 5, -7, 損實1
上禾2, 下禾2, 常數2 = 7, -5, 損實2

# Step 1: Eliminate one variable (下禾) using elimination
# Multiply the first equation by 5 and the second equation by 7 to align 下禾 coefficients
方程1_新 = [上禾1 * 5, 下禾1 * 5, 常數1 * 5]  # 25上禾 - 35下禾 = 55
方程2_新 = [上禾2 * 7, 下禾2 * 7, 常數2 * 7]  # 49上禾 - 35下禾 = 175

# Subtract the two equations to eliminate 下禾
# (25上禾 - 35下禾) - (49上禾 - 35下禾) = 55 - 175
上禾_消去 = 方程1_新[0] - 方程2_新[0]  # 25 - 49 = -24
常數_消去 = 方程1_新[2] - 方程2_新[2]  # 55 - 175 = -120

# Solve for 上禾 (grain per bundle of upper grain)
上禾_實 = Fraction(常數_消去, 上禾_消去)  # -120 / -24 = 5 sheng

# Step 2: Substitute 上禾_實 back into one of the original equations to solve for 下禾
# Using the first equation: 5上禾 - 7下禾 = 11
# 5(5) - 7下禾 = 11
# 25 - 7下禾 = 11
# -7下禾 = 11 - 25
# -7下禾 = -14
# 下禾 = -14 / -7 = 2 sheng

# Final results
a = 上禾_實  # Grain per bundle of upper grain
b = Fraction(2)  # Grain per bundle of lower grain

# Output the results
print(f"上禾一秉 {a}升 ，下禾一秉 {b}升 。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Unit Conversion**: The given grain losses are converted from dou and sheng into a single unit (sheng) for easier calculation.
2. **Equation Setup**: The two relationships are expressed as linear equations.
3. **Elimination**: The coefficients of one variable (下禾) are aligned, and subtraction is used to eliminate it, leaving a single equation for 上禾.
4. **Back Substitution**: The value of 上禾 is substituted back into one of the original equations to solve for 下禾.
5. **Results**: The values of 上禾 and 下禾 are expressed as fractions for precision.

### Answer:
```
上禾一秉 5升 ，下禾一秉 2升 。
```
"""


"""
"""
