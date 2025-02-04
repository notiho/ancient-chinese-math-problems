"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
To solve this problem, we will follow the "方程術" (method of equations) as described. The problem can be translated into a system of equations based on the conditions provided:

1. If 甲 gets half of 乙's money, 甲 will have 50 units of money.
2. If 乙 gets more than half of 甲's money, 乙 will also have 50 units of money.

Let 甲's money be \( x \) and 乙's money be \( y \). The equations are:
- \( x + \frac{y}{2} = 50 \)
- \( y + \frac{3x}{2} = 50 \)

We will solve this system of equations step by step using the "方程術".

---

### Step 1: Define the equations


---

### Step 2: Eliminate fractions by multiplying through by 2


---

### Step 3: Solve the system of equations

"""

#----- content starts here -----

from fractions import Fraction

# Let 甲's money be x and 乙's money be y
# Equation 1: x + y/2 = 50
# Equation 2: y + 3x/2 = 50

# Multiply both equations by 2 to eliminate fractions
# Equation 1 becomes: 2x + y = 100
# Equation 2 becomes: 2y + 3x = 100

# Rearrange Equation 1: y = 100 - 2x
# Substitute y into Equation 2: 2(100 - 2x) + 3x = 100
# Simplify: 200 - 4x + 3x = 100
# Combine terms: -x = -100
x = 100

# Substitute x back into Equation 1 to find y
y = 100 - 2 * x
y = 100 - 2 * 100
#----- content ends here -----


"""



"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
