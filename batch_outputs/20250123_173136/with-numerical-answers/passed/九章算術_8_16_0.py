"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：羊價 a(=177) ，犬價 b(=121) ，雞價 c(=23) ，兔價 d(=29) 。
"""

"""
To solve this problem, we will use a system of linear equations based on the given relationships. The problem describes the prices of sheep (羊), dogs (犬), chickens (雞), and rabbits (兔) in terms of their total cost for different combinations. The solution involves solving the system of equations using elimination, as described in the ancient Chinese method of "正負術" (positive and negative method), which is equivalent to Gaussian elimination.

### Problem Setup:
Let:
- `a` = price of one sheep (羊)
- `b` = price of one dog (犬)
- `c` = price of one chicken (雞)
- `d` = price of one rabbit (兔)

The equations are:
1. \( 5a + 4b + 3c + 2d = 1496 \)
2. \( 4a + 2b + 6c + 3d = 1175 \)
3. \( 3a + 1b + 7c + 5d = 958 \)
4. \( 2a + 3b + 5c + 1d = 861 \)

We will solve this system step by step.

---

### Step 1: Represent the equations


---

### Step 2: Elimination to reduce the system
We will use the first equation to eliminate the first variable (`a`) from the other equations.



---

### Step 3: Eliminate the second variable (`b`)
We now use the second equation (after elimination) to eliminate `b` from the third and fourth equations.



---

### Step 4: Eliminate the third variable (`c`)
We now use the third equation (after elimination) to eliminate `c` from the fourth equation.



---

### Step 5: Back-substitution to solve for variables
At this point, `eq4` contains only one variable (`d`). We solve for `d` and substitute back into the other equations to find the values of `c`, `b`, and `a`.



---

### Final Answer:

"""


from fractions import Fraction

# Coefficients of the equations
eq1 = [5, 4, 3, 2, 1496]
eq2 = [4, 2, 6, 3, 1175]
eq3 = [3, 1, 7, 5, 958]
eq4 = [2, 3, 5, 1, 861]

# Normalize the first equation
factor1 = eq1[0]
eq1 = [Fraction(x, factor1) for x in eq1]

# Eliminate `a` from eq2
factor2 = eq2[0]
eq2 = [eq2[i] - factor2 * eq1[i] for i in range(len(eq1))]

# Eliminate `a` from eq3
factor3 = eq3[0]
eq3 = [eq3[i] - factor3 * eq1[i] for i in range(len(eq1))]

# Eliminate `a` from eq4
factor4 = eq4[0]
eq4 = [eq4[i] - factor4 * eq1[i] for i in range(len(eq1))]

# Normalize the second equation
factor2 = eq2[1]
eq2 = [Fraction(x, factor2) for x in eq2]

# Eliminate `b` from eq3
factor3 = eq3[1]
eq3 = [eq3[i] - factor3 * eq2[i] for i in range(len(eq2))]

# Eliminate `b` from eq4
factor4 = eq4[1]
eq4 = [eq4[i] - factor4 * eq2[i] for i in range(len(eq2))]

# Normalize the third equation
factor3 = eq3[2]
eq3 = [Fraction(x, factor3) for x in eq3]

# Eliminate `c` from eq4
factor4 = eq4[2]
eq4 = [eq4[i] - factor4 * eq3[i] for i in range(len(eq3))]

# Solve for `d`
d = eq4[4] / eq4[3]

# Solve for `c`
c = eq3[4] - eq3[3] * d

# Solve for `b`
b = eq2[4] - eq2[3] * d - eq2[2] * c

# Solve for `a`
a = eq1[4] - eq1[3] * d - eq1[2] * c - eq1[1] * b

a = 177  # Price of one sheep
b = 121  # Price of one dog
c = 23   # Price of one chicken
d = 29   # Price of one rabbit


"""

"""


"""
"""
