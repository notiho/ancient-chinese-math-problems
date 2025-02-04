"""
今有武馬一匹中馬二匹下馬三匹皆載四十石至阪皆不能上武馬借中馬一匹中馬借下馬一匹下馬借武馬一匹乃皆上問武中下馬一匹各力引幾何
術曰如方程各置所借以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰武馬一匹力引 a石 中馬一匹力引 b石 下馬一匹力引 c石 
"""

"""
This is a classic ancient Chinese problem involving a system of linear equations. The problem describes the relative strength of three types of horses (武馬, 中馬, 下馬) in terms of their ability to pull loads. The solution involves using a method similar to Gaussian elimination to solve the system of equations.

Let's translate the problem and solution into Python code step by step:


"""


"""
Suppose there is one warhorse (武馬), two medium horses (中馬), and three lower horses (下馬), each carrying 40 shi of load.
When climbing a slope, none of them can ascend.
The warhorse borrows one medium horse, the medium horse borrows one lower horse, and the lower horse borrows one warhorse.
Then all of them can ascend.
Question: how much pulling force does each type of horse have?

The procedure says: Use the method of equations. Place the borrowed amounts with positive and negative signs into the equations.

The method of equations says:
1. Place the coefficients for the warhorse (3), medium horse (2), and lower horse (1) on the left side.
2. Place the total load (39 dou) on the right side.
3. For the medium horse, subtract the warhorse's contribution.
4. For the lower horse, subtract the medium horse's contribution.
5. Solve step by step using division and substitution.

The answer says: the warhorse pulls *a* shi, the medium horse pulls *b* shi, and the lower horse pulls *c* shi.
"""

from fractions import Fraction

# Step 1: Define the system of equations
# Let x = warhorse's pulling force, y = medium horse's pulling force, z = lower horse's pulling force
# The equations are:
# 3x + 2y + 1z = 39 (total load when all horses work together)
# 2y + 1z = 26 (medium and lower horses' contribution)
# 1z = 13 (lower horse's contribution)

# Step 2: Solve for z (lower horse's pulling force)
z = Fraction(13)  # From the third equation

# Step 3: Solve for y (medium horse's pulling force)
y = Fraction(26) - 1 * z  # Substitute z into the second equation

# Step 4: Solve for x (warhorse's pulling force)
x = Fraction(39) - 2 * y - 1 * z  # Substitute y and z into the first equation

# Final results
a = x  # Warhorse's pulling force
b = y  # Medium horse's pulling force
c = z  # Lower horse's pulling force

# Output the results
a, b, c


"""


### Explanation of the Code:
1. **Equations Setup**:
   - The problem is modeled as a system of linear equations based on the relationships described in the problem.
   - Each equation represents the total pulling force required for the horses to ascend the slope.

2. **Solving Step by Step**:
   - Start by solving for the simplest variable (`z`, the lower horse's pulling force).
   - Substitute `z` into the second equation to solve for `y` (medium horse's pulling force).
   - Substitute both `y` and `z` into the first equation to solve for `x` (warhorse's pulling force).

3. **Use of Fractions**:
   - The `Fraction` class is used to ensure precise arithmetic without floating-point errors.

### Final Answer:
The pulling force of each type of horse is:
- Warhorse (武馬): `a` shi
- Medium horse (中馬): `b` shi
- Lower horse (下馬): `c` shi
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 0
Variable 'b' has wrong value. Expected: 120/7, Actual: 13
Variable 'c' has wrong value. Expected: 40/7, Actual: 13"""
