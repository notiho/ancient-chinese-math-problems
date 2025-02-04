"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
This is a classic problem of distributing work among different types of horses based on their strength. Let's solve it step by step.

### Problem Breakdown:
- A Wu horse (武馬) can pull a certain amount of weight.
- A Zhong horse (中馬) can pull a certain amount of weight.
- A Xia horse (下馬) can pull a certain amount of weight.
- Each horse is initially tasked with pulling **40 shi (石)**, but none of them can do it alone.
- To solve this:
  - The Wu horse borrows one Zhong horse.
  - The Zhong horse borrows one Xia horse.
  - The Xia horse borrows one Wu horse.
- After borrowing, all horses are able to pull their loads up the slope.
- We need to calculate the pulling capacity of each type of horse.

---

### Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Let the pulling capacity of Wu horse, Zhong horse, and Xia horse be:
# a, b, and c respectively (in shi).

# Total weight each horse needs to pull:
total_weight = 40

# Equations based on the problem:
# 1. 武馬 (Wu horse) + 中馬 (Zhong horse) = 40
# 2. 中馬 (Zhong horse) + 下馬 (Xia horse) = 40
# 3. 下馬 (Xia horse) + 武馬 (Wu horse) = 40

# Solve the equations:
# From equation 1: a + b = 40
# From equation 2: b + c = 40
# From equation 3: c + a = 40

# Adding all three equations:
# (a + b) + (b + c) + (c + a) = 120
# 2a + 2b + 2c = 120
# a + b + c = 60

# Now solve for individual values:
# From a + b = 40, we get a = 40 - b
# Substitute into a + b + c = 60:
# (40 - b) + b + c = 60
# 40 + c = 60
# c = 20

# Substitute c = 20 into b + c = 40:
# b + 20 = 40
# b = 20

# Substitute b = 20 into a + b = 40:
# a + 20 = 40
# a = 20

# Final results:
a = Fraction(20)  # Wu horse's pulling capacity
b = Fraction(20)  # Zhong horse's pulling capacity
c = Fraction(20)  # Xia horse's pulling capacity

# Output the results
print(f"武馬 (Wu horse) can pull {a} 石.")
print(f"中馬 (Zhong horse) can pull {b} 石.")
print(f"下馬 (Xia horse) can pull {c} 石.")
#----- content ends here -----


"""


---

### Explanation of Results:
- Each type of horse (Wu, Zhong, Xia) can pull **20 shi**.
- This means that the horses are equally strong in this specific problem setup.
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
