"""
今有上禾五秉損實一斗一升當下禾七秉上禾七秉損實二斗五升當下禾五秉問上下禾實一秉各幾何
術曰如方程置上禾五秉正下禾七秉負損實一斗一升正次置上禾七秉正下禾五秉負損實二斗五升正以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰上禾 a秉 b升 下禾 c秉 d升 
"""

"""
This problem involves solving a system of equations to determine the yield of one bundle of "upper millet" (上禾) and one bundle of "lower millet" (下禾). The procedure uses the ancient Chinese method of solving simultaneous equations, which is similar to Gaussian elimination.

### Problem Breakdown:
- **Given:**
  - 5 bundles of upper millet and 7 bundles of lower millet lose a total of 1 dou and 1 sheng.
  - 7 bundles of upper millet and 5 bundles of lower millet lose a total of 2 dou and 5 sheng.
- **Question:**
  - What is the yield of one bundle of upper millet and one bundle of lower millet?

### Procedure:
1. Represent the problem as a system of equations:
   - \( 5x + 7y = 1斗1升 \)
   - \( 7x + 5y = 2斗5升 \)
   Here, \(x\) is the yield of one bundle of upper millet, and \(y\) is the yield of one bundle of lower millet.

2. Convert the units of dou and sheng into a consistent unit (sheng):
   - 1 dou = 10 sheng.
   - \( 1斗1升 = 10 + 1 = 11升 \)
   - \( 2斗5升 = 20 + 5 = 25升 \)

3. Solve the system of equations using the ancient Chinese method:
   - Eliminate one variable by multiplying and subtracting equations.
   - Solve for the remaining variable.
   - Back-substitute to find the other variable.

4. Convert the results back into dou and sheng.

### Python Code Implementation:

"""


from fractions import Fraction

# Given data
上禾_秉1 = 5  # Coefficient of upper millet in the first equation
下禾_秉1 = 7  # Coefficient of lower millet in the first equation
損實1 = 11    # Total loss in the first equation (in sheng)

上禾_秉2 = 7  # Coefficient of upper millet in the second equation
下禾_秉2 = 5  # Coefficient of lower millet in the second equation
損實2 = 25    # Total loss in the second equation (in sheng)

# Step 1: Eliminate one variable (use the ancient method)
# Multiply the first equation by 7 (coefficient of 上禾 in the second equation)
# Multiply the second equation by 5 (coefficient of 上禾 in the first equation)
eq1_multiplied = [上禾_秉1 * 7, 下禾_秉1 * 7, 損實1 * 7]
eq2_multiplied = [上禾_秉2 * 5, 下禾_秉2 * 5, 損實2 * 5]

# Subtract the equations to eliminate 上禾
下禾_diff = eq1_multiplied[1] - eq2_multiplied[1]
損實_diff = eq1_multiplied[2] - eq2_multiplied[2]

# Solve for 下禾 (y)
下禾_實 = Fraction(損實_diff, 下禾_diff)

# Step 2: Back-substitute to find 上禾 (x)
# Use the first equation: 5x + 7y = 11
上禾_實 = Fraction(損實1 - 下禾_秉1 * 下禾_實, 上禾_秉1)

# Step 3: Convert results back into dou and sheng
def convert_to_dou_sheng(value):
    dou = value // 10
    sheng = value % 10
    return (dou, sheng)

上禾_dou, 上禾_sheng = convert_to_dou_sheng(上禾_實)
下禾_dou, 下禾_sheng = convert_to_dou_sheng(下禾_實)

# Final Answer
a, b = 上禾_dou, 上禾_sheng
c, d = 下禾_dou, 下禾_sheng

print(f"上禾 {a}斗 {b}升, 下禾 {c}斗 {d}升")


"""


### Explanation of the Code:
1. **Input Conversion:** The losses are converted into a consistent unit (sheng) for easier calculation.
2. **Equation Elimination:** The coefficients of one variable (上禾) are equalized by multiplying the equations, and then subtraction eliminates that variable.
3. **Variable Solving:** The remaining variable (下禾) is solved using the difference of the equations. Back-substitution is used to find the other variable (上禾).
4. **Unit Conversion:** The results are converted back into dou and sheng for the final answer.

### Final Answer:
The yield of one bundle of upper millet is \(a\) dou and \(b\) sheng, and the yield of one bundle of lower millet is \(c\) dou and \(d\) sheng.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 0
Variable 'c' has wrong value. Expected: 1, Actual: -1
Variable 'd' has wrong value. Expected: 2, Actual: 8"""
