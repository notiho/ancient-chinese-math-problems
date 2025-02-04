"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
This is a classic system of linear equations problem. Let's solve it step by step in Python.

### Problem Breakdown:
- Let the price of a cow (牛) be `a`, the price of a sheep (羊) be `b`, and the price of a pig (豕) be `c`.
- From the problem, we have the following equations:
  1. \( 2a + 5b = 13c + 1000 \)
  2. \( 3a + 3c = 9b \)
  3. \( 6b + 8c = 5a - 600 \)

We will solve these equations to find the values of \( a \), \( b \), and \( c \).

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations
# 1. 2a + 5b = 13c + 1000
# Rearrange: 2a + 5b - 13c = 1000
eq1 = lambda a, b, c: 2 * a + 5 * b - 13 * c - 1000

# 2. 3a + 3c = 9b
# Rearrange: 3a - 9b + 3c = 0
eq2 = lambda a, b, c: 3 * a - 9 * b + 3 * c

# 3. 6b + 8c = 5a - 600
# Rearrange: 5a - 6b - 8c = 600
eq3 = lambda a, b, c: 5 * a - 6 * b - 8 * c - 600

# Solve the system of equations manually
# We'll assume some values for one variable and solve for the others iteratively.

# Start with guesses for a, b, c
for a in range(1, 10000):  # Iterate over possible values for a
    for b in range(1, 10000):  # Iterate over possible values for b
        for c in range(1, 10000):  # Iterate over possible values for c
            if eq1(a, b, c) == 0 and eq2(a, b, c) == 0 and eq3(a, b, c) == 0:
                print(f"牛價 a = {a}, 羊價 b = {b}, 豕價 c = {c}")
                break
#----- content ends here -----


"""


### Explanation:
1. We define the three equations based on the problem statement.
2. We iterate over possible integer values for \( a \), \( b \), and \( c \) (prices of cows, sheep, and pigs) to find a solution that satisfies all three equations.
3. When all three equations are satisfied, we print the values of \( a \), \( b \), and \( c \).

This brute-force approach works because the problem likely has integer solutions, and the range of prices is reasonable.
"""


"""
Timed out"""
