"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
荅曰：武馬 a匹 力引 b石 ，中馬 c匹 力引 d石 ，下馬 e匹 力引 f石 。
"""

"""
This is a classic ancient Chinese math problem involving horses of different strengths sharing loads to climb a slope. Let's solve it step by step.

### Problem Breakdown:
1. There are three types of horses:
   - Wu horse (武馬): 1 horse
   - Zhong horse (中馬): 2 horses
   - Xia horse (下馬): 3 horses
2. Each horse is tasked with carrying **40 shi** of load up a slope, but none can do it alone.
3. They borrow strength from each other:
   - Wu horse borrows 1 Zhong horse.
   - Zhong horse borrows 1 Xia horse.
   - Xia horse borrows 1 Wu horse.
4. After borrowing, all horses are able to climb the slope.
5. The question asks for the pulling strength of each type of horse.

---

### Solution:
Let the pulling strength of:
- Wu horse = `a` shi,
- Zhong horse = `b` shi,
- Xia horse = `c` shi.

#### Step 1: Write equations for each horse's total pulling strength after borrowing.
- Wu horse: \( a + b = 40 \)
- Zhong horse: \( b + c = 40 \)
- Xia horse: \( c + a = 40 \)

#### Step 2: Solve the system of equations.
From the equations:
1. \( a + b = 40 \)  → \( b = 40 - a \),
2. \( b + c = 40 \)  → Substitute \( b = 40 - a \): \( (40 - a) + c = 40 \) → \( c = a \),
3. \( c + a = 40 \)  → Substitute \( c = a \): \( a + a = 40 \) → \( a = 20 \).

Now substitute \( a = 20 \) into the other equations:
- \( b = 40 - a = 40 - 20 = 20 \),
- \( c = a = 20 \).

---

### Final Answer:
Each horse has the same pulling strength:
- Wu horse (武馬): \( a = 20 \) shi,
- Zhong horse (中馬): \( b = 20 \) shi,
- Xia horse (下馬): \( c = 20 \) shi.

---

### Python Code:


"""


from fractions import Fraction

# Define the total load
total_load = 40

# Solve for the pulling strength of each horse
a = Fraction(20)  # Wu horse
b = Fraction(20)  # Zhong horse
c = Fraction(20)  # Xia horse

# Output the results
print(f"武馬 pulling strength: {a} 石")
print(f"中馬 pulling strength: {b} 石")
print(f"下馬 pulling strength: {c} 石")


"""


Output:
```
武馬 pulling strength: 20 石
中馬 pulling strength: 20 石
下馬 pulling strength: 20 石
```
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 20
Variable 'b' has wrong value. Expected: 160/7, Actual: 20
Variable 'c' has wrong value. Expected: 1, Actual: 20
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'"""
