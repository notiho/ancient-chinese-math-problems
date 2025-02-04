"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉 a升 ，下禾一秉 b升 。
"""

"""
This problem involves solving a system of linear equations to determine the yield per bundle of "upper millet" (上禾) and "lower millet" (下禾). The procedure follows the ancient Chinese method of solving simultaneous equations, known as the "fangcheng" method.

### Problem Breakdown:
- **First equation**: 5 bundles of upper millet (上禾) and 7 bundles of lower millet (下禾) lose 1 dou and 1 sheng (11 sheng in total).
- **Second equation**: 7 bundles of upper millet (上禾) and 5 bundles of lower millet (下禾) lose 2 dou and 5 sheng (25 sheng in total).
- We need to find the yield per bundle of upper millet (上禾) and lower millet (下禾).

### Procedure:
The procedure involves setting up the equations, eliminating variables, and solving for the unknowns step by step.


"""


from fractions import Fraction

# Convert all measurements to sheng (1 dou = 10 sheng)
損實1 = 1 * 10 + 1  # 1斗1升 = 11升
損實2 = 2 * 10 + 5  # 2斗5升 = 25升

# Coefficients for the equations
# First equation: 5上禾 - 7下禾 = 11升
上禾1 = 5
下禾1 = -7
實1 = 損實1

# Second equation: 7上禾 - 5下禾 = 25升
上禾2 = 7
下禾2 = -5
實2 = 損實2

# Eliminate one variable (下禾) using the fangcheng method
# Multiply the first equation by 5 and the second equation by 7 to align 下禾 coefficients
上禾1 *= 5
下禾1 *= 5
實1 *= 5

上禾2 *= 7
下禾2 *= 7
實2 *= 7

# Subtract the first equation from the second to eliminate 下禾
上禾 = 上禾2 - 上禾1
實 = 實2 - 实1

# Solve for 上禾 (yield per bundle of upper millet)
a = Fraction(實, 上禾)

# Substitute a (上禾 yield) back into one of the original equations to solve for 下禾
# Using the first equation: 5上禾 - 7下禾 = 11升
實1 -= 5 * a
下禾 = Fraction(實1, -7)

# Convert results to sheng
a = a  # 上禾 yield per bundle in sheng
b = 下禾  # 下禾 yield per bundle in sheng

# Output the results
a, b


"""


### Explanation of the Code:
1. **Convert units**: All measurements are converted to sheng for consistency (1 dou = 10 sheng).
2. **Set up equations**: The coefficients for 上禾 and 下禾 are extracted from the problem statement.
3. **Eliminate a variable**: The fangcheng method is used to eliminate 下禾 by aligning its coefficients and subtracting the equations.
4. **Solve for 上禾**: The resulting equation is solved for 上禾 (a).
5. **Substitute back**: The value of 上禾 is substituted into one of the original equations to solve for 下禾 (b).
6. **Output results**: The yields per bundle of 上禾 and 下禾 are returned as fractions for precision.

### Final Answer:
- 上禾一秉 yields `a` sheng.
- 下禾一秉 yields `b` sheng.
"""


"""
Code error: name '实1' is not defined"""
