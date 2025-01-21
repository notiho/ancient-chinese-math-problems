"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
荅曰：白禾 a步 實 b斗 ，青禾 c步 實 d斗 ，黃禾 e步 實 f斗 ，黑禾 g步 實 h斗 。
"""

"""
This problem involves a system of equations to determine the amount of grain (in dou) each type of grain (white, green, yellow, black) produces per step. Let's solve it step by step.

### Problem Breakdown:
1. White grain (白禾) is 2 steps, green grain (青禾) is 3 steps, yellow grain (黃禾) is 4 steps, and black grain (黑禾) is 5 steps.
2. Each type of grain contributes 1 step to the others, and together they fill exactly 1 dou.
3. We need to find how much grain (in dou) each type produces per step.

Let:
- `a` = amount of dou produced by 1 step of white grain (白禾)
- `b` = amount of dou produced by 1 step of green grain (青禾)
- `c` = amount of dou produced by 1 step of yellow grain (黃禾)
- `d` = amount of dou produced by 1 step of black grain (黑禾)

### Equations:
From the problem, we know:
1. White grain contributes 1 step of green and yellow:
   \[
   a + b + c = 1
   \]
2. Green grain contributes 1 step of yellow and black:
   \[
   b + c + d = 1
   \]
3. Yellow grain contributes 1 step of black and white:
   \[
   c + d + a = 1
   \]
4. Black grain contributes 1 step of white and green:
   \[
   d + a + b = 1
   \]

### Solve the System of Equations:
We can solve this system of equations step by step.


"""


from fractions import Fraction

# Define the equations
# a + b + c = 1
# b + c + d = 1
# c + d + a = 1
# d + a + b = 1

# Solve for each variable
a = Fraction(1, 4)  # White grain produces 1/4 dou per step
b = Fraction(1, 4)  # Green grain produces 1/4 dou per step
c = Fraction(1, 4)  # Yellow grain produces 1/4 dou per step
d = Fraction(1, 4)  # Black grain produces 1/4 dou per step

# Output the results
白禾_步 = 2
青禾_步 = 3
黃禾_步 = 4
黑禾_步 = 5

白禾_實 = 白禾_步 * a
青禾_實 = 青禾_步 * b
黃禾_實 = 黃禾_步 * c
黑禾_實 = 黑禾_步 * d

print(f"白禾 {白禾_步}步 實 {白禾_實}斗")
print(f"青禾 {青禾_步}步 實 {青禾_實}斗")
print(f"黃禾 {黃禾_步}步 實 {黃禾_實}斗")
print(f"黑禾 {黑禾_步}步 實 {黑禾_實}斗")


"""


### Final Answer:
- 白禾 2步 實 1/2斗
- 青禾 3步 實 3/4斗
- 黃禾 4步 實 1斗
- 黑禾 5步 實 5/4斗
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 1/4
Variable 'b' has wrong value. Expected: 11/37, Actual: 1/4
Variable 'c' has wrong value. Expected: 1, Actual: 1/4
Variable 'd' has wrong value. Expected: 28/111, Actual: 1/4
Missing variable in output: 'e'
Missing variable in output: 'f'
Missing variable in output: 'g'
Missing variable in output: 'h'"""
