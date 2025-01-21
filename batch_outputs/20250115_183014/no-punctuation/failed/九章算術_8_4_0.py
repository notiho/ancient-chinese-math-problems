"""
今有上禾六秉損實一斗八升當下禾一十秉下禾十五秉損實五升當上禾五秉問上下禾實一秉各幾何
術曰如方程置上禾六秉正下禾一十秉負損實一斗八升正次置上禾五秉負下禾一十五秉正損實五升正以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰上禾 a秉 實 b升 下禾 c秉 實 d升 
"""

"""
This problem involves solving a system of equations using ancient Chinese "fangcheng" (matrix-like) methods. Let's break it down and encode the solution step by step.

### Problem Description:
We are given:
1. **First equation**: 6 bundles of upper millet (上禾), 10 bundles of lower millet (下禾), and a total loss of 1 dou 8 sheng (18 sheng).
2. **Second equation**: 5 bundles of upper millet (上禾), 15 bundles of lower millet (下禾), and a total loss of 5 sheng.

We are tasked to find the actual yield per bundle of upper millet (上禾) and lower millet (下禾).

### Procedure:
The procedure follows the ancient "fangcheng" method, which is similar to solving simultaneous linear equations. Here's the step-by-step breakdown:

1. Represent the problem as a system of equations:
   - \( 6x + 10y = 18 \) (where \( x \) is the yield per bundle of upper millet, and \( y \) is the yield per bundle of lower millet).
   - \( 5x + 15y = 5 \).

2. Use the "正負術" (positive-negative method) to eliminate one variable and solve for the other.

3. Substitute back to find the remaining variable.

4. Convert the results into dou and sheng.

### Python Code Implementation:


"""


from fractions import Fraction

# Equation 1: 6上禾 + 10下禾 = 18升
上禾1 = 6
下禾1 = 10
實1 = 18  # 1斗8升 = 18升

# Equation 2: 5上禾 + 15下禾 = 5升
上禾2 = 5
下禾2 = 15
實2 = 5

# Step 1: Eliminate one variable (use "正負術")
# Multiply the first equation by 5 and the second equation by 6 to align the coefficients of 上禾
上禾系數 = 上禾1 * 上禾2
下禾系數1 = 下禾1 * 上禾2
下禾系數2 = 下禾2 * 上禾1
實系數1 = 實1 * 上禾2
實系數2 = 實2 * 上禾1

# Subtract the two equations to eliminate 上禾
下禾差 = 下禾系數2 - 下禾系數1
實差 = 實系數2 - 實系數1

# Solve for 下禾 (yield per bundle of lower millet)
下禾實 = Fraction(實差, 下禾差)

# Step 2: Substitute 下禾實 back into one of the original equations to solve for 上禾
實1_adjusted = 實1 - (下禾1 * 下禾實)
上禾實 = Fraction(實1_adjusted, 上禾1)

# Step 3: Convert results into dou and sheng
# 上禾實 and 下禾實 are in sheng per bundle
a = 上禾1  # Number of 上禾 bundles
b = 上禾實  # Yield per 上禾 bundle in sheng
c = 下禾1  # Number of 下禾 bundles
d = 下禾實  # Yield per 下禾 bundle in sheng

# Output results
a = 上禾實
b = 下禾實


"""


### Explanation of Variables:
- \( a \): Number of upper millet bundles.
- \( b \): Yield per bundle of upper millet in sheng.
- \( c \): Number of lower millet bundles.
- \( d \): Yield per bundle of lower millet in sheng.

### Final Answer:
The code will compute the yield per bundle for both upper and lower millet based on the given equations.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 11/2
Variable 'b' has wrong value. Expected: 8, Actual: -3/2
Variable 'c' has wrong value. Expected: 1, Actual: 10
Variable 'd' has wrong value. Expected: 3, Actual: -3/2"""
