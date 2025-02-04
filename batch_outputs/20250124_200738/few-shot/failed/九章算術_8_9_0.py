"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
This problem involves solving a system of equations to determine how much money person A (甲) and person B (乙) each hold. The problem is described in terms of a traditional Chinese mathematical method, but we can translate it into a modern algebraic approach using Python.

The problem can be expressed as follows:
1. If A gets half of B's money, A will have 50 units of money.
2. If B gets more than half of A's money (specifically, 3/2 of A's money), B will also have 50 units of money.

We will solve this using Python and fractions to ensure precision.

### Problem Translation into Equations:
Let:
- `甲` (A) = the amount of money A holds.
- `乙` (B) = the amount of money B holds.

From the problem:
1. \( A + \frac{1}{2}B = 50 \)
2. \( B + \frac{3}{2}A = 50 \)

We solve these equations step by step.

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Define the equations:
# A + (1/2)B = 50
# B + (3/2)A = 50

# Let A = 甲, B = 乙
# Rewrite the equations:
# 2A + B = 100  (Multiply the first equation by 2)
# 2B + 3A = 100 (Multiply the second equation by 2)

# Step 1: Solve for B in terms of A using the first equation
# B = 100 - 2A
def solve():
    # Step 2: Substitute B into the second equation
    # 2(100 - 2A) + 3A = 100
    # 200 - 4A + 3A = 100
    # -A = -100
    # A = 100
    甲 = 100

    # Step 3: Solve for B using B = 100 - 2A
    乙 = 100 - 2 * 甲

    return 甲, 乙

# Solve the equations
a, b = solve()

# Output the results
print(f"甲持 {a} 錢 ，乙持 {b} 錢 。")
#----- content ends here -----


"""


### Explanation of the Code:
1. The equations are rewritten to eliminate fractions by multiplying through by 2.
2. The first equation is solved for \( B \) in terms of \( A \).
3. Substituting \( B \) into the second equation allows us to solve for \( A \).
4. Once \( A \) is found, \( B \) is calculated using the first equation.

### Answer:
The solution will output:
```
甲持 100 錢 ，乙持 -100 錢 。
```
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: -100"""
