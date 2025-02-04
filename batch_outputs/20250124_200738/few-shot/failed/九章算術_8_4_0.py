"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a升 ，下禾一秉實 b升 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, as described in the "方程術" (fangcheng method). Below is the Python implementation of the procedure:


"""

#----- content starts here -----

from fractions import Fraction

# 上禾六秉，損實一斗八升，當下禾一十秉
# Convert 1斗8升 to total 升 (1斗 = 10升)
上禾1 = 6
下禾1 = -10
損實1 = 1 * 10 + 8  # 1斗8升 = 18升

# 下禾十五秉，損實五升，當上禾五秉
上禾2 = -5
下禾2 = 15
損實2 = 5

# 方程術: Eliminate one variable (下禾) using the two equations
# Multiply the first equation by 15 and the second equation by 10 to align 下禾 coefficients
上禾1_scaled = 15 * 上禾1
下禾1_scaled = 15 * 下禾1
損實1_scaled = 15 * 損實1

上禾2_scaled = 10 * 上禾2
下禾2_scaled = 10 * 下禾2
損實2_scaled = 10 * 損實2

# Subtract the second scaled equation from the first scaled equation to eliminate 下禾
上禾_eliminated = 上禾1_scaled - 上禾2_scaled
損實_eliminated = 損實1_scaled - 損實2_scaled

# Solve for 上禾 (one 秉 of 上禾)
上禾實 = Fraction(損實_eliminated, 上禾_eliminated)

# Substitute 上禾實 back into one of the original equations to solve for 下禾實
# Using the first equation: 6 * 上禾實 - 10 * 下禾實 = 18
下禾實 = Fraction(損實1 - 上禾1 * 上禾實, 下禾1)

# Convert results to 升
a = 上禾實  # 上禾一秉實
b = 下禾實  # 下禾一秉實

# Output the results
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Conversion**: The problem provides the losses in terms of 斗 and 升. These are converted to 升 for consistent calculations (1斗 = 10升).
2. **Scaling Equations**: The coefficients of 下禾 in both equations are scaled to align their magnitudes, enabling elimination of 下禾.
3. **Elimination**: Subtracting the scaled equations eliminates 下禾, leaving an equation with only 上禾, which is solved.
4. **Back Substitution**: The value of 上禾 is substituted back into one of the original equations to solve for 下禾.
5. **Output**: The results are presented as fractions in 升 for both 上禾 and 下禾.

### Answer:
The solution gives:
- 上禾一秉實 = `a` 升
- 下禾一秉實 = `b` 升
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 11/7
Variable 'b' has wrong value. Expected: 3, Actual: -6/7"""
