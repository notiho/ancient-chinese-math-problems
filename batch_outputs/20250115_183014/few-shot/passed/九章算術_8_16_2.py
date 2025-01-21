"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
To solve this problem, we need to use a system of linear equations based on the given data. The problem describes four equations with four unknowns (the prices of sheep, dogs, chickens, and rabbits). The solution involves using the method of elimination, as described in the ancient Chinese "方程術" (method of solving systems of equations). Below is the Python implementation:


"""


from fractions import Fraction

# Define the coefficients of the equations
# Each equation is of the form: a * 羊 + b * 犬 + c * 雞 + d * 兔 = value
eq1 = [5, 4, 3, 2, 1496]  # 5羊 + 4犬 + 3雞 + 2兔 = 1496
eq2 = [4, 2, 6, 3, 1175]  # 4羊 + 2犬 + 6雞 + 3兔 = 1175
eq3 = [3, 1, 7, 5, 958]   # 3羊 + 1犬 + 7雞 + 5兔 = 958
eq4 = [2, 3, 5, 1, 861]   # 2羊 + 3犬 + 5雞 + 1兔 = 861

# Step 1: Eliminate one variable (兔) from eq2, eq3, and eq4 using eq1
def eliminate(eq1, eq2, var_index):
    factor = Fraction(eq2[var_index], eq1[var_index])
    return [eq2[i] - factor * eq1[i] for i in range(len(eq1))]

eq2 = eliminate(eq1, eq2, 3)  # Eliminate 兔 from eq2
eq3 = eliminate(eq1, eq3, 3)  # Eliminate 兔 from eq3
eq4 = eliminate(eq1, eq4, 3)  # Eliminate 兔 from eq4

# Step 2: Eliminate another variable (雞) from eq3 and eq4 using eq2
eq3 = eliminate(eq2, eq3, 2)  # Eliminate 雞 from eq3
eq4 = eliminate(eq2, eq4, 2)  # Eliminate 雞 from eq4

# Step 3: Eliminate another variable (犬) from eq4 using eq3
eq4 = eliminate(eq3, eq4, 1)  # Eliminate 犬 from eq4

# Step 4: Solve for the remaining variable (羊) in eq4
羊 = Fraction(eq4[4], eq4[0])

# Step 5: Back-substitute to solve for 犬 in eq3
犬 = Fraction(eq3[4] - eq3[0] * 羊, eq3[1])

# Step 6: Back-substitute to solve for 雞 in eq2
雞 = Fraction(eq2[4] - eq2[0] * 羊 - eq2[1] * 犬, eq2[2])

# Step 7: Back-substitute to solve for 兔 in eq1
兔 = Fraction(eq1[4] - eq1[0] * 羊 - eq1[1] * 犬 - eq1[2] * 雞, eq1[3])

# Final results
a = 羊
b = 犬
c = 雞
d = 兔

print(f"羊價 a = {a}")
print(f"犬價 b = {b}")
print(f"雞價 c = {c}")
print(f"兔價 d = {d}")


"""


### Explanation of the Code:
1. **Input Equations**: The coefficients of the equations are directly taken from the problem statement.
2. **Elimination Process**: The `eliminate` function performs the elimination of a variable by subtracting a scaled version of one equation from another.
3. **Back-Substitution**: After reducing the system to a single variable, we solve for that variable and substitute it back into the previous equations to solve for the remaining variables.
4. **Fraction Handling**: The `Fraction` class is used to ensure exact arithmetic throughout the calculations.

### Output:
The program will output the prices of sheep (`a`), dogs (`b`), chickens (`c`), and rabbits (`d`) in terms of exact fractions or integers.
"""


"""
"""
