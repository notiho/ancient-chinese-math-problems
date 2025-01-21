"""
今有上禾三秉益實六斗當下禾十秉下禾五秉益實一斗當上禾二秉問上下禾實一秉各幾何
術曰如方程置上禾三秉正下禾一十秉負益實六斗負次置上禾二秉負下禾五秉正益實一斗負以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰上禾 a秉 實 b斗 下禾 c秉 實 d斗 
"""

"""
This is a classic simultaneous equations problem from ancient Chinese mathematics, solved using a method similar to Gaussian elimination. Let's translate the problem and solution into Python code step by step.

---

### Problem:
There are two types of grain, "upper grain" (上禾) and "lower grain" (下禾).  
- 3 bundles of upper grain plus 6 dou of additional grain equals 10 bundles of lower grain.  
- 5 bundles of lower grain plus 1 dou of additional grain equals 2 bundles of upper grain.  

Question: How much grain (in dou) does one bundle of upper grain and one bundle of lower grain yield?

---

### Procedure:
The procedure describes solving this system of equations using elimination:
1. Represent the equations as follows:
   - \( 3 \cdot 上禾 - 10 \cdot 下禾 = -6 \)
   - \( -2 \cdot 上禾 + 5 \cdot 下禾 = -1 \)
2. Use elimination to solve for the grain yield per bundle of upper and lower grain.

---

### Python Code:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 3 * 上禾 - 10 * 下禾 = -6
# Equation 2: -2 * 上禾 + 5 * 下禾 = -1

# Representing the equations
上禾1, 下禾1, 實1 = 3, -10, -6  # Coefficients for the first equation
上禾2, 下禾2, 實2 = -2, 5, -1   # Coefficients for the second equation

# Step 1: Eliminate one variable (e.g., 下禾)
# Multiply the first equation by 5 and the second equation by 10 to align 下禾 coefficients
上禾1, 下禾1, 實1 = 5 * 上禾1, 5 * 下禾1, 5 * 實1
上禾2, 下禾2, 實2 = 10 * 上禾2, 10 * 下禾2, 10 * 實2

# New equations:
# 15 * 上禾 - 50 * 下禾 = -30
# -20 * 上禾 + 50 * 下禾 = -10

# Add the equations to eliminate 下禾
上禾 = 上禾1 + 上禾2
實 = 實1 + 實2

# Solve for 上禾
上禾實 = Fraction(實, 上禾)

# Step 2: Solve for 下禾 using one of the original equations
# Substitute 上禾實 into the first equation: 3 * 上禾 - 10 * 下禾 = -6
下禾實 = Fraction((實1 - 上禾1 * 上禾實), 下禾1)

# Results
a = 1  # Each bundle of upper grain
b = 上禾實  # Grain yield per bundle of upper grain
c = 1  # Each bundle of lower grain
d = 下禾實  # Grain yield per bundle of lower grain

# Output
print(f"上禾 {a}秉 實 {b}斗 下禾 {c}秉 實 {d}斗")


"""


---

### Explanation of the Code:
1. The equations are represented in the form \( ax + by = c \), where \( x \) is the upper grain yield and \( y \) is the lower grain yield.
2. The elimination method is used to remove one variable (下禾) by aligning coefficients and adding the equations.
3. Once one variable (上禾) is solved, it is substituted back into one of the original equations to solve for the other variable (下禾).
4. The results are expressed as fractions to ensure precision.

---

### Answer:
The output will provide the grain yield per bundle of upper and lower grain in dou.
"""


"""
"""
