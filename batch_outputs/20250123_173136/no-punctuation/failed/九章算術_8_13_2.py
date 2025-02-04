"""
今有白禾二步青禾三步黃禾四步黑禾五步實各不滿斗白取青黃青取黃黑黃取黑白黑取白青各一步而實滿斗問白青黃黑禾實一步各幾何
術曰如方程各置所取以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰白禾一步實 a斗 青禾一步實 b斗 黃禾一步實 c斗 黑禾一步實 d斗 
"""

"""
This problem involves solving a system of linear equations using ancient Chinese mathematical methods described in the "方程術" (fangcheng method). Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# Given data
# White (白禾), Green (青禾), Yellow (黃禾), Black (黑禾)
# White takes from Green and Yellow, Green takes from Yellow and Black,
# Yellow takes from Black and White, Black takes from White and Green.
# Each contributes 1 bu (步), and the total fills 1 dou (斗).

# Coefficients for the equations
# Each row represents the equation for one type of grain (White, Green, Yellow, Black)
# Each column represents the contribution of White, Green, Yellow, Black respectively
coefficients = [
    [1, -1, -1, 0],  # White takes from Green and Yellow
    [0, 1, -1, -1],  # Green takes from Yellow and Black
    [-1, 0, 1, -1],  # Yellow takes from Black and White
    [-1, -1, 0, 1]   # Black takes from White and Green
]

# The total contribution for each type of grain (1 dou)
totals = [1, 1, 1, 1]

# Solve the system of equations using the fangcheng method
# Step 1: Convert the coefficients into a triangular form
for i in range(len(coefficients)):
    # Normalize the current row
    divisor = coefficients[i][i]
    for j in range(len(coefficients[i])):
        coefficients[i][j] = Fraction(coefficients[i][j], divisor)
    totals[i] = Fraction(totals[i], divisor)
    
    # Eliminate the current variable from the rows below
    for k in range(i + 1, len(coefficients)):
        factor = coefficients[k][i]
        for j in range(len(coefficients[k])):
            coefficients[k][j] -= factor * coefficients[i][j]
        totals[k] -= factor * totals[i]

# Step 2: Back-substitution to solve for each variable
results = [0] * len(totals)
for i in range(len(coefficients) - 1, -1, -1):
    results[i] = totals[i]
    for j in range(i + 1, len(coefficients)):
        results[i] -= coefficients[i][j] * results[j]

# Extract the results
a, b, c, d = results

# Output the results
print(f"白禾一步實 {a}斗")
print(f"青禾一步實 {b}斗")
print(f"黃禾一步實 {c}斗")
print(f"黑禾一步實 {d}斗")


"""


### Explanation of the Code:
1. **Coefficients Matrix**: The coefficients matrix represents the relationships between the grains as described in the problem.
2. **Totals Vector**: The totals vector represents the total contribution of each type of grain (1 dou each).
3. **Fangcheng Method**:
   - The coefficients matrix is converted into an upper triangular form by normalizing each row and eliminating variables from the rows below.
   - Back-substitution is used to solve for each variable (the amount of grain contributed by each type).
4. **Results**: The results are the contributions of White, Green, Yellow, and Black grains, respectively.

### Answer:
The output will be:
```
白禾一步實 a斗
青禾一步實 b斗
黃禾一步實 c斗
黑禾一步實 d斗
```
Where `a`, `b`, `c`, and `d` are the respective contributions of each type of grain in dou.
"""


"""
Variable 'a' has wrong value. Expected: 11/37, Actual: -1
Variable 'b' has wrong value. Expected: 28/111, Actual: -1
Variable 'c' has wrong value. Expected: 17/111, Actual: -1
Variable 'd' has wrong value. Expected: 10/111, Actual: -1"""
