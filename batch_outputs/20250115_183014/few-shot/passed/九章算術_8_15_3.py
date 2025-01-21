"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：令 a人 食 b雞 ，吏 c人 食 d雞 ，從者 e人 食 f雞 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, specifically the "fangcheng" (方程) method, which is equivalent to solving simultaneous linear equations. Let's translate the problem into Python step by step.

### Problem Setup
We are given:
1. One "Ling" (令), five "Li" (吏), and ten "Congzhe" (從者) eat 10 chickens.
2. Ten "Ling", one "Li", and five "Congzhe" eat 8 chickens.
3. Five "Ling", ten "Li", and one "Congzhe" eat 6 chickens.

We need to determine how many chickens each type of person eats.

### Procedure
The procedure involves setting up the equations and solving them using elimination, as described in the "fangcheng" method.

### Equations
Let:
- \( x \): the number of chickens eaten by one "Ling" (令),
- \( y \): the number of chickens eaten by one "Li" (吏),
- \( z \): the number of chickens eaten by one "Congzhe" (從者).

The equations are:
1. \( x + 5y + 10z = 10 \)
2. \( 10x + y + 5z = 8 \)
3. \( 5x + 10y + z = 6 \)

We will solve these equations step by step using Python.


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: x + 5y + 10z = 10
eq1 = [1, 5, 10, 10]

# Equation 2: 10x + y + 5z = 8
eq2 = [10, 1, 5, 8]

# Equation 3: 5x + 10y + z = 6
eq3 = [5, 10, 1, 6]

# Step 1: Eliminate x from eq2 and eq3 using eq1
factor1 = Fraction(eq2[0], eq1[0])  # Factor to eliminate x from eq2
factor2 = Fraction(eq3[0], eq1[0])  # Factor to eliminate x from eq3

for i in range(4):
    eq2[i] -= factor1 * eq1[i]
    eq3[i] -= factor2 * eq1[i]

# Step 2: Eliminate y from eq3 using eq2
factor3 = Fraction(eq3[1], eq2[1])  # Factor to eliminate y from eq3

for i in range(4):
    eq3[i] -= factor3 * eq2[i]

# Step 3: Solve for z
z = Fraction(eq3[3], eq3[2])

# Step 4: Solve for y using eq2
y = Fraction(eq2[3] - eq2[2] * z, eq2[1])

# Step 5: Solve for x using eq1
x = Fraction(eq1[3] - eq1[1] * y - eq1[2] * z, eq1[0])

# Results
a = 1  # Number of Ling
b = x  # Chickens eaten by one Ling
c = 1  # Number of Li
d = y  # Chickens eaten by one Li
e = 1  # Number of Congzhe
f = z  # Chickens eaten by one Congzhe

print(f"令 {a}人 食 {b}雞 ，吏 {c}人 食 {d}雞 ，從者 {e}人 食 {f}雞 。")


"""


### Explanation of the Code
1. **Step 1**: Eliminate \( x \) from the second and third equations by subtracting appropriate multiples of the first equation.
2. **Step 2**: Eliminate \( y \) from the third equation by subtracting an appropriate multiple of the modified second equation.
3. **Step 3**: Solve for \( z \) from the simplified third equation.
4. **Step 4**: Substitute \( z \) into the modified second equation to solve for \( y \).
5. **Step 5**: Substitute \( y \) and \( z \) into the first equation to solve for \( x \).

### Output
The program will output the number of chickens eaten by each type of person:
- \( a \): Number of Ling (令),
- \( b \): Chickens eaten by one Ling,
- \( c \): Number of Li (吏),
- \( d \): Chickens eaten by one Li,
- \( e \): Number of Congzhe (從者),
- \( f \): Chickens eaten by one Congzhe.
"""


"""
"""
