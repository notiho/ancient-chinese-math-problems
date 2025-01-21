"""
今有上禾三秉益實六斗當下禾十秉下禾五秉益實一斗當上禾二秉問上下禾實一秉各幾何
術曰如方程置上禾三秉正下禾一十秉負益實六斗負次置上禾二秉負下禾五秉正益實一斗負以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰上禾 a秉 實 b斗 下禾 c秉 實 d斗 
"""

"""
This problem involves solving a system of equations using ancient Chinese methods, specifically the "fangcheng" (方程) procedure, which is an early form of linear algebra. Let's translate the problem and procedure into Python code.

### Problem Description:
There are two types of grain, "upper grain" (上禾) and "lower grain" (下禾).  
- 3 bundles of upper grain plus 6 dou of additional grain are equivalent to 10 bundles of lower grain.  
- 5 bundles of lower grain plus 1 dou of additional grain are equivalent to 2 bundles of upper grain.  

Question: How much grain does one bundle of upper grain and one bundle of lower grain yield?

### Procedure:
The "fangcheng" procedure involves setting up a system of equations and solving it step by step using elimination. The solution will yield the amount of grain per bundle for both upper and lower grain.

---

### Python Code Implementation:


"""


from fractions import Fraction

# Problem setup
# Equation 1: 3上禾 - 10下禾 = -6 (converted to standard form)
# Equation 2: -2上禾 + 5下禾 = -1 (converted to standard form)

# Coefficients of the equations
上禾系數_1, 下禾系數_1, 常數_1 = 3, -10, -6  # First equation
上禾系數_2, 下禾系數_2, 常數_2 = -2, 5, -1   # Second equation

# Step 1: Eliminate one variable (e.g., 上禾)
# Multiply the first equation by 2 and the second equation by 3 to align 上禾 coefficients
上禾系數_1 *= 2
下禾系數_1 *= 2
常數_1 *= 2

上禾系數_2 *= 3
下禾系數_2 *= 3
常數_2 *= 3

# New equations:
# Equation 1: 6上禾 - 20下禾 = -12
# Equation 2: -6上禾 + 15下禾 = -3

# Add the two equations to eliminate 上禾
下禾系數 = 下禾系數_1 + 下禾系數_2
常數 = 常數_1 + 常數_2

# Solve for 下禾
下禾實 = Fraction(-常數, 下禾系數)

# Step 2: Solve for 上禾 using one of the original equations
# Substitute 下禾實 into the first equation: 3上禾 - 10下禾 = -6
上禾實 = Fraction(-常數_1 - 下禾系數_1 * 下禾實, 上禾系數_1)

# Step 3: Output results
a = 1  # One bundle of upper grain
b = 上禾實  # Grain per bundle of upper grain
c = 1  # One bundle of lower grain
d = 下禾實  # Grain per bundle of lower grain

# Final answer
print(f"上禾 {a}秉 實 {b}斗 下禾 {c}秉 實 {d}斗")


"""


---

### Explanation of the Code:
1. **Problem Setup**: The two equations are derived from the problem statement and converted into standard form.
2. **Elimination**: The coefficients of one variable (上禾) are aligned by multiplying the equations, and then the equations are added to eliminate that variable.
3. **Substitution**: The value of the remaining variable (下禾) is substituted back into one of the original equations to solve for the other variable (上禾).
4. **Output**: The results are presented as the amount of grain per bundle for both upper and lower grain.

### Answer:
The code will compute the values of `b` (grain per bundle of upper grain) and `d` (grain per bundle of lower grain).
"""


"""
Variable 'b' has wrong value. Expected: 8, Actual: -8
Variable 'd' has wrong value. Expected: 3, Actual: -3"""
