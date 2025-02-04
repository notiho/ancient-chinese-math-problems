"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a升 ，下禾一秉實 b升 。
"""

"""
This problem involves solving a system of equations using ancient Chinese methods, specifically the "fangcheng" (方程) method, which is equivalent to solving linear equations. Let's break this down and translate it into Python code.

### Problem Breakdown:
1. **Given:**
   - 6 bundles of upper millet lose 1 dou 8 sheng (18 sheng) when compared to 10 bundles of lower millet.
   - 15 bundles of lower millet lose 5 sheng when compared to 5 bundles of upper millet.

2. **Goal:**
   - Find the actual yield of 1 bundle of upper millet (`a`) and 1 bundle of lower millet (`b`).

3. **Equations:**
   - From the first condition: \( 6a - 10b = 18 \) (in sheng).
   - From the second condition: \( 5a - 15b = 5 \) (in sheng).

4. **Solution Method:**
   - Use the ancient "fangcheng" method, which is equivalent to Gaussian elimination.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Define the coefficients of the equations
# Equation 1: 6a - 10b = 18
# Equation 2: 5a - 15b = 5

# Coefficients for the equations
coefficients = [
    [6, -10, 18],  # 6a - 10b = 18
    [5, -15, 5]    # 5a - 15b = 5
]

# Step 1: Normalize the first row (divide by the leading coefficient of the first row)
factor = coefficients[0][0]
coefficients[0] = [Fraction(x, factor) for x in coefficients[0]]

# Step 2: Eliminate the first variable (a) from the second row
factor = coefficients[1][0] / coefficients[0][0]
coefficients[1] = [
    coefficients[1][i] - factor * coefficients[0][i]
    for i in range(len(coefficients[0]))
]

# Step 3: Solve for b (second variable) from the second row
b = coefficients[1][2] / coefficients[1][1]

# Step 4: Solve for a (first variable) using the first row
a = (coefficients[0][2] - coefficients[0][1] * b) / coefficients[0][0]

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
1. **Input Equations:**
   - The equations are represented as rows in a matrix, where each row contains the coefficients of the variables and the constant term.

2. **Gaussian Elimination:**
   - The first row is normalized by dividing all terms by the leading coefficient.
   - The second row is updated to eliminate the first variable (`a`) by subtracting a multiple of the first row.

3. **Back Substitution:**
   - Solve for `b` using the second row.
   - Substitute `b` into the first row to solve for `a`.

4. **Output:**
   - The results are expressed in terms of `sheng`.

---

### Answer:
The output will provide the values of `a` (yield of 1 bundle of upper millet) and `b` (yield of 1 bundle of lower millet) in `sheng`.
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 11/2
Variable 'b' has wrong value. Expected: 3, Actual: 3/2"""
