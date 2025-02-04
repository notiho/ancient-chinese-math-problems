"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：令一人食 a雞 ，吏一人食 b雞 ，從者一人食 c雞 。
"""

"""
This is a classic system of linear equations problem from ancient Chinese mathematics, often solved using a method similar to Gaussian elimination. Let's translate the problem into Python code and solve it step by step.

### Problem Description:
We have three groups of people:
1. **令** (officials),
2. **吏** (clerks),
3. **從者** (attendants).

The groups consume chickens as follows:
1. 1 official, 5 clerks, and 10 attendants eat 10 chickens.
2. 10 officials, 1 clerk, and 5 attendants eat 8 chickens.
3. 5 officials, 10 clerks, and 1 attendant eat 6 chickens.

We are tasked with finding how many chickens each type of person consumes individually.

---

### Solution:
We can represent the problem as a system of linear equations:
1. \( x + 5y + 10z = 10 \)
2. \( 10x + y + 5z = 8 \)
3. \( 5x + 10y + z = 6 \)

Where:
- \( x \) is the number of chickens consumed by one official,
- \( y \) is the number of chickens consumed by one clerk,
- \( z \) is the number of chickens consumed by one attendant.

We solve this system using the method described in the problem, which is essentially Gaussian elimination.

---

### Python Code:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define variables
x, y, z = symbols('x y z')

# Define the equations
eq1 = Eq(x + 5*y + 10*z, 10)  # 1 official, 5 clerks, 10 attendants eat 10 chickens
eq2 = Eq(10*x + y + 5*z, 8)   # 10 officials, 1 clerk, 5 attendants eat 8 chickens
eq3 = Eq(5*x + 10*y + z, 6)   # 5 officials, 10 clerks, 1 attendant eat 6 chickens

# Solve the system of equations
solution = solve((eq1, eq2, eq3), (x, y, z))

# Extract the results
a = solution[x]  # Chickens consumed by one official
b = solution[y]  # Chickens consumed by one clerk
c = solution[z]  # Chickens consumed by one attendant

# Output the results
print(f"令一人食 {a} 雞")  # Chickens consumed by one official
print(f"吏一人食 {b} 雞")  # Chickens consumed by one clerk
print(f"從者一人食 {c} 雞")  # Chickens consumed by one attendant
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Define Variables**: We use `x`, `y`, and `z` to represent the number of chickens consumed by one official, one clerk, and one attendant, respectively.
2. **Define Equations**: The three equations are written based on the problem description.
3. **Solve the System**: Using SymPy's `solve` function, we solve the system of linear equations.
4. **Output the Results**: The solution gives the number of chickens consumed by each type of person.

---

### Answer:
After running the code, the solution will provide the values of \( a \), \( b \), and \( c \), which are the number of chickens consumed by one official, one clerk, and one attendant, respectively.
"""


"""
"""
