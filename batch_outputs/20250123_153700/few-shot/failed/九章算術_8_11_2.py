"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method described in the "Nine Chapters on the Mathematical Art" (方程術). Let's translate the problem and solution into Python code.

### Problem Description:
There are three types of horses:
- One Wu horse (武馬),
- Two Zhong horses (中馬),
- Three Xia horses (下馬).

Each horse is tasked with carrying 40 shi (石) of weight up a slope, but none of them can do so alone. To solve the problem, they borrow strength from each other:
- The Wu horse borrows one Zhong horse,
- The Zhong horse borrows one Xia horse,
- The Xia horse borrows one Wu horse.

After borrowing, all horses are able to carry the weight up the slope. The question is: how much pulling force (in shi) does each type of horse have?

### Procedure:
The procedure involves setting up and solving a system of linear equations using the described method. Let's implement this step-by-step in Python.


"""


from fractions import Fraction

# Step 1: Define the borrowing relationships as equations
# Let a = pulling force of Wu horse (武馬)
# Let b = pulling force of Zhong horse (中馬)
# Let c = pulling force of Xia horse (下馬)

# Equation 1: Wu horse + 1 Zhong horse = 40 shi
# a + b = 40

# Equation 2: Zhong horse + 1 Xia horse = 40 shi
# b + c = 40

# Equation 3: Xia horse + 1 Wu horse = 40 shi
# c + a = 40

# Step 2: Solve the system of equations using substitution/elimination
# From Equation 1: b = 40 - a
# Substitute b into Equation 2: (40 - a) + c = 40
# Simplify: c = a
# Substitute c into Equation 3: a + a = 40
# Simplify: 2a = 40
# Solve for a: a = 20

# Step 3: Solve for b and c using the values of a
a = 20  # Pulling force of Wu horse
b = 40 - a  # From Equation 1
c = a  # From the substitution step

# Step 4: Output the results
print(f"武馬一匹力引 {a} 石")  # Wu horse pulling force
print(f"中馬一匹力引 {b} 石")  # Zhong horse pulling force
print(f"下馬一匹力引 {c} 石")  # Xia horse pulling force


"""


### Explanation of the Solution:
1. We set up three equations based on the borrowing relationships:
   - \( a + b = 40 \)
   - \( b + c = 40 \)
   - \( c + a = 40 \)
2. Using substitution, we express \( b \) and \( c \) in terms of \( a \), and solve for \( a \).
3. Once \( a \) is determined, we substitute back to find \( b \) and \( c \).
4. The solution gives the pulling force of each type of horse.

### Answer:
- 武馬一匹力引 \( a = 20 \) 石
- 中馬一匹力引 \( b = 20 \) 石
- 下馬一匹力引 \( c = 20 \) 石
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
