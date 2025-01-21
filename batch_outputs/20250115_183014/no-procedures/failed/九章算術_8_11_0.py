"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
荅曰：武馬 a匹 力引 b石 ，中馬 c匹 力引 d石 ，下馬 e匹 力引 f石 。
"""

"""
This is a classic ancient Chinese math problem involving the distribution of effort among different types of horses (strong, medium, and weak). Let's solve it step by step.

### Problem Breakdown:
- A strong horse (武馬) cannot pull 40 shi (石) alone.
- A medium horse (中馬) cannot pull 40 shi alone.
- A weak horse (下馬) cannot pull 40 shi alone.
- When the strong horse borrows one medium horse, the medium horse borrows one weak horse, and the weak horse borrows one strong horse, they can all pull 40 shi.

We need to calculate how much weight each type of horse can pull individually.

---

### Solution:

Let:
- \( a \) = the number of strong horses (武馬) needed to pull 40 shi.
- \( b \) = the weight (in shi) that one strong horse can pull.
- \( c \) = the number of medium horses (中馬) needed to pull 40 shi.
- \( d \) = the weight (in shi) that one medium horse can pull.
- \( e \) = the number of weak horses (下馬) needed to pull 40 shi.
- \( f \) = the weight (in shi) that one weak horse can pull.

We know:
1. \( a \cdot b = 40 \)
2. \( c \cdot d = 40 \)
3. \( e \cdot f = 40 \)

When the horses borrow each other:
- A strong horse (武馬) borrows one medium horse, so together they can pull 40 shi:
  \( b + d = 40 \)
- A medium horse (中馬) borrows one weak horse, so together they can pull 40 shi:
  \( d + f = 40 \)
- A weak horse (下馬) borrows one strong horse, so together they can pull 40 shi:
  \( f + b = 40 \)

From these equations, we can solve for \( b \), \( d \), and \( f \).

---

### Python Code:


"""


from fractions import Fraction

# Total weight to pull
total_weight = 40

# Equations:
# b + d = 40
# d + f = 40
# f + b = 40

# Solve for b, d, and f
b = Fraction(total_weight - total_weight // 2)  # Weight pulled by one strong horse
d = Fraction(total_weight - b)                 # Weight pulled by one medium horse
f = Fraction(total_weight - d)                 # Weight pulled by one weak horse

# Calculate the number of horses needed for each type
a = Fraction(total_weight, b)  # Number of strong horses needed
c = Fraction(total_weight, d)  # Number of medium horses needed
e = Fraction(total_weight, f)  # Number of weak horses needed

# Results
print(f"Strong horse (武馬): {a} horses, each pulling {b} shi")
print(f"Medium horse (中馬): {c} horses, each pulling {d} shi")
print(f"Weak horse (下馬): {e} horses, each pulling {f} shi")


"""


---

### Explanation of Results:
- \( a \): Number of strong horses needed.
- \( b \): Weight (in shi) that one strong horse can pull.
- \( c \): Number of medium horses needed.
- \( d \): Weight (in shi) that one medium horse can pull.
- \( e \): Number of weak horses needed.
- \( f \): Weight (in shi) that one weak horse can pull.

This code solves the problem using the relationships between the weights and the borrowing conditions.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 2
Variable 'b' has wrong value. Expected: 160/7, Actual: 20
Variable 'c' has wrong value. Expected: 1, Actual: 2
Variable 'd' has wrong value. Expected: 120/7, Actual: 20
Variable 'e' has wrong value. Expected: 1, Actual: 2
Variable 'f' has wrong value. Expected: 40/7, Actual: 20"""
