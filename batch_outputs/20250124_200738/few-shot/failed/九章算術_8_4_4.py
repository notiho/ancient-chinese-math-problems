"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a升 ，下禾一秉實 b升 。
"""

"""
This is a classic simultaneous equations problem from ancient Chinese mathematics, solved using a method similar to Gaussian elimination. Let's translate the procedure into Python step by step.

### Problem Description:
We are given:
1. 6 bundles of "upper millet" lose 1 dou and 8 sheng of grain when compared to 10 bundles of "lower millet."
2. 15 bundles of "lower millet" lose 5 sheng of grain when compared to 5 bundles of "upper millet."

We are tasked to find how much grain (in sheng) is in one bundle of "upper millet" and one bundle of "lower millet."

### Procedure:
The procedure uses a method similar to solving simultaneous linear equations. Let's implement it step by step.


"""

#----- content starts here -----

from fractions import Fraction

# Convert units to sheng (1 dou = 10 sheng)
損實1 = 1 * 10 + 8  # 1 dou 8 sheng = 18 sheng
損實2 = 5  # 5 sheng

# Coefficients for the equations
# Equation 1: 6上禾 - 10下禾 = 18
上禾1 = 6
下禾1 = -10
常數1 = 損實1

# Equation 2: -5上禾 + 15下禾 = 5
上禾2 = -5
下禾2 = 15
常數2 = 損實2

# Step 1: Eliminate one variable (use 上禾 as the pivot)
# Multiply the first equation by 5 and the second equation by 6 to align 上禾 coefficients
上禾1, 下禾1, 常數1 = 5 * 上禾1, 5 * 下禾1, 5 * 常數1
上禾2, 下禾2, 常數2 = 6 * 上禾2, 6 * 下禾2, 6 * 常數2

# Subtract the second equation from the first to eliminate 上禾
下禾 = 下禾1 - 下禾2
常數 = 常數1 - 常數2

# Solve for 下禾 (value of one bundle of lower millet in sheng)
下禾實 = Fraction(常數, 下禾)

# Step 2: Substitute 下禾實 back into one of the original equations to solve for 上禾
常數1 -= 下禾1 * 下禾實  # Adjust the constant term of the first equation
上禾實 = Fraction(常數1, 上禾1)  # Solve for 上禾

# Final results
a = 上禾實  # Grain in one bundle of upper millet (in sheng)
b = 下禾實  # Grain in one bundle of lower millet (in sheng)

# Output the results
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **Unit Conversion**: Convert all measurements to the same unit (sheng) for consistency.
2. **Set Up Equations**: Represent the problem as two linear equations.
3. **Elimination**: Use elimination to solve for one variable (下禾).
4. **Back Substitution**: Substitute the value of 下禾 into one of the original equations to solve for 上禾.
5. **Output**: The results are given as fractions to ensure precision.

### Answer:
The grain in one bundle of "upper millet" is `a` sheng, and the grain in one bundle of "lower millet" is `b` sheng.
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 16/7
Variable 'b' has wrong value. Expected: 3, Actual: -3/7"""
