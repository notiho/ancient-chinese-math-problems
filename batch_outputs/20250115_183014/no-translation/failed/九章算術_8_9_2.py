"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code. The problem involves solving a system of equations based on the given conditions. Let's proceed step by step.

---

### Problem Setup:
1. Let `甲` have `x` money and `乙` have `y` money.
2. From the problem:
   - If 甲 gets half of 乙's money, 甲 will have 50.
   - If 乙 gets more than half of 甲's money, 乙 will also have 50.

This translates into the following equations:
1. \( x + \frac{y}{2} = 50 \)
2. \( y + \frac{3x}{2} = 50 \)

We will solve this system of equations using the ancient Chinese method described.

---

### Python Code:


"""


from fractions import Fraction

# Define the equations:
# Equation 1: x + y/2 = 50
# Equation 2: y + 3x/2 = 50

# Step 1: Represent the coefficients of the equations
# Coefficients for Equation 1: x + y/2 = 50
a1 = 1  # Coefficient of x in Equation 1
b1 = Fraction(1, 2)  # Coefficient of y in Equation 1
c1 = 50  # Constant term in Equation 1

# Coefficients for Equation 2: y + 3x/2 = 50
a2 = Fraction(3, 2)  # Coefficient of x in Equation 2
b2 = 1  # Coefficient of y in Equation 2
c2 = 50  # Constant term in Equation 2

# Step 2: Eliminate one variable (using ancient method of elimination)
# Multiply Equation 1 by 2 to eliminate fractions
a1 = a1 * 2
b1 = b1 * 2
c1 = c1 * 2

# Now Equation 1 becomes: 2x + y = 100
# Equation 2 remains: (3/2)x + y = 50

# Subtract Equation 2 from Equation 1 to eliminate y
# (2x + y) - ((3/2)x + y) = 100 - 50
eliminated_x = a1 - a2  # Coefficient of x after elimination
eliminated_c = c1 - c2  # Constant term after elimination

# Solve for x
x = Fraction(eliminated_c, eliminated_x)

# Step 3: Substitute x back into one of the original equations to solve for y
# Using Equation 1: 2x + y = 100
y = c1 - (a1 * x)

# Step 4: Results
a = x  # 甲's money
b = y  # 乙's money

# Output the results
a, b


"""


---

### Explanation of the Code:
1. The equations are represented with coefficients for \(x\) and \(y\), and the constant terms.
2. The first equation is multiplied by 2 to eliminate fractions.
3. The ancient method of elimination is used to subtract one equation from the other, eliminating \(y\) and solving for \(x\).
4. The value of \(x\) is substituted back into one of the original equations to solve for \(y\).
5. The results are stored in `a` (甲's money) and `b` (乙's money).

---

### Final Answer:
The values of `a` (甲's money) and `b` (乙's money) will be computed by the code.
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: -100"""
