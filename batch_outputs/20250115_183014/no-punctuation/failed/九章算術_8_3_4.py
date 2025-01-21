"""
今有上禾五秉損實一斗一升當下禾七秉上禾七秉損實二斗五升當下禾五秉問上下禾實一秉各幾何
術曰如方程置上禾五秉正下禾七秉負損實一斗一升正次置上禾七秉正下禾五秉負損實二斗五升正以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰上禾 a秉 b升 下禾 c秉 d升 
"""

"""
This is a classic ancient Chinese problem involving simultaneous equations and proportional reasoning. The problem essentially asks us to solve for the amount of grain (实) per bundle (秉) for both the upper (上禾) and lower (下禾) types of grain.

Let's break it down step by step and encode it in Python.

---

### Problem Description:
We are given:
1. **First condition**: 5 bundles of upper grain (上禾) and 7 bundles of lower grain (下禾) lose 1 dou and 1 sheng of grain.
2. **Second condition**: 7 bundles of upper grain (上禾) and 5 bundles of lower grain (下禾) lose 2 dou and 5 sheng of grain.

We need to find the amount of grain per bundle for both the upper and lower types of grain.

---

### Procedure:
The solution involves setting up a system of linear equations and solving it using the ancient Chinese "fangcheng" (方程) method, which is equivalent to Gaussian elimination.

1. Represent the problem as two equations:
   - \( 5x + 7y = 1斗1升 \)
   - \( 7x + 5y = 2斗5升 \)

   Here, \(x\) is the grain per bundle of upper grain (上禾), and \(y\) is the grain per bundle of lower grain (下禾).

2. Convert the units into a consistent format (e.g., convert dou and sheng into sheng, where 1 dou = 10 sheng).

3. Use the fangcheng method to solve for \(x\) and \(y\).

4. Convert the results back into dou and sheng.

---

### Python Code:


"""


from fractions import Fraction

# Convert the given losses into sheng (1 dou = 10 sheng)
損實1 = 1 * 10 + 1  # 1斗1升 = 11升
損實2 = 2 * 10 + 5  # 2斗5升 = 25升

# Coefficients for the equations
# First equation: 5x + 7y = 11
# Second equation: 7x + 5y = 25
上禾1, 下禾1 = 5, 7
上禾2, 下禾2 = 7, 5

# Use the fangcheng method (Gaussian elimination)
# Step 1: Eliminate one variable
# Multiply the first equation by 7 and the second equation by 5 to align coefficients of x
eq1 = (上禾1 * 7, 下禾1 * 7, 損實1 * 7)  # (35x, 49y, 77)
eq2 = (上禾2 * 5, 下禾2 * 5, 損實2 * 5)  # (35x, 25y, 125)

# Subtract the second equation from the first to eliminate x
# (35x + 49y - 35x - 25y = 77 - 125)
_, 下禾_diff, 損實_diff = eq1[1] - eq2[1], eq1[2] - eq2[2]
下禾系數 = 下禾_diff  # Coefficient of y
損實系數 = 損實_diff  # Constant term

# Solve for y (grain per bundle of lower grain)
下禾實 = Fraction(損實系數, 下禾系數)

# Substitute y back into the first equation to solve for x
上禾實 = Fraction(損實1 - 下禾1 * 下禾實, 上禾1)

# Convert results back into dou and sheng
a_dou, a_sheng = divmod(上禾實.numerator, 上禾實.denominator * 10)
b_dou, b_sheng = divmod(下禾實.numerator, 下禾實.denominator * 10)

# Output the results
a, b = 上禾實, 下禾實
print(f"上禾 {a_dou}斗 {a_sheng}升 下禾 {b_dou}斗 {b_sheng}升")


"""


---

### Explanation of the Code:
1. **Unit Conversion**: The given losses are converted into a consistent unit (sheng).
2. **Equation Setup**: The coefficients of the equations are set up based on the problem description.
3. **Fangcheng Method**: The equations are solved using elimination (subtracting one equation from the other to eliminate a variable).
4. **Result Conversion**: The results are converted back into dou and sheng for the final answer.

---

### Final Answer:
The code will compute the values of \(x\) (grain per bundle of upper grain) and \(y\) (grain per bundle of lower grain) and output them in the required format.
"""


"""
Code error: not enough values to unpack (expected 3, got 2)"""
