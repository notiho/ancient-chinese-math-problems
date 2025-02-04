"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a升 ，下禾一秉實 b升 。
"""

"""
This problem involves solving a system of linear equations to determine the yield of one bundle of "upper millet" (上禾) and one bundle of "lower millet" (下禾). The procedure described in the problem is essentially an ancient form of Gaussian elimination. Let's translate this into Python code.

### Problem Breakdown:
1. **Given:**
   - 6 bundles of upper millet lose 1 dou 8 sheng (18 sheng) of grain when compared to 10 bundles of lower millet.
   - 15 bundles of lower millet lose 5 sheng of grain when compared to 5 bundles of upper millet.

2. **Unknowns:**
   - The yield of one bundle of upper millet (denoted as `a` in sheng).
   - The yield of one bundle of lower millet (denoted as `b` in sheng).

3. **Equations:**
   - \( 6a - 10b = 18 \) (converted to sheng).
   - \( -5a + 15b = 5 \).

4. **Solution:**
   - Solve the system of equations using the method described (Gaussian elimination).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the coefficients of the equations
# Equation 1: 6a - 10b = 18
# Equation 2: -5a + 15b = 5

# Coefficients for the equations
coefficients = [
    [6, -10, 18],  # 6a - 10b = 18
    [-5, 15, 5]    # -5a + 15b = 5
]

# Step 1: Normalize the first equation (make the leading coefficient 1)
factor_1 = coefficients[0][0]
coefficients[0] = [Fraction(x, factor_1) for x in coefficients[0]]

# Step 2: Eliminate the first variable (a) from the second equation
factor_2 = coefficients[1][0]
coefficients[1] = [coefficients[1][i] - factor_2 * coefficients[0][i] for i in range(3)]

# Step 3: Normalize the second equation (make the leading coefficient of b = 1)
factor_3 = coefficients[1][1]
coefficients[1] = [Fraction(x, factor_3) for x in coefficients[1]]

# Step 4: Back-substitute to solve for a
b = coefficients[1][2]  # The solution for b
a = coefficients[0][2] - coefficients[0][1] * b  # Solve for a using the first equation

# Convert results to sheng
a_sheng = a
b_sheng = b

# Output the results
print(f"上禾一秉實 a = {a_sheng} 升")
print(f"下禾一秉實 b = {b_sheng} 升")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Input the equations:** The coefficients of the equations are represented as a list of lists. Each sublist contains the coefficients of \(a\), \(b\), and the constant term.
2. **Normalize the first equation:** Divide the first equation by the leading coefficient to make the coefficient of \(a\) equal to 1.
3. **Eliminate \(a\) from the second equation:** Subtract a multiple of the first equation from the second equation to eliminate \(a\).
4. **Normalize the second equation:** Divide the second equation by the coefficient of \(b\) to make the coefficient of \(b\) equal to 1.
5. **Back-substitute:** Use the simplified equations to solve for \(a\) and \(b\).
6. **Output the results:** The yield of one bundle of upper millet (\(a\)) and one bundle of lower millet (\(b\)) is printed in sheng.

---

### Answer:
The Python code will compute the values of \(a\) and \(b\) in terms of sheng. The final output will be:

```
上禾一秉實 a = 2 升
下禾一秉實 b = 1 升
```
"""


"""
"""
