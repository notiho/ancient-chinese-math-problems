"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
荅曰：白禾 a步 實 b斗 ，青禾 c步 實 d斗 ，黃禾 e步 實 f斗 ，黑禾 g步 實 h斗 。
"""

"""
This is a classic ancient Chinese math problem involving proportional reasoning and simultaneous equations. Let's break it down and solve it step by step.

---

### Problem Explanation:
We are given:
- White rice (白禾): 2 bu
- Green rice (青禾): 3 bu
- Yellow rice (黃禾): 4 bu
- Black rice (黑禾): 5 bu

Each type of rice contributes a certain amount of volume (in dou) per bu. However, the exact contribution per bu is unknown. Let's denote:
- White rice contributes `a` dou per bu.
- Green rice contributes `c` dou per bu.
- Yellow rice contributes `e` dou per bu.
- Black rice contributes `g` dou per bu.

The problem states:
1. White rice takes 1 bu from Green and Yellow rice, and the total volume becomes 1 dou.
2. Green rice takes 1 bu from Yellow and Black rice, and the total volume becomes 1 dou.
3. Yellow rice takes 1 bu from Black and White rice, and the total volume becomes 1 dou.
4. Black rice takes 1 bu from White and Green rice, and the total volume becomes 1 dou.

We need to determine the contribution per bu for each type of rice (`a`, `c`, `e`, `g`).

---

### Solution:

We can set up the equations based on the problem:

1. White rice:  
   \( 2a + c + e = 1 \)

2. Green rice:  
   \( 3c + e + g = 1 \)

3. Yellow rice:  
   \( 4e + g + a = 1 \)

4. Black rice:  
   \( 5g + a + c = 1 \)

We now solve this system of equations.

---

### Python Code:


"""


from fractions import Fraction

# Solve the system of equations
# 2a + c + e = 1
# 3c + e + g = 1
# 4e + g + a = 1
# 5g + a + c = 1

# Step 1: Express all variables in terms of one (e.g., a)
# From equation 1: c = 1 - 2a - e
# Substitute c into other equations

# Equation 2 becomes:
# 3(1 - 2a - e) + e + g = 1
# 3 - 6a - 3e + e + g = 1
# g = 6a + 2e - 2

# Substitute c and g into equation 3:
# 4e + (6a + 2e - 2) + a = 1
# 4e + 6a + 2e - 2 + a = 1
# 7a + 6e = 3
# e = (3 - 7a) / 6

# Substitute c, g, and e into equation 4:
# 5(6a + 2e - 2) + a + (1 - 2a - e) = 1
# 30a + 10e - 10 + a + 1 - 2a - e = 1
# 29a + 9e = 9
# Substitute e = (3 - 7a) / 6:
# 29a + 9((3 - 7a) / 6) = 9
# 29a + (27 - 63a) / 6 = 9
# (174a + 27 - 63a) / 6 = 9
# (111a + 27) / 6 = 9
# 111a + 27 = 54
# 111a = 27
# a = 27 / 111 = 1 / 4

# Step 2: Solve for other variables
a = Fraction(1, 4)
e = Fraction(3 - 7 * a, 6)
c = Fraction(1 - 2 * a - e)
g = Fraction(6 * a + 2 * e - 2)

# Step 3: Output results
print(f"White rice contributes {a} dou per bu.")
print(f"Green rice contributes {c} dou per bu.")
print(f"Yellow rice contributes {e} dou per bu.")
print(f"Black rice contributes {g} dou per bu.")


"""


---

### Explanation of Results:
The code solves the system of equations step by step using substitution and simplification. The final output will give the contribution of each type of rice (in dou per bu).
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 1/4
Missing variable in output: 'b'
Variable 'c' has wrong value. Expected: 1, Actual: 7/24
Missing variable in output: 'd'
Variable 'e' has wrong value. Expected: 1, Actual: 5/24
Missing variable in output: 'f'
Variable 'g' has wrong value. Expected: 1, Actual: -1/12
Missing variable in output: 'h'"""
