"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
To solve this problem, we need to translate the ancient Chinese "方程術" (method of solving simultaneous linear equations) into Python code. The problem involves three equations with three unknowns (牛價, 羊價, 豕價). Let's proceed step by step.

### Problem Setup:
The equations based on the problem are:
1. \( 2x + 5y - 13z = 1000 \)  (牛2, 羊5, 豕13, 餘錢1000)
2. \( 3x - 9y + 3z = 0 \)     (牛3, 羊9, 豕3, 錢適足)
3. \( -5x + 6y + 8z = -600 \) (牛5, 羊6, 豕8, 不足錢600)

Where:
- \( x \): 牛價
- \( y \): 羊價
- \( z \): 豕價

We will use the elimination method as described in the "方程術" to solve these equations.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# Equation 1: 2x + 5y - 13z = 1000
a1, b1, c1, d1 = 2, 5, -13, 1000

# Equation 2: 3x - 9y + 3z = 0
a2, b2, c2, d2 = 3, -9, 3, 0

# Equation 3: -5x + 6y + 8z = -600
a3, b3, c3, d3 = -5, 6, 8, -600

# Step 1: Eliminate x from equations 2 and 3 using equation 1
# Multiply equation 1 by 3 and equation 2 by 2, then subtract
factor1 = 3
factor2 = 2
a1_, b1_, c1_, d1_ = factor1 * a1, factor1 * b1, factor1 * c1, factor1 * d1
a2_, b2_, c2_, d2_ = factor2 * a2, factor2 * b2, factor2 * c2, factor2 * d2

# New equation (eliminating x between eq1 and eq2)
b4 = b2_ - b1_
c4 = c2_ - c1_
d4 = d2_ - d1_

# Multiply equation 1 by 5 and equation 3 by 2, then subtract
factor3 = 5
factor4 = 2
a1__, b1__, c1__, d1__ = factor3 * a1, factor3 * b1, factor3 * c1, factor3 * d1
a3_, b3_, c3_, d3_ = factor4 * a3, factor4 * b3, factor4 * c3, factor4 * d3

# New equation (eliminating x between eq1 and eq3)
b5 = b3_ - b1__
c5 = c3_ - c1__
d5 = d3_ - d1__

# Step 2: Eliminate y from the two new equations
# Multiply the first new equation by b5 and the second new equation by b4, then subtract
factor5 = b5
factor6 = b4
b4_, c4_, d4_ = factor5 * b4, factor5 * c4, factor5 * d4
b5_, c5_, d5_ = factor6 * b5, factor6 * c5, factor6 * d5

# New equation (eliminating y)
c6 = c5_ - c4_
d6 = d5_ - d4_

# Step 3: Solve for z
z = Fraction(d6, c6)

# Step 4: Solve for y using one of the new equations
y = Fraction(d4 - c4 * z, b4)

# Step 5: Solve for x using the original first equation
x = Fraction(d1 - b1 * y - c1 * z, a1)

# Results
a = x  # 牛價
b = y  # 羊價
c = z  # 豕價

# Output the results
a, b, c
#----- content ends here -----


"""


---

### Explanation:
1. **Step 1**: Eliminate \( x \) from the second and third equations using the first equation.
2. **Step 2**: Eliminate \( y \) from the resulting two equations to get a single equation in terms of \( z \).
3. **Step 3**: Solve for \( z \).
4. **Step 4**: Back-substitute \( z \) into one of the equations to solve for \( y \).
5. **Step 5**: Back-substitute \( y \) and \( z \) into the first equation to solve for \( x \).

The results \( a, b, c \) represent the prices of 牛 (x), 羊 (y), and 豕 (z), respectively.
"""


"""
Variable 'a' has wrong value. Expected: 1200, Actual: 800/29
Variable 'b' has wrong value. Expected: 500, Actual: -500/29
Variable 'c' has wrong value. Expected: 300, Actual: -2300/29"""
