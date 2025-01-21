"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
This problem involves solving a system of equations to determine how much money each person,甲 (A) and 乙 (B), holds. The problem can be translated into two equations based on the given conditions:

1. If A takes half of B's money, A will have 50 units of money.
2. If B takes more than half of A's money (specifically, 3/2 of half of A's money), B will also have 50 units of money.

We will solve this system of equations using the method described in the ancient Chinese "fangcheng" (simultaneous equations) procedure.

---

### Problem Setup:
Let:
- `甲 = x` (money held by A)
- `乙 = y` (money held by B)

From the problem:
1. \( x + \frac{1}{2}y = 50 \)
2. \( y + \frac{3}{2}(\frac{1}{2}x) = 50 \)

Simplify the second equation:
\( y + \frac{3}{4}x = 50 \)

We now have the system of equations:
1. \( x + \frac{1}{2}y = 50 \)
2. \( \frac{3}{4}x + y = 50 \)

---

### Fangcheng Procedure:
We will solve this system step by step using the ancient method.


"""


from fractions import Fraction

# Step 1: Define the coefficients of the equations
# Equation 1: x + (1/2)y = 50
a1 = 1  # Coefficient of x in equation 1
b1 = Fraction(1, 2)  # Coefficient of y in equation 1
c1 = 50  # Constant term in equation 1

# Equation 2: (3/4)x + y = 50
a2 = Fraction(3, 4)  # Coefficient of x in equation 2
b2 = 1  # Coefficient of y in equation 2
c2 = 50  # Constant term in equation 2

# Step 2: Eliminate y by aligning coefficients
# Multiply equation 1 by 2 to eliminate the fraction in b1
a1 = a1 * 2
b1 = b1 * 2
c1 = c1 * 2

# Now equation 1 becomes: 2x + y = 100
# Equation 2 remains: (3/4)x + y = 50

# Step 3: Subtract equation 2 from equation 1 to eliminate y
# (2x + y) - ((3/4)x + y) = 100 - 50
x_coefficient = a1 - a2  # Coefficient of x after subtraction
y_coefficient = b1 - b2  # Coefficient of y after subtraction (should be 0)
constant = c1 - c2  # Constant term after subtraction

# Simplify the resulting equation
# (2 - 3/4)x = 50
x_coefficient = x_coefficient  # 2 - 3/4 = 8/4 - 3/4 = 5/4
x = Fraction(constant, x_coefficient)  # x = 50 / (5/4) = 50 * (4/5) = 40

# Step 4: Solve for y using one of the original equations
# Substitute x = 40 into equation 1: 2x + y = 100
y = c1 - (a1 * x)  # y = 100 - 2(40) = 100 - 80 = 20

# Final Answer
a = x  # Money held by A (甲)
b = y  # Money held by B (乙)

print(f"甲持 {a}錢 ，乙持 {b}錢 。")


"""


---

### Final Answer:
甲持 \( a = 40 \) 錢 ，乙持 \( b = 20 \) 錢 。
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 40
Variable 'b' has wrong value. Expected: 25, Actual: 20"""
