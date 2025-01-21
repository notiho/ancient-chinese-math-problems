"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：羊價 a(=177) ，犬價 b(=121) ，雞價 c(=23) ，兔價 d(=29) 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. The problem provides the prices of combinations of animals (sheep, dogs, chickens, and rabbits) and asks for the price of each animal.

### Problem Setup:
We are given four equations:
1. \( 5x + 4y + 3z + 2w = 1496 \)
2. \( 4x + 2y + 6z + 3w = 1175 \)
3. \( 3x + y + 7z + 5w = 958 \)
4. \( 2x + 3y + 5z + w = 861 \)

Where:
- \( x \) is the price of a sheep,
- \( y \) is the price of a dog,
- \( z \) is the price of a chicken,
- \( w \) is the price of a rabbit.

We will solve this system of equations step by step using the elimination method described in the procedure.

---


"""


from fractions import Fraction

# Coefficients of the equations
eq1 = [5, 4, 3, 2, 1496]  # 5x + 4y + 3z + 2w = 1496
eq2 = [4, 2, 6, 3, 1175]  # 4x + 2y + 6z + 3w = 1175
eq3 = [3, 1, 7, 5, 958]   # 3x + y + 7z + 5w = 958
eq4 = [2, 3, 5, 1, 861]   # 2x + 3y + 5z + w = 861

# Step 1: Eliminate x from eq2, eq3, and eq4 using eq1
def eliminate_x(eq1, eq2):
    factor = Fraction(eq2[0], eq1[0])
    return [eq2[i] - factor * eq1[i] for i in range(len(eq1))]

eq2 = eliminate_x(eq1, eq2)  # Eliminate x from eq2
eq3 = eliminate_x(eq1, eq3)  # Eliminate x from eq3
eq4 = eliminate_x(eq1, eq4)  # Eliminate x from eq4

# Step 2: Eliminate y from eq3 and eq4 using the new eq2
def eliminate_y(eq2, eq3):
    factor = Fraction(eq3[1], eq2[1])
    return [eq3[i] - factor * eq2[i] for i in range(len(eq2))]

eq3 = eliminate_y(eq2, eq3)  # Eliminate y from eq3
eq4 = eliminate_y(eq2, eq4)  # Eliminate y from eq4

# Step 3: Eliminate z from eq4 using the new eq3
def eliminate_z(eq3, eq4):
    factor = Fraction(eq4[2], eq3[2])
    return [eq4[i] - factor * eq3[i] for i in range(len(eq3))]

eq4 = eliminate_z(eq3, eq4)  # Eliminate z from eq4

# Step 4: Solve for w in eq4
w = Fraction(eq4[4], eq4[3])

# Step 5: Back-substitute to solve for z in eq3
z = Fraction(eq3[4] - eq3[3] * w, eq3[2])

# Step 6: Back-substitute to solve for y in eq2
y = Fraction(eq2[4] - eq2[3] * w - eq2[2] * z, eq2[1])

# Step 7: Back-substitute to solve for x in eq1
x = Fraction(eq1[4] - eq1[3] * w - eq1[2] * z - eq1[1] * y, eq1[0])

# Convert to integers (since prices are whole numbers)
a = int(x)  # Price of a sheep
b = int(y)  # Price of a dog
c = int(z)  # Price of a chicken
d = int(w)  # Price of a rabbit

# Final results
a, b, c, d  # 177, 121, 23, 29


"""


### Explanation of the Solution:
1. **Elimination of Variables**: The method systematically eliminates variables from the equations, starting with \( x \), then \( y \), and finally \( z \), leaving a single equation to solve for \( w \).
2. **Back-Substitution**: Once \( w \) is found, it is substituted back into the previous equations to solve for \( z \), \( y \), and \( x \) in reverse order.
3. **Final Prices**: The prices of the animals are:
   - Sheep (\( x \)): 177
   - Dog (\( y \)): 121
   - Chicken (\( z \)): 23
   - Rabbit (\( w \)): 29

### Answer:
- Sheep price \( a = 177 \)
- Dog price \( b = 121 \)
- Chicken price \( c = 23 \)
- Rabbit price \( d = 29 \)
"""


"""
"""
