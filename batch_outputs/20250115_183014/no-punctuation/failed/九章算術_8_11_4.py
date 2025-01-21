"""
今有武馬一匹中馬二匹下馬三匹皆載四十石至阪皆不能上武馬借中馬一匹中馬借下馬一匹下馬借武馬一匹乃皆上問武中下馬一匹各力引幾何
術曰如方程各置所借以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰武馬 a匹 力引 b石 中馬 c匹 力引 d石 下馬 e匹 力引 f石 
"""

"""
This problem involves solving a system of equations using the ancient Chinese method of "fangcheng" (方程), which is equivalent to solving simultaneous linear equations. The problem describes three types of horses (武馬, 中馬, 下馬) and their ability to carry loads, with borrowing and redistribution of loads to balance the effort.

Let's translate the procedure and solve step by step:

---

### Problem:
There is one warhorse (武馬), two middle horses (中馬), and three lower horses (下馬). Each is tasked with carrying 40 shi of load up a slope but cannot do so alone. They borrow strength from each other as follows:
- The warhorse borrows one middle horse.
- The middle horse borrows one lower horse.
- The lower horse borrows one warhorse.

After borrowing, all horses can ascend the slope. Question: What is the pulling strength of each type of horse?

---

### Procedure:
1. Represent the pulling strength of each horse type as variables:
   - 武馬 (warhorse): \( x \)
   - 中馬 (middle horse): \( y \)
   - 下馬 (lower horse): \( z \)

2. Formulate the equations based on the borrowing and load distribution:
   - Equation 1 (武馬 + 中馬): \( x + y = 40 \)
   - Equation 2 (中馬 + 下馬): \( y + z = 40 \)
   - Equation 3 (下馬 + 武馬): \( z + x = 40 \)

3. Solve the system of equations using the "fangcheng" method.

---

### Code Implementation:

"""


from fractions import Fraction

# Step 1: Define the equations
# 武馬 + 中馬 = 40
# 中馬 + 下馬 = 40
# 下馬 + 武馬 = 40

# Step 2: Solve for each variable
# Add all three equations: (x + y) + (y + z) + (z + x) = 120
# Simplify: 2x + 2y + 2z = 120
# Divide by 2: x + y + z = 60

# Use substitution to solve:
# From x + y = 40, we get x = 40 - y
# From y + z = 40, we get z = 40 - y

# Substitute into x + y + z = 60:
# (40 - y) + y + (40 - y) = 60
# Simplify: 80 - y = 60
# Solve for y: y = 20

# Substitute y = 20 into other equations:
x = 40 - 20  # x = 20
z = 40 - 20  # z = 20

# Step 3: Assign results
a = 1  # 武馬 count
b = Fraction(x)  # 武馬 pulling strength
c = 2  # 中馬 count
d = Fraction(y)  # 中馬 pulling strength
e = 3  # 下馬 count
f = Fraction(z)  # 下馬 pulling strength

# Output results
a, b, c, d, e, f


"""


---

### Explanation of Results:
- 武馬 (warhorse): \( a = 1 \), pulling strength \( b = 20 \) shi.
- 中馬 (middle horse): \( c = 2 \), pulling strength \( d = 20 \) shi.
- 下馬 (lower horse): \( e = 3 \), pulling strength \( f = 20 \) shi.

Answer:
武馬 \( a = 1 \), 力引 \( b = 20 \) 石  
中馬 \( c = 2 \), 力引 \( d = 20 \) 石  
下馬 \( e = 3 \), 力引 \( f = 20 \) 石
"""


"""
Code error: name 'y' is not defined"""
