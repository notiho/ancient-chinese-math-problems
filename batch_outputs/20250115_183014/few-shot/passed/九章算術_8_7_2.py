"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. Let's translate the problem into Python code step by step.

### Problem Setup:
We are given three equations based on the transactions:
1. Selling 2 cows and 5 sheep to buy 13 pigs, with 1000 money left over:
   \( 2x + 5y - 13z = 1000 \)
2. Selling 3 cows and 3 pigs to buy 9 sheep, with no money left:
   \( 3x - 9y + 3z = 0 \)
3. Selling 6 sheep and 8 pigs to buy 5 cows, but 600 money is short:
   \( -5x + 6y + 8z = -600 \)

Here, \(x\), \(y\), and \(z\) represent the prices of a cow, a sheep, and a pig, respectively.

We will solve this system of equations using the elimination method described in the problem.

---

### Python Code Implementation:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 2x + 5y - 13z = 1000
eq1 = [2, 5, -13, 1000]

# Equation 2: 3x - 9y + 3z = 0
eq2 = [3, -9, 3, 0]

# Equation 3: -5x + 6y + 8z = -600
eq3 = [-5, 6, 8, -600]

# Step 1: Normalize the first equation (make the first coefficient 1)
factor = eq1[0]
eq1 = [Fraction(term, factor) for term in eq1]

# Step 2: Eliminate the first variable (x) from the other equations
factor = eq2[0]
eq2 = [eq2[i] - factor * eq1[i] for i in range(4)]

factor = eq3[0]
eq3 = [eq3[i] - factor * eq1[i] for i in range(4)]

# Step 3: Normalize the second equation (make the second coefficient 1)
factor = eq2[1]
eq2 = [Fraction(term, factor) for term in eq2]

# Step 4: Eliminate the second variable (y) from the other equations
factor = eq1[1]
eq1 = [eq1[i] - factor * eq2[i] for i in range(4)]

factor = eq3[1]
eq3 = [eq3[i] - factor * eq2[i] for i in range(4)]

# Step 5: Normalize the third equation (make the third coefficient 1)
factor = eq3[2]
eq3 = [Fraction(term, factor) for term in eq3]

# Step 6: Back-substitute to solve for the variables
factor = eq2[2]
eq2 = [eq2[i] - factor * eq3[i] for i in range(4)]

factor = eq1[2]
eq1 = [eq1[i] - factor * eq3[i] for i in range(4)]

factor = eq1[1]
eq1 = [eq1[i] - factor * eq2[i] for i in range(4)]

# The solutions are now in the constants of the equations
a = eq1[3]  # Price of a cow
b = eq2[3]  # Price of a sheep
c = eq3[3]  # Price of a pig

# Output the results
a, b, c


"""


---

### Explanation of the Code:
1. **Equation Setup**: Each equation is represented as a list of coefficients, including the constant term on the right-hand side.
2. **Normalization**: Each equation is normalized by dividing through by the leading coefficient to make it 1.
3. **Elimination**: Variables are eliminated step by step using subtraction and multiplication, following the ancient Chinese elimination method.
4. **Back-Substitution**: After elimination, the values of the variables are determined by substituting back into the equations.

---

### Final Answer:
The values of \(a\), \(b\), and \(c\) represent the prices of a cow, a sheep, and a pig, respectively.
"""


"""
"""
