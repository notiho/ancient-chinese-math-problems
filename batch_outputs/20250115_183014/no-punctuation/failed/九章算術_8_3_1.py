"""
今有上禾五秉損實一斗一升當下禾七秉上禾七秉損實二斗五升當下禾五秉問上下禾實一秉各幾何
術曰如方程置上禾五秉正下禾七秉負損實一斗一升正次置上禾七秉正下禾五秉負損實二斗五升正以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰上禾 a秉 b升 下禾 c秉 d升 
"""

"""
This problem involves solving a system of linear equations to determine the yield of one sheaf of upper millet (*shang he*) and one sheaf of lower millet (*xia he*). The procedure involves using the ancient Chinese method of solving simultaneous equations, which is akin to Gaussian elimination.

### Problem Breakdown:
- **Given:**
  - 5 sheaves of upper millet and 7 sheaves of lower millet lose 1 dou and 1 sheng.
  - 7 sheaves of upper millet and 5 sheaves of lower millet lose 2 dou and 5 sheng.
- **Question:**
  - What is the yield of one sheaf of upper millet and one sheaf of lower millet?

### Procedure:
The procedure involves setting up the equations and solving them step by step using the "正負術" (positive-negative method), which is equivalent to elimination in modern terms.

---


"""


from fractions import Fraction

# Convert dou and sheng into a single unit (sheng)
# 1 dou = 10 sheng
損實1 = 1 * 10 + 1  # 1 dou 1 sheng = 11 sheng
損實2 = 2 * 10 + 5  # 2 dou 5 sheng = 25 sheng

# Set up the coefficients for the equations
# Equation 1: 5上禾 - 7下禾 = 11 (損實1)
# Equation 2: 7上禾 - 5下禾 = 25 (損實2)
上禾1 = 5
下禾1 = -7
實1 = 11

上禾2 = 7
下禾2 = -5
實2 = 25

# Step 1: Eliminate one variable (下禾) using the 正負術
# Multiply the first equation by 5 (coefficient of 下禾 in the second equation)
# Multiply the second equation by 7 (coefficient of 下禾 in the first equation)
# Subtract the two equations to eliminate 下禾
上禾系數 = 上禾1 * 5 - 上禾2 * 7
實系數 = 實1 * 5 - 實2 * 7

# Solve for 上禾 (yield of one sheaf of upper millet)
上禾實 = Fraction(實系數, 上禾系數)

# Step 2: Substitute 上禾實 back into one of the original equations to solve for 下禾
# Using the first equation: 5上禾 - 7下禾 = 11
下禾實 = Fraction(實1 - 上禾1 * 上禾實, 下禾1)

# Convert results back to dou and sheng
a = 上禾實.numerator // 10  # dou for 上禾
b = 上禾實.numerator % 10   # sheng for 上禾

c = 下禾實.numerator // 10  # dou for 下禾
d = 下禾實.numerator % 10   # sheng for 下禾

# Answer
a, b, c, d


"""


### Explanation of the Code:
1. **Unit Conversion:** Convert dou and sheng into a single unit (sheng) for easier calculations.
2. **Set Up Equations:** Represent the problem as two linear equations with coefficients for upper millet (*shang he*) and lower millet (*xia he*).
3. **Elimination (正負術):** Use elimination to solve for one variable (upper millet yield per sheaf).
4. **Back Substitution:** Substitute the solved value into one of the original equations to find the yield of lower millet per sheaf.
5. **Convert Back to Dou and Sheng:** Convert the results back into dou and sheng for the final answer.

### Final Answer:
The yield of one sheaf of upper millet is `a dou b sheng`, and the yield of one sheaf of lower millet is `c dou d sheng`.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 0
Variable 'c' has wrong value. Expected: 1, Actual: 0"""
