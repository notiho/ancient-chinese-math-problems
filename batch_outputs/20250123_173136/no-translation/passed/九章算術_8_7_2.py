"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
To solve this problem, we need to translate the ancient Chinese method of solving simultaneous linear equations (方程術) into Python code. The problem involves three equations with three unknowns (牛價, 羊價, 豕價). Here's the step-by-step solution:


"""


from fractions import Fraction

# Define the coefficients of the equations
# Equation 1: 2牛 + 5羊 - 13豕 = 1000
eq1 = [2, 5, -13, 1000]

# Equation 2: 3牛 - 9羊 + 3豕 = 0
eq2 = [3, -9, 3, 0]

# Equation 3: -5牛 + 6羊 + 8豕 = -600
eq3 = [-5, 6, 8, -600]

# Step 1: Eliminate the first variable (牛) from eq2 and eq3 using eq1
factor2 = Fraction(eq2[0], eq1[0])
factor3 = Fraction(eq3[0], eq1[0])

for i in range(4):
    eq2[i] -= factor2 * eq1[i]
    eq3[i] -= factor3 * eq1[i]

# Step 2: Eliminate the second variable (羊) from eq3 using the updated eq2
factor3 = Fraction(eq3[1], eq2[1])

for i in range(4):
    eq3[i] -= factor3 * eq2[i]

# Step 3: Solve for the third variable (豕價) in eq3
c = Fraction(eq3[3], eq3[2])

# Step 4: Solve for the second variable (羊價) in eq2 using the value of c
b = Fraction(eq2[3] - eq2[2] * c, eq2[1])

# Step 5: Solve for the first variable (牛價) in eq1 using the values of b and c
a = Fraction(eq1[3] - eq1[1] * b - eq1[2] * c, eq1[0])

# Output the results
a, b, c


"""


### Explanation of the Code:
1. **Define the equations**: Each equation is represented as a list of coefficients `[牛, 羊, 豕, constant]`.
2. **Elimination process**: Using the method described in the 方程術, we eliminate variables step by step:
   - First, eliminate 牛 from the second and third equations using the first equation.
   - Then, eliminate 羊 from the third equation using the updated second equation.
3. **Back substitution**: Solve for 豕價 (c) from the third equation, then substitute back to find 羊價 (b) and 牛價 (a).
4. **Fractions**: Use the `Fraction` class to ensure exact arithmetic throughout the calculations.

### Final Answer:
The values of 牛價 (a), 羊價 (b), and 豕價 (c) will be output as fractions for precision.
"""


"""
"""
