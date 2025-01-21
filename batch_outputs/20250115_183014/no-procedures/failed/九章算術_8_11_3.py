"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
荅曰：武馬 a匹 力引 b石 ，中馬 c匹 力引 d石 ，下馬 e匹 力引 f石 。
"""

"""
This is a classic ancient Chinese math problem involving horses of different strengths (Wu horse, Zhong horse, and Xia horse) and their ability to pull loads. Let's solve it step by step.

### Problem Breakdown:
1. A Wu horse (武馬) pulls **40 shi** but cannot climb the slope.
2. A Zhong horse (中馬) pulls **40 shi** but cannot climb the slope.
3. A Xia horse (下馬) pulls **40 shi** but cannot climb the slope.
4. To solve the problem:
   - The Wu horse borrows the strength of 1 Zhong horse.
   - The Zhong horse borrows the strength of 1 Xia horse.
   - The Xia horse borrows the strength of 1 Wu horse.
   - After borrowing, all horses can climb the slope.

We need to calculate the pulling power of each horse (武馬, 中馬, 下馬) in terms of **shi**.

---

### Solution:
Let:
- The pulling power of a Wu horse = `a` shi.
- The pulling power of a Zhong horse = `b` shi.
- The pulling power of a Xia horse = `c` shi.

From the problem, we know:
1. A Wu horse + 1 Zhong horse can pull **40 shi**:  
   **a + b = 40**.

2. A Zhong horse + 1 Xia horse can pull **40 shi**:  
   **b + c = 40**.

3. A Xia horse + 1 Wu horse can pull **40 shi**:  
   **c + a = 40**.

We now solve these equations.

---

### Python Code:


"""


from fractions import Fraction

# Define the equations
# a + b = 40
# b + c = 40
# c + a = 40

# Solve for a, b, c
a = Fraction((40 + 40 - 40), 2)  # a = (40 + 40 - b) / 2
b = Fraction((40 + 40 - 40), 2)  # b = (40 + 40 - c) / 2
c = Fraction((40 + 40 - 40), 2)  # c = (40 + 40 - a) / 2

# Output results
print(f"武馬 pulling power: {a} shi")
print(f"中馬 pulling power: {b} shi")
print(f"下馬 pulling power: {c} shi")


"""


---

### Explanation of the Solution:
1. We solve the system of linear equations:
   - Add all three equations:  
     **(a + b) + (b + c) + (c + a) = 40 + 40 + 40**  
     **2a + 2b + 2c = 120**  
     **a + b + c = 60**.

   - From **a + b = 40**, substitute **b = 40 - a**.
   - From **b + c = 40**, substitute **c = 40 - b**.
   - Solve for **a**, **b**, and **c**.

2. Each horse's pulling power is calculated and expressed as a fraction if necessary.

---

### Final Answer:
- 武馬 (Wu horse) pulling power: **20 shi**.
- 中馬 (Zhong horse) pulling power: **20 shi**.
- 下馬 (Xia horse) pulling power: **20 shi**.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 20
Variable 'b' has wrong value. Expected: 160/7, Actual: 20
Variable 'c' has wrong value. Expected: 1, Actual: 20
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'"""
