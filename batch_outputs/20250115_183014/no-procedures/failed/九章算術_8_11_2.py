"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
荅曰：武馬 a匹 力引 b石 ，中馬 c匹 力引 d石 ，下馬 e匹 力引 f石 。
"""

"""
This problem involves determining the pulling power of three types of horses (Wu Ma, Zhong Ma, and Xia Ma) based on their ability to pull loads up a slope. Here's how we can solve it step by step:

### Problem Breakdown:
1. **Given:**
   - Wu Ma (武馬): 1 horse
   - Zhong Ma (中馬): 2 horses
   - Xia Ma (下馬): 3 horses
   - Each horse is initially tasked with pulling **40 shi** of weight, but none can pull the load up the slope.

2. **Borrowing Assistance:**
   - Wu Ma borrows 1 Zhong Ma.
   - Zhong Ma borrows 1 Xia Ma.
   - Xia Ma borrows 1 Wu Ma.
   - After borrowing, all groups are able to pull their loads up the slope.

3. **Question:**
   - What is the pulling power of each type of horse? Specifically:
     - Wu Ma (武馬): *a* horses can pull *b* shi.
     - Zhong Ma (中馬): *c* horses can pull *d* shi.
     - Xia Ma (下馬): *e* horses can pull *f* shi.

---

### Solution:

We need to calculate the pulling power of each type of horse. Let:
- \( x \): Pulling power of 1 Wu Ma (in shi).
- \( y \): Pulling power of 1 Zhong Ma (in shi).
- \( z \): Pulling power of 1 Xia Ma (in shi).

#### Step 1: Write equations based on the problem.

1. **Wu Ma + 1 Zhong Ma:**
   - Wu Ma borrows 1 Zhong Ma, so their combined pulling power is \( x + y \), which must equal 40 shi:
     \[
     x + y = 40
     \]

2. **Zhong Ma + 1 Xia Ma:**
   - Zhong Ma borrows 1 Xia Ma, so their combined pulling power is \( y + z \), which must equal 40 shi:
     \[
     y + z = 40
     \]

3. **Xia Ma + 1 Wu Ma:**
   - Xia Ma borrows 1 Wu Ma, so their combined pulling power is \( z + x \), which must equal 40 shi:
     \[
     z + x = 40
     \]

#### Step 2: Solve the system of equations.

We now have three equations:
1. \( x + y = 40 \)
2. \( y + z = 40 \)
3. \( z + x = 40 \)

Add all three equations together:
\[
(x + y) + (y + z) + (z + x) = 40 + 40 + 40
\]
\[
2x + 2y + 2z = 120
\]
\[
x + y + z = 60
\]

Now subtract each pair of equations to isolate variables:
1. From \( x + y + z = 60 \) and \( x + y = 40 \):
   \[
   z = 60 - 40 = 20
   \]

2. From \( x + y + z = 60 \) and \( y + z = 40 \):
   \[
   x = 60 - 40 = 20
   \]

3. From \( x + y + z = 60 \) and \( z + x = 40 \):
   \[
   y = 60 - 40 = 20
   \]

#### Step 3: Verify the solution.

- \( x = 20 \), \( y = 20 \), \( z = 20 \).
- Substituting back into the original equations:
  - \( x + y = 20 + 20 = 40 \) (correct).
  - \( y + z = 20 + 20 = 40 \) (correct).
  - \( z + x = 20 + 20 = 40 \) (correct).

Thus, the pulling power of each type of horse is:
- Wu Ma: \( 1 \) horse pulls \( 20 \) shi.
- Zhong Ma: \( 1 \) horse pulls \( 20 \) shi.
- Xia Ma: \( 1 \) horse pulls \( 20 \) shi.

---

### Final Answer:
- 武馬 \( a = 1 \), 力引 \( b = 20 \) 石.
- 中馬 \( c = 1 \), 力引 \( d = 20 \) 石.
- 下馬 \( e = 1 \), 力引 \( f = 20 \) 石.

Here is the Python code to represent the solution:


"""


from fractions import Fraction

# Let x, y, z represent the pulling power of Wu Ma, Zhong Ma, and Xia Ma respectively.
# Solve the equations:
# x + y = 40
# y + z = 40
# z + x = 40

# Step 1: Calculate the total pulling power
total_power = 60  # x + y + z = 60

# Step 2: Solve for each variable
x = Fraction(20)  # Wu Ma's pulling power
y = Fraction(20)  # Zhong Ma's pulling power
z = Fraction(20)  # Xia Ma's pulling power

# Output the results
a, b = 1, x  # Wu Ma
c, d = 1, y  # Zhong Ma
e, f = 1, z  # Xia Ma

print(f"武馬 {a}匹 力引 {b}石")
print(f"中馬 {c}匹 力引 {d}石")
print(f"下馬 {e}匹 力引 {f}石")


"""


This will output:
```
武馬 1匹 力引 20石
中馬 1匹 力引 20石
下馬 1匹 力引 20石
```
"""


"""
Variable 'b' has wrong value. Expected: 160/7, Actual: 20
Variable 'd' has wrong value. Expected: 120/7, Actual: 20
Variable 'f' has wrong value. Expected: 40/7, Actual: 20"""
