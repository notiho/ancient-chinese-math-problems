"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
This problem is a classic system of linear equations problem, where the prices of sheep (羊), dogs (犬), chickens (雞), and rabbits (兔) are unknowns. The problem can be solved using matrix methods or Gaussian elimination, as described in the ancient Chinese "方程術" (method of solving simultaneous equations). Below is the Python implementation of the solution using modern linear algebra techniques.


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define the unknowns
羊價, 犬價, 雞價, 兔價 = symbols('羊價 犬價 雞價 兔價')

# Define the equations based on the problem
eq1 = Eq(5 * 羊價 + 4 * 犬價 + 3 * 雞價 + 2 * 兔價, 1496)
eq2 = Eq(4 * 羊價 + 2 * 犬價 + 6 * 雞價 + 3 * 兔價, 1175)
eq3 = Eq(3 * 羊價 + 1 * 犬價 + 7 * 雞價 + 5 * 兔價, 958)
eq4 = Eq(2 * 羊價 + 3 * 犬價 + 5 * 雞價 + 1 * 兔價, 861)

# Solve the system of equations
solution = solve((eq1, eq2, eq3, eq4), (羊價, 犬價, 雞價, 兔價))

# Extract the results
a = solution[羊價]
b = solution[犬價]
c = solution[雞價]
d = solution[兔價]

# Print the results
print(f"羊價: {a} 錢")
print(f"犬價: {b} 錢")
print(f"雞價: {c} 錢")
print(f"兔價: {d} 錢")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Define Variables**: The prices of sheep, dogs, chickens, and rabbits are represented as `羊價`, `犬價`, `雞價`, and `兔價`.
2. **Set Up Equations**: Each equation corresponds to the total price of a combination of animals, as given in the problem.
3. **Solve the System**: The `solve` function from the `sympy` library is used to solve the system of linear equations.
4. **Output the Results**: The solution is printed, showing the price of each animal.

### Answer:
After running the code, the values of `a`, `b`, `c`, and `d` will represent the prices of sheep, dogs, chickens, and rabbits, respectively.
"""


"""
"""
