"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：武馬 a匹 力引 b石 ，中馬 c匹 力引 d石 ，下馬 e匹 力引 f石 。
"""

"""
To solve this problem using the described "方程術" (method of equations), we will translate the procedure into Python code step by step. The problem involves solving a system of linear equations to determine the pulling power of 武馬 (strong horse), 中馬 (medium horse), and 下馬 (weak horse).

### Problem Setup:
- 武馬 (strong horse): 1匹
- 中馬 (medium horse): 2匹
- 下馬 (weak horse): 3匹
- Each horse carries 40石 (stones) but cannot ascend the slope alone.
- Borrowing system:
  - 武馬 borrows 1匹 of 中馬.
  - 中馬 borrows 1匹 of 下馬.
  - 下馬 borrows 1匹 of 武馬.
- The goal is to determine the pulling power of each type of horse.

### Procedure:
The "方程術" describes a method to solve a system of linear equations. Let's translate this into Python code.

---


"""


from fractions import Fraction

# Step 1: Define the equations based on the problem description.
# Let x = 武馬 pulling power, y = 中馬 pulling power, z = 下馬 pulling power.
# Each equation corresponds to the borrowing scenario.

# 武馬 + 中馬 = 40石
# 中馬 + 下馬 = 40石
# 下馬 + 武馬 = 40石

# Step 2: Translate the equations into a system of linear equations.
# Equation 1: x + y = 40
# Equation 2: y + z = 40
# Equation 3: z + x = 40

# Step 3: Solve the system of equations using substitution or elimination.
# From Equation 1: y = 40 - x
# Substitute y into Equation 2: (40 - x) + z = 40 -> z = x
# Substitute z into Equation 3: x + x = 40 -> 2x = 40 -> x = 20

# Step 4: Calculate y and z using the values of x.
x = Fraction(20)  # 武馬 pulling power
y = Fraction(40 - x)  # 中馬 pulling power
z = Fraction(x)  # 下馬 pulling power

# Step 5: Output the results.
a = 1  # 武馬匹数
b = x  # 武馬 pulling power
c = 2  # 中馬匹数
d = y  # 中馬 pulling power
e = 3  # 下馬匹数
f = z  # 下馬 pulling power

# Results
print(f"武馬 {a}匹 力引 {b}石")
print(f"中馬 {c}匹 力引 {d}石")
print(f"下馬 {e}匹 力引 {f}石")


"""


### Explanation of the Code:
1. The system of equations is derived from the problem description.
2. The equations are solved step by step using substitution.
3. The results are expressed as fractions to maintain accuracy, as described in the "方程術."
4. The pulling power of each type of horse is calculated and displayed.

### Final Answer:
- 武馬 1匹 力引 20石
- 中馬 2匹 力引 20石
- 下馬 3匹 力引 20石
"""


"""
Variable 'b' has wrong value. Expected: 160/7, Actual: 20
Variable 'c' has wrong value. Expected: 1, Actual: 2
Variable 'd' has wrong value. Expected: 120/7, Actual: 20
Variable 'e' has wrong value. Expected: 1, Actual: 3
Variable 'f' has wrong value. Expected: 40/7, Actual: 20"""
