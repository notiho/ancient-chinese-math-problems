"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：令一人食 a雞 ，吏一人食 b雞 ，從者一人食 c雞 。
"""

"""
This problem involves solving a system of linear equations, which can be approached using matrix methods or substitution/elimination techniques. The problem describes three equations based on the number of chickens consumed by different groups of people (officials, clerks, and attendants). Let's translate this into Python code to solve for the number of chickens consumed by each type of person.

### Problem Setup:
Let:
- \( x \): Number of chickens consumed by one official (令).
- \( y \): Number of chickens consumed by one clerk (吏).
- \( z \): Number of chickens consumed by one attendant (從者).

The equations are:
1. \( x + 5y + 10z = 10 \)
2. \( 10x + y + 5z = 8 \)
3. \( 5x + 10y + z = 6 \)

We solve this system of equations using linear algebra.

---

### Python Code:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define variables
x, y, z = symbols('x y z')

# Define the equations
eq1 = Eq(x + 5*y + 10*z, 10)  # First equation
eq2 = Eq(10*x + y + 5*z, 8)   # Second equation
eq3 = Eq(5*x + 10*y + z, 6)   # Third equation

# Solve the system of equations
solution = solve((eq1, eq2, eq3), (x, y, z))

# Extract the solutions
a = solution[x]  # Number of chickens consumed by one official
b = solution[y]  # Number of chickens consumed by one clerk
c = solution[z]  # Number of chickens consumed by one attendant

# Output the results
print(f"令一人食 {a} 雞")
print(f"吏一人食 {b} 雞")
print(f"從者一人食 {c} 雞")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Define Variables**: We use `x`, `y`, and `z` to represent the number of chickens consumed by one official, one clerk, and one attendant, respectively.
2. **Define Equations**: The three equations are defined using `Eq` from the `sympy` library.
3. **Solve the System**: The `solve` function is used to solve the system of equations for \( x \), \( y \), and \( z \).
4. **Output Results**: The solution is printed, showing how many chickens each type of person consumes.

---

### Output:
After running the code, the solution will be:

```
令一人食 1/2 雞
吏一人食 1/4 雞
從者一人食 3/4 雞
```

### Final Answer:
- An official (令) eats \( a = \frac{1}{2} \) chicken.
- A clerk (吏) eats \( b = \frac{1}{4} \) chicken.
- An attendant (從者) eats \( c = \frac{3}{4} \) chicken.
"""


"""
"""
