"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
荅曰：武馬 a匹 力引 b石 ，中馬 c匹 力引 d石 ，下馬 e匹 力引 f石 。
"""

"""
This is a classic problem involving the distribution of effort among different types of horses (Wu Ma, Zhong Ma, and Xia Ma) to pull loads up a slope. Let's solve it step by step.

### Problem Breakdown:
1. A Wu Ma (武馬) cannot pull 40 shi (石) up the slope alone.
2. A Zhong Ma (中馬) cannot pull 40 shi up the slope alone.
3. A Xia Ma (下馬) cannot pull 40 shi up the slope alone.
4. When:
   - Wu Ma borrows one Zhong Ma,
   - Zhong Ma borrows one Xia Ma,
   - Xia Ma borrows one Wu Ma,
   they can all pull their loads up the slope.

We need to calculate the pulling capacity (力引) of each type of horse.

---

### Solution:
Let:
- \( a \) = pulling capacity of Wu Ma (武馬) in shi,
- \( b \) = pulling capacity of Zhong Ma (中馬) in shi,
- \( c \) = pulling capacity of Xia Ma (下馬) in shi.

From the problem, we can form the following equations:

1. \( a + b \geq 40 \) (Wu Ma and Zhong Ma together can pull 40 shi),
2. \( b + c \geq 40 \) (Zhong Ma and Xia Ma together can pull 40 shi),
3. \( c + a \geq 40 \) (Xia Ma and Wu Ma together can pull 40 shi),
4. \( a < 40 \), \( b < 40 \), \( c < 40 \) (individually, none of them can pull 40 shi).

We solve these equations to find the pulling capacity of each horse.

---

### Python Code:


"""


from fractions import Fraction

# Total load
load = 40

# Let the pulling capacities of Wu Ma, Zhong Ma, and Xia Ma be a, b, and c respectively
# Solve the equations:
# a + b = 40
# b + c = 40
# c + a = 40

# Using algebra:
a = Fraction((load + load - load), 2)  # Wu Ma's pulling capacity
b = Fraction((load + load - load), 2)  # Zhong Ma's pulling capacity
c = Fraction((load + load - load), 2)  # Xia Ma's pulling capacity

# Output results
print(f"Wu Ma (武馬) pulling capacity: {a} 石")
print(f"Zhong Ma (中馬) pulling capacity: {b} 石")
print(f"Xia Ma (下馬) pulling capacity: {c} 石")


"""


---

### Explanation of the Solution:
1. The equations \( a + b = 40 \), \( b + c = 40 \), and \( c + a = 40 \) are derived from the problem's conditions.
2. Solving these equations simultaneously gives the pulling capacities of each type of horse.
3. The solution assumes that the pulling capacities are evenly distributed among the horses.


"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 20
Variable 'b' has wrong value. Expected: 160/7, Actual: 20
Variable 'c' has wrong value. Expected: 1, Actual: 20
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'"""
