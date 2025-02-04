"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
This problem is a classic system of linear equations problem, where the prices of sheep (羊), dogs (犬), chickens (雞), and rabbits (兔) are unknown. The problem provides four equations based on the total cost of combinations of these animals. We will solve it using Python and linear algebra.

Here is the Python implementation:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define the variables for the prices of sheep, dogs, chickens, and rabbits
羊, 犬, 雞, 兔 = symbols('羊 犬 雞 兔')

# Define the equations based on the problem
eq1 = Eq(5 * 羊 + 4 * 犬 + 3 * 雞 + 2 * 兔, 1496)
eq2 = Eq(4 * 羊 + 2 * 犬 + 6 * 雞 + 3 * 兔, 1175)
eq3 = Eq(3 * 羊 + 1 * 犬 + 7 * 雞 + 5 * 兔, 958)
eq4 = Eq(2 * 羊 + 3 * 犬 + 5 * 雞 + 1 * 兔, 861)

# Solve the system of equations
solution = solve((eq1, eq2, eq3, eq4), (羊, 犬, 雞, 兔))

# Extract the solutions
a = solution[羊]
b = solution[犬]
c = solution[雞]
d = solution[兔]

# Print the results
print(f"羊價 a = {a}")
print(f"犬價 b = {b}")
print(f"雞價 c = {c}")
print(f"兔價 d = {d}")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Define Variables**: We use `sympy.symbols` to define the unknowns: 羊 (sheep price), 犬 (dog price), 雞 (chicken price), and 兔 (rabbit price).
2. **Define Equations**: The problem provides four equations based on the total cost of combinations of animals. These equations are encoded using `sympy.Eq`.
3. **Solve the System**: We use `sympy.solve` to solve the system of linear equations.
4. **Output the Results**: The solution is printed for each variable.

### Expected Output:
The solution will provide the prices of sheep, dogs, chickens, and rabbits in terms of currency (錢). For example:
```
羊價 a = 123
犬價 b = 234
雞價 c = 45
兔價 d = 67
```

This approach uses modern linear algebra techniques to solve the ancient Chinese problem systematically.
"""


"""
"""
