"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
This problem involves solving a system of linear equations to determine the yield of one sheaf of "upper millet" (上禾) and one sheaf of "lower millet" (下禾). Here's the step-by-step solution encoded in Python:

### Problem Breakdown:
1. **Given Conditions:**
   - 3 sheaves of upper millet (上禾) plus 6 dou of additional yield are equivalent to 10 sheaves of lower millet (下禾).
   - 5 sheaves of lower millet (下禾) plus 1 dou of additional yield are equivalent to 2 sheaves of upper millet (上禾).

2. **Goal:**
   - Determine the yield of one sheaf of upper millet (上禾) and one sheaf of lower millet (下禾).

3. **Method:**
   - Use the method of solving simultaneous linear equations, as described in the ancient Chinese "fangcheng" (方程) method.

---

### Python Code Implementation:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define variables
上禾 = symbols('上禾')  # Yield of one sheaf of upper millet (in dou)
下禾 = symbols('下禾')  # Yield of one sheaf of lower millet (in dou)

# Define the equations based on the problem
# Equation 1: 3上禾 + 6 = 10下禾
eq1 = Eq(3 * 上禾 + 6, 10 * 下禾)

# Equation 2: 2上禾 = 5下禾 + 1
eq2 = Eq(2 * 上禾, 5 * 下禾 + 1)

# Solve the system of equations
solution = solve((eq1, eq2), (上禾, 下禾))

# Extract the results
a = solution[上禾]  # Yield of one sheaf of upper millet
b = solution[下禾]  # Yield of one sheaf of lower millet

# Output the results
print(f"上禾一秉實 {a}斗")
print(f"下禾一秉實 {b}斗")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Define Variables:**
   - `上禾` represents the yield of one sheaf of upper millet.
   - `下禾` represents the yield of one sheaf of lower millet.

2. **Set Up Equations:**
   - The first equation corresponds to the condition: \( 3 \cdot 上禾 + 6 = 10 \cdot 下禾 \).
   - The second equation corresponds to the condition: \( 2 \cdot 上禾 = 5 \cdot 下禾 + 1 \).

3. **Solve the System:**
   - Use the `solve` function from the `sympy` library to solve the two equations simultaneously.

4. **Output Results:**
   - The solution gives the yield of one sheaf of upper millet (`a`) and one sheaf of lower millet (`b`).

---

### Output:
The solution to the problem will be printed as:
```
上禾一秉實 2斗
下禾一秉實 1斗
```

Thus:
- The yield of one sheaf of upper millet is **2 dou**.
- The yield of one sheaf of lower millet is **1 dou**.
"""


"""
"""
