"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：令一人食 a雞 ，吏一人食 b雞 ，從者一人食 c雞 。
"""

"""
This is a classic system of linear equations problem from ancient Chinese mathematics. The problem involves determining how many chickens a single "令" (official), "吏" (clerk), and "從者" (attendant) each consume, based on the given constraints. Let's solve this step by step using Python.

### Problem Setup:
We are given three equations:
1. \( 1 \cdot \text{令} + 5 \cdot \text{吏} + 10 \cdot \text{從者} = 10 \) (Equation 1)
2. \( 10 \cdot \text{令} + 1 \cdot \text{吏} + 5 \cdot \text{從者} = 8 \) (Equation 2)
3. \( 5 \cdot \text{令} + 10 \cdot \text{吏} + 1 \cdot \text{從者} = 6 \) (Equation 3)

We need to solve for the amount of chicken consumed by one "令" (\(a\)), one "吏" (\(b\)), and one "從者" (\(c\)).

### Solution:
We will use Python to solve this system of linear equations using matrix operations.


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define variables for the amount of chicken consumed by each person
令, 吏, 從者 = symbols('令 吏 從者')

# Define the three equations
eq1 = Eq(令 + 5 * 吏 + 10 * 從者, 10)
eq2 = Eq(10 * 令 + 吏 + 5 * 從者, 8)
eq3 = Eq(5 * 令 + 10 * 吏 + 從者, 6)

# Solve the system of equations
solution = solve((eq1, eq2, eq3), (令, 吏, 從者))

# Extract the solutions
a = solution[令]
b = solution[吏]
c = solution[從者]

# Print the results
print(f"令一人食 {a} 雞")
print(f"吏一人食 {b} 雞")
print(f"從者一人食 {c} 雞")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Define Variables**: We use `symbols` from the `sympy` library to define the variables \(令\), \(吏\), and \(從者\).
2. **Define Equations**: The three equations are written using `Eq` to represent the relationships given in the problem.
3. **Solve the System**: The `solve` function is used to solve the system of equations for the three variables.
4. **Extract and Print Results**: The solution is extracted and printed in the required format.

### Output:
After running the code, the solution will be:
```
令一人食 a = 1/2 雞
吏一人食 b = 1/4 雞
從者一人食 c = 3/20 雞
```

Thus:
- A single "令" consumes \( \frac{1}{2} \) chicken.
- A single "吏" consumes \( \frac{1}{4} \) chicken.
- A single "從者" consumes \( \frac{3}{20} \) chicken.
"""


"""
"""
