"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
To solve this problem using the described "方程術" (system of equations method), we will translate the procedure into Python code step by step. The problem involves solving a system of linear equations to determine the pulling power of each type of horse.

---

### Problem Setup:
- **武馬 (W)**: 1 horse
- **中馬 (M)**: 2 horses
- **下馬 (L)**: 3 horses
- Each horse initially cannot pull 40 石 (units of weight) up the slope.
- Borrowing scenario:
  - 武馬 borrows 1 中馬.
  - 中馬 borrows 1 下馬.
  - 下馬 borrows 1 武馬.
- After borrowing, all horses can pull the load.

We need to determine the pulling power of each type of horse.

---

### Procedure:
The described "方程術" corresponds to solving a system of equations. Let:
- \( W \): Pulling power of 武馬.
- \( M \): Pulling power of 中馬.
- \( L \): Pulling power of 下馬.

The equations are derived as follows:
1. 武馬 + 中馬 = 40
2. 2 中馬 + 下馬 = 40
3. 3 下馬 + 武馬 = 40

We solve this system of equations step by step.

---

### Python Code:


"""


from fractions import Fraction

# Step 1: Define the equations
# 武馬 + 中馬 = 40
# 2 中馬 + 下馬 = 40
# 3 下馬 + 武馬 = 40

# Step 2: Express the equations in terms of coefficients and constants
# Coefficients matrix:
# [ 1  1  0 ]   [ W ]   [ 40 ]
# [ 0  2  1 ] * [ M ] = [ 40 ]
# [ 1  0  3 ]   [ L ]   [ 40 ]

# Constants
C1 = 40
C2 = 40
C3 = 40

# Step 3: Solve using substitution/elimination
# From equation 1: W + M = 40 -> W = 40 - M
# Substitute W into equation 3: (40 - M) + 3L = 40 -> 3L - M = 0 -> M = 3L
# Substitute M = 3L into equation 2: 2(3L) + L = 40 -> 6L + L = 40 -> 7L = 40 -> L = 40 / 7

L = Fraction(40, 7)  # 下馬 pulling power
M = 3 * L            # 中馬 pulling power
W = 40 - M           # 武馬 pulling power

# Results
a = W  # 武馬 pulling power
b = M  # 中馬 pulling power
c = L  # 下馬 pulling power

# Output results
a, b, c


"""


---

### Explanation of the Code:
1. We start by defining the equations based on the problem description.
2. Using substitution and elimination, we solve for \( L \), \( M \), and \( W \) step by step.
3. The results are expressed as fractions to maintain precision.

---

### Final Answer:
- 武馬 (W): \( a = \frac{160}{7} \) 石
- 中馬 (M): \( b = \frac{120}{7} \) 石
- 下馬 (L): \( c = \frac{40}{7} \) 石
"""


"""
"""
