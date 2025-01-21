"""
今有上禾三秉益實六斗當下禾十秉下禾五秉益實一斗當上禾二秉問上下禾實一秉各幾何
術曰如方程置上禾三秉正下禾一十秉負益實六斗負次置上禾二秉負下禾五秉正益實一斗負以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰上禾 a秉 實 b斗 下禾 c秉 實 d斗 
"""

"""
This is a classic simultaneous equations problem from ancient Chinese mathematics, solved using a method similar to Gaussian elimination. Let's break it down step by step and translate it into Python code.

### Problem Description:
We are given:
1. 3 bundles of upper millet (上禾) plus an additional 6 dou of grain equals 10 bundles of lower millet (下禾).
2. 5 bundles of lower millet plus an additional 1 dou of grain equals 2 bundles of upper millet.

We are tasked to find the amount of grain (實) per bundle for both upper millet (上禾) and lower millet (下禾).

### Procedure:
The procedure involves setting up the equations, performing elimination, and solving for the unknowns step by step.

### Python Code:


"""


from fractions import Fraction

# Equation 1: 3上禾 - 10下禾 = -6 (converted to standard form)
上禾1 = 3
下禾1 = -10
實1 = -6

# Equation 2: -2上禾 + 5下禾 = -1 (converted to standard form)
上禾2 = -2
下禾2 = 5
實2 = -1

# Step 1: Eliminate one variable (e.g., 上禾) using the two equations.
# Multiply the first equation by 2 and the second equation by 3 to align 上禾 coefficients.
上禾1_scaled = 2 * 上禾1
下禾1_scaled = 2 * 下禾1
實1_scaled = 2 * 实1

上禾2_scaled = 3 * 上禾2
下禾2_scaled = 3 * 下禾2
實2_scaled = 3 * 实2

# Subtract the scaled equations to eliminate 上禾.
下禾_eliminated = 下禾1_scaled - 下禾2_scaled
實_eliminated = 實1_scaled - 實2_scaled

# Step 2: Solve for 下禾實 (grain per bundle of lower millet).
下禾實 = Fraction(實_eliminated, 下禾_eliminated)

# Step 3: Substitute 下禾實 back into one of the original equations to solve for 上禾實.
實1_substituted = 實1 - (下禾1 * 下禾實)
上禾實 = Fraction(實1_substituted, 上禾1)

# Step 4: Output the results.
a = 1  # 上禾 bundles
b = 上禾實  # Grain per bundle of 上禾
c = 1  # 下禾 bundles
d = 下禾實  # Grain per bundle of 下禾

print(f"上禾 {a}秉 實 {b}斗 下禾 {c}秉 實 {d}斗")


"""


### Explanation of the Code:
1. **Equation Setup**: The two equations are written in standard form, with coefficients for 上禾, 下禾, and the constant term (實).
2. **Variable Elimination**: The coefficients of 上禾 are aligned by scaling the equations, and then one variable (上禾) is eliminated by subtraction.
3. **Solve for 下禾實**: After eliminating 上禾, the remaining equation is solved for 下禾實.
4. **Back-Substitution**: The value of 下禾實 is substituted back into one of the original equations to solve for 上禾實.
5. **Output**: The results are displayed as the grain per bundle for both types of millet.

### Answer:
The output will provide the grain per bundle for both upper millet (上禾) and lower millet (下禾).
"""


"""
Code error: name '实1' is not defined"""
