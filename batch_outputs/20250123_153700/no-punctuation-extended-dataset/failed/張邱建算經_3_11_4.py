"""
今有上錦三疋中錦二疋下錦一疋直絹四十五疋上錦二疋中錦三疋下錦一疋直絹四十三疋上錦一疋中錦二疋下錦三疋直絹三十五疋問上中下錦各直絹幾何
術曰如方程
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
答曰上錦一疋直絹 a疋 中錦一疋直絹 b疋 下錦一疋直絹 c疋
"""

"""
This problem involves solving a system of linear equations, which is described as "方程術" (the method of simultaneous equations). The problem involves determining the value of each type of silk (上錦, 中錦, 下錦) in terms of plain silk (直絹). Here's the solution:

### Problem Description:
We are given three equations based on the relationships between 上錦 (upper silk), 中錦 (middle silk), 下錦 (lower silk), and 直絹 (plain silk):

1. \( 3 \cdot 上錦 + 2 \cdot 中錦 + 1 \cdot 下錦 = 45 \)
2. \( 2 \cdot 上錦 + 3 \cdot 中錦 + 1 \cdot 下錦 = 43 \)
3. \( 1 \cdot 上錦 + 2 \cdot 中錦 + 3 \cdot 下錦 = 35 \)

We need to solve for \( 上錦 \), \( 中錦 \), and \( 下錦 \) in terms of 直絹.

---

### Solution Using 方程術 (Simultaneous Equations Method):


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 3 * 上錦 + 2 * 中錦 + 1 * 下錦 = 45
# Equation 2: 2 * 上錦 + 3 * 中錦 + 1 * 下錦 = 43
# Equation 3: 1 * 上錦 + 2 * 中錦 + 3 * 下錦 = 35

# Step 1: Define the coefficients and constants
a1, b1, c1, d1 = 3, 2, 1, 45  # Coefficients and constant for equation 1
a2, b2, c2, d2 = 2, 3, 1, 43  # Coefficients and constant for equation 2
a3, b3, c3, d3 = 1, 2, 3, 35  # Coefficients and constant for equation 3

# Step 2: Eliminate 下錦 (c) from the first two equations
# Multiply the first equation by c2 and the second equation by c1, then subtract
factor1 = c2
factor2 = c1

A1 = a1 * factor1 - a2 * factor2
B1 = b1 * factor1 - b2 * factor2
D1 = d1 * factor1 - d2 * factor2

# Step 3: Eliminate 下錦 (c) from the second and third equations
# Multiply the second equation by c3 and the third equation by c2, then subtract
factor3 = c3
factor4 = c2

A2 = a2 * factor3 - a3 * factor4
B2 = b2 * factor3 - b3 * factor4
D2 = d2 * factor3 - d3 * factor4

# Step 4: Solve for 中錦 (b) using the two new equations
# Multiply the first new equation by B2 and the second new equation by B1, then subtract
factor5 = B2
factor6 = B1

A3 = A1 * factor5 - A2 * factor6
D3 = D1 * factor5 - D2 * factor6

# Solve for 中錦 (b)
中錦 = Fraction(D3, A3)

# Step 5: Solve for 上錦 (a) using one of the new equations
上錦 = Fraction(D1 - B1 * 中錦, A1)

# Step 6: Solve for 下錦 (c) using one of the original equations
下錦 = Fraction(d1 - a1 * 上錦 - b1 * 中錦, c1)

# Outputs
a = 上錦
b = 中錦
c = 下錦

print(f"上錦一疋直絹 {a} 疋")
print(f"中錦一疋直絹 {b} 疋")
print(f"下錦一疋直絹 {c} 疋")


"""


---

### Explanation of the Code:
1. **Step 1:** Eliminate one variable (下錦) from two pairs of equations to reduce the system to two equations with two unknowns.
2. **Step 2:** Use the reduced equations to eliminate another variable (中錦), leaving one equation with one unknown (上錦).
3. **Step 3:** Solve for the remaining variables (中錦 and 下錦) using back-substitution into the previous equations.
4. **Fractions:** The `Fraction` class is used to ensure exact arithmetic without floating-point errors.

---

### Final Answer:
The values of \( 上錦 \), \( 中錦 \), and \( 下錦 \) in terms of 直絹 are:

- \( 上錦 = a \) 疋
- \( 中錦 = b \) 疋
- \( 下錦 = c \) 疋
"""


"""
Variable 'a' has wrong value. Expected: 9, Actual: 11
Variable 'b' has wrong value. Expected: 7, Actual: 9
Variable 'c' has wrong value. Expected: 4, Actual: -6"""
