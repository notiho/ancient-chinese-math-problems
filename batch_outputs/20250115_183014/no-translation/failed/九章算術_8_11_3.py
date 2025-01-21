"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：武馬 a匹 力引 b石 ，中馬 c匹 力引 d石 ，下馬 e匹 力引 f石 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method described in the "方程術" (method of equations). Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# 武馬、中馬、下馬的秉數 (coefficients in the equations)
武馬秉數 = [3, -1, 1]  # 武馬借中馬一匹，借下馬一匹
中馬秉數 = [-1, 2, -1]  # 中馬借武馬一匹，借下馬一匹
下馬秉數 = [1, -1, 1]   # 下馬借武馬一匹，借中馬一匹

# 實數 (total load each type of horse must carry)
實數 = [39, 39, 39]  # 39斗 (equivalent to 40石 minus 1石 for borrowing)

# Step 1: Normalize the 武馬 row (武馬秉數)
武馬法 = 武馬秉數[0]
武馬秉數 = [Fraction(x, 武馬法) for x in 武馬秉數]
實數[0] = Fraction(實數[0], 武馬法)

# Step 2: Eliminate 武馬 from 中馬 and 下馬 rows
中馬秉數 = [中馬秉數[i] - 武馬秉數[i] * 中馬秉數[0] for i in range(3)]
實數[1] = 實數[1] - 武馬秉數[0] * 實數[1]

下馬秉數 = [下馬秉數[i] - 武馬秉數[i] * 下馬秉數[0] for i in range(3)]
實數[2] = 實數[2] - 武馬秉數[0] * 實數[2]

# Step 3: Normalize the 中馬 row (中馬秉數)
中馬法 = 中馬秉數[1]
中馬秉數 = [Fraction(x, 中馬法) for x in 中馬秉數]
實數[1] = Fraction(實數[1], 中馬法)

# Step 4: Eliminate 中馬 from 下馬 row
下馬秉數 = [下馬秉數[i] - 中馬秉數[i] * 下馬秉數[1] for i in range(3)]
實數[2] = 實數[2] - 中馬秉數[1] * 實數[2]

# Step 5: Solve for 下馬
下馬法 = 下馬秉數[2]
下馬實 = Fraction(實數[2], 下馬法)

# Step 6: Solve for 中馬
中馬實 = 實數[1] - 中馬秉數[2] * 下馬實

# Step 7: Solve for 武馬
武馬實 = 實數[0] - 武馬秉數[2] * 下馬實 - 武馬秉數[1] * 中馬實

# Results
a = 1  # 武馬一匹
b = 武馬實  # 武馬力引
c = 1  # 中馬一匹
d = 中馬實  # 中馬力引
e = 1  # 下馬一匹
f = 下馬實  # 下馬力引

# Output the results
print(f"武馬 {a}匹 力引 {b}石")
print(f"中馬 {c}匹 力引 {d}石")
print(f"下馬 {e}匹 力引 {f}石")


"""


### Explanation of the Code:
1. **Initialization**: The coefficients of the equations (秉數) and the total load (實數) are set up based on the problem description.
2. **Normalization**: Each row is normalized by dividing through by the leading coefficient (法).
3. **Elimination**: The leading variable in each row is eliminated from the rows below it.
4. **Back Substitution**: The values of the variables (實) are calculated starting from the last row and working upwards.
5. **Results**: The calculated values for the pulling capacity of 武馬, 中馬, and 下馬 are output.

This follows the ancient Chinese method of solving simultaneous linear equations step by step.
"""


"""
Variable 'b' has wrong value. Expected: 160/7, Actual: 13
Variable 'd' has wrong value. Expected: 120/7, Actual: 0
Variable 'f' has wrong value. Expected: 40/7, Actual: 0"""
