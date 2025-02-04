"""
今有令一人吏五人從者一十人食雞一十令一十人吏一人從者五人食雞八令五人吏一十人從者一人食雞六問令吏從者食雞各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰令一人食 a雞 吏一人食 b雞 從者一人食 c雞 
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of "方程術" (method of solving equations). The problem can be translated into a system of equations based on the given conditions:

1. One "令" (leader), five "吏" (officials), and ten "從者" (followers) eat 10 chickens.
2. Ten "令", one "吏", and five "從者" eat 8 chickens.
3. Five "令", ten "吏", and one "從者" eat 6 chickens.

We need to determine how many chickens each individual (令, 吏, 從者) eats.

The solution involves encoding the procedure described in the "方程術" into Python code.

---

### Step-by-step encoding of the procedure:


"""

#----- content starts here -----

from fractions import Fraction

# Define the coefficients and constants of the equations
# Equation 1: 1令 + 5吏 + 10從者 = 10
# Equation 2: 10令 + 1吏 + 5從者 = 8
# Equation 3: 5令 + 10吏 + 1從者 = 6

# Coefficients of the equations
coefficients = [
    [1, 5, 10],  # Coefficients for 令, 吏, 從者 in equation 1
    [10, 1, 5],  # Coefficients for 令, 吏, 從者 in equation 2
    [5, 10, 1]   # Coefficients for 令, 吏, 從者 in equation 3
]

# Constants on the right-hand side of the equations
constants = [10, 8, 6]

# Step 1: Normalize the first row (divide by the coefficient of the first variable)
factor = coefficients[0][0]
coefficients[0] = [Fraction(x, factor) for x in coefficients[0]]
constants[0] = Fraction(constants[0], factor)

# Step 2: Eliminate the first variable from the second and third rows
for i in range(1, 3):
    factor = coefficients[i][0]
    coefficients[i] = [coefficients[i][j] - factor * coefficients[0][j] for j in range(3)]
    constants[i] = constants[i] - factor * constants[0]

# Step 3: Normalize the second row (divide by the coefficient of the second variable)
factor = coefficients[1][1]
coefficients[1] = [Fraction(x, factor) for x in coefficients[1]]
constants[1] = Fraction(constants[1], factor)

# Step 4: Eliminate the second variable from the third row
factor = coefficients[2][1]
coefficients[2] = [coefficients[2][j] - factor * coefficients[1][j] for j in range(3)]
constants[2] = constants[2] - factor * constants[1]

# Step 5: Solve for the third variable
c = Fraction(constants[2], coefficients[2][2])

# Step 6: Back-substitute to solve for the second variable
b = constants[1] - coefficients[1][2] * c

# Step 7: Back-substitute to solve for the first variable
a = constants[0] - coefficients[0][1] * b - coefficients[0][2] * c

# Results
print(f"令一人食 {a} 雞")
print(f"吏一人食 {b} 雞")
print(f"從者一人食 {c} 雞")
#----- content ends here -----


"""


---

### Explanation of the Code:

1. **Define the equations**: The coefficients of the variables (令, 吏, 從者) and the constants on the right-hand side are defined based on the problem statement.
2. **Gaussian elimination**: The procedure follows the steps of Gaussian elimination:
   - Normalize the first row.
   - Eliminate the first variable from the subsequent rows.
   - Normalize the second row.
   - Eliminate the second variable from the third row.
   - Solve for the third variable, then back-substitute to find the second and first variables.
3. **Output the results**: The solution gives the number of chickens each individual eats.

---

### Answer:
The output of the code will be:

```
令一人食 a 雞
吏一人食 b 雞
從者一人食 c 雞
```

Where `a`, `b`, and `c` are the respective fractions of chickens each individual eats.
"""


"""
"""
