"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem involves solving a system of equations to find the price of a horse (`a`) and the price of a cow (`b`). Here's the solution:

### Problem Breakdown:
1. Two horses and one cow cost more than 10,000, equal to the price of half a horse.
   \[
   2a + b = \frac{1}{2}a + 10000
   \]

2. One horse and two cows cost less than 10,000, equal to the price of half a cow.
   \[
   a + 2b = \frac{1}{2}b + 10000
   \]

We will solve these equations for `a` (the price of a horse) and `b` (the price of a cow).

---

### Python Code:

"""


from fractions import Fraction

# Equation 1: 2a + b = (1/2)a + 10000
# Rearrange: (2a - (1/2)a) + b = 10000
# Simplify: (3/2)a + b = 10000
# Final form: (3/2)a + b = 10000

# Equation 2: a + 2b = (1/2)b + 10000
# Rearrange: a + (2b - (1/2)b) = 10000
# Simplify: a + (3/2)b = 10000
# Final form: a + (3/2)b = 10000

# Let us solve these equations:
# (3/2)a + b = 10000  (Equation 1)
# a + (3/2)b = 10000  (Equation 2)

# Step 1: Express b from Equation 1
# b = 10000 - (3/2)a

# Step 2: Substitute b into Equation 2
# a + (3/2)(10000 - (3/2)a) = 10000
# a + (3/2)(10000) - (3/2)(3/2)a = 10000
# a + 15000 - (9/4)a = 10000
# Combine like terms:
# a - (9/4)a = 10000 - 15000
# (-5/4)a = -5000
# a = (-5000) / (-5/4)
# a = 5000 * (4/5)
# a = 4000

# Step 3: Substitute a back into Equation 1 to find b
# (3/2)(4000) + b = 10000
# 6000 + b = 10000
# b = 10000 - 6000
# b = 4000

# Final answers:
a = Fraction(4000)  # Price of a horse
b = Fraction(4000)  # Price of a cow


"""


---

### Explanation of the Code:
1. We start by writing the two equations based on the problem statement.
2. We rearrange the equations to isolate one variable (`b`) in terms of the other (`a`).
3. We substitute the expression for `b` into the second equation to solve for `a`.
4. Once `a` is found, we substitute it back into the first equation to solve for `b`.
5. The solutions are stored in variables `a` and `b` as fractions to maintain precision.

---

### Final Results:
The price of a horse (`a`) is **4000** (in the same units as the problem), and the price of a cow (`b`) is **4000**.
"""


"""
Variable 'a' has wrong value. Expected: 60000/11, Actual: 4000
Variable 'b' has wrong value. Expected: 20000/11, Actual: 4000"""
