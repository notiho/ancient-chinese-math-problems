"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. The problem is to determine the prices of cows, sheep, and pigs. Let's translate the procedure into Python code step by step.

### Problem Setup
We are given three equations based on the transactions:
1. Selling 2 cows and 5 sheep, buying 13 pigs, and having 1000 leftover money:
   \( 2x + 5y - 13z = 1000 \)
2. Selling 3 cows and 3 pigs, buying 9 sheep, and having no leftover money:
   \( 3x - 9y + 3z = 0 \)
3. Selling 6 sheep and 8 pigs, buying 5 cows, and being short of 600 money:
   \( -5x + 6y + 8z = -600 \)

Here:
- \( x \) is the price of a cow,
- \( y \) is the price of a sheep,
- \( z \) is the price of a pig.

We will solve this system using the described elimination method.

---

### Python Code Implementation


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 2x + 5y - 13z = 1000
eq1 = [2, 5, -13, 1000]

# Equation 2: 3x - 9y + 3z = 0
eq2 = [3, -9, 3, 0]

# Equation 3: -5x + 6y + 8z = -600
eq3 = [-5, 6, 8, -600]

# Step 1: Normalize the first equation (divide by the leading coefficient of x in eq1)
factor1 = eq1[0]
eq1 = [Fraction(term, factor1) for term in eq1]

# Step 2: Eliminate x from eq2 and eq3 using eq1
factor2 = eq2[0]
eq2 = [eq2[i] - factor2 * eq1[i] for i in range(4)]

factor3 = eq3[0]
eq3 = [eq3[i] - factor3 * eq1[i] for i in range(4)]

# Step 3: Normalize the second equation (divide by the leading coefficient of y in eq2)
factor4 = eq2[1]
eq2 = [Fraction(term, factor4) for term in eq2]

# Step 4: Eliminate y from eq3 using eq2
factor5 = eq3[1]
eq3 = [eq3[i] - factor5 * eq2[i] for i in range(4)]

# Step 5: Solve for z in eq3
z = Fraction(eq3[3], eq3[2])

# Step 6: Solve for y in eq2 using the value of z
y = eq2[3] - eq2[2] * z

# Step 7: Solve for x in eq1 using the values of y and z
x = eq1[3] - eq1[1] * y - eq1[2] * z

# Results
a = x  # Price of a cow
b = y  # Price of a sheep
c = z  # Price of a pig

# Output the results
a, b, c


"""


---

### Explanation of the Code
1. **Normalization**: Each equation is normalized by dividing through by the leading coefficient of the variable being eliminated.
2. **Elimination**: Variables are eliminated step by step using subtraction and multiplication, following the ancient Chinese elimination method.
3. **Back Substitution**: Once the last variable is solved, the values are substituted back into the previous equations to solve for the remaining variables.

---

### Final Answer
The prices of the animals are:
- \( a \): Price of a cow,
- \( b \): Price of a sheep,
- \( c \): Price of a pig.

This method ensures the solution adheres to the ancient Chinese elimination procedure.
"""


"""
"""
