"""
今有雉、兔同籠，上有三十五頭，下有九十四足。問：雉、兔各幾何？
術曰：上置三十五頭，下置九十四足。半其足，得四十七，以少減多，再命之，上三除下三，上五除下五，下有一除上一，下有二除上二，即得。
答曰：雉 a ，兔 b 。
"""

"""
This is a classic problem known as the "chicken and rabbit problem" (雉兔同籠). Let's solve it step by step in Python using the provided method.

### Problem Breakdown:
- Let `a` be the number of chickens (雉), and `b` be the number of rabbits (兔).
- Chickens have 2 legs each, and rabbits have 4 legs each.
- There are 35 heads in total (chickens + rabbits), so \( a + b = 35 \).
- There are 94 legs in total, so \( 2a + 4b = 94 \).

We can solve this system of equations to find `a` and `b`.

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Total heads and legs
heads = 35
legs = 94

# Solve for a (chickens) and b (rabbits)
# Using the equations:
# a + b = heads
# 2a + 4b = legs

# Step 1: Simplify the second equation by dividing through by 2
# a + 2b = 47

# Step 2: Subtract the first equation from the simplified second equation
# (a + 2b) - (a + b) = 47 - 35
# b = 12

# Step 3: Substitute b = 12 into the first equation
# a + 12 = 35
# a = 23

# Assign the solutions
a = 23  # Number of chickens
b = 12  # Number of rabbits
#----- content ends here -----


"""


### Solution:
- \( a = 23 \) (Number of chickens)
- \( b = 12 \) (Number of rabbits)
"""


"""
"""
