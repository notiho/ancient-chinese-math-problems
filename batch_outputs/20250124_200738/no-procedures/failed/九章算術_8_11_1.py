"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
This is a classic problem involving the distribution of work (or force) among different types of horses (Wu, Zhong, and Xia horses). Let's solve it step by step.

### Problem Breakdown:
1. A Wu horse, a Zhong horse, and a Xia horse are tasked with carrying 40 shi each but cannot do so individually.
2. They borrow help from each other:
   - The Wu horse borrows one Zhong horse.
   - The Zhong horse borrows one Xia horse.
   - The Xia horse borrows one Wu horse.
3. After borrowing, they are all able to carry their loads up the slope.
4. The question asks: How much force (in shi) can each type of horse pull individually?

### Solution:
Let the force (or pulling capacity) of:
- A Wu horse = `a` shi,
- A Zhong horse = `b` shi,
- A Xia horse = `c` shi.

From the problem, we can derive the following equations:
1. When the Wu horse borrows a Zhong horse, they together can pull 40 shi:
   \[
   a + b = 40
   \]
2. When the Zhong horse borrows a Xia horse, they together can pull 40 shi:
   \[
   b + c = 40
   \]
3. When the Xia horse borrows a Wu horse, they together can pull 40 shi:
   \[
   c + a = 40
   \]

We now solve these equations to find the values of `a`, `b`, and `c`.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations
# a + b = 40
# b + c = 40
# c + a = 40

# Solve for a, b, and c
a = Fraction(40 - 40 + 40, 2)  # Wu horse's pulling capacity
b = Fraction(40 - a)          # Zhong horse's pulling capacity
c = Fraction(40 - b)          # Xia horse's pulling capacity

# Output the results
a, b, c
#----- content ends here -----


"""


---

### Explanation of the Solution:
1. From the three equations:
   \[
   a + b = 40, \quad b + c = 40, \quad c + a = 40
   \]
   Adding all three equations together:
   \[
   (a + b) + (b + c) + (c + a) = 120
   \]
   Simplify:
   \[
   2a + 2b + 2c = 120
   \]
   Divide by 2:
   \[
   a + b + c = 60
   \]
2. Using \( a + b = 40 \), substitute \( b = 40 - a \) into \( a + b + c = 60 \):
   \[
   a + (40 - a) + c = 60
   \]
   Simplify:
   \[
   40 + c = 60
   \]
   Solve for \( c \):
   \[
   c = 20
   \]
3. Substitute \( c = 20 \) into \( b + c = 40 \):
   \[
   b + 20 = 40
   \]
   Solve for \( b \):
   \[
   b = 20
   \]
4. Substitute \( b = 20 \) into \( a + b = 40 \):
   \[
   a + 20 = 40
   \]
   Solve for \( a \):
   \[
   a = 20
   \]

---

### Final Answer:
- Wu horse's pulling capacity (\(a\)) = 20 shi,
- Zhong horse's pulling capacity (\(b\)) = 20 shi,
- Xia horse's pulling capacity (\(c\)) = 20 shi.
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
