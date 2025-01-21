"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves solving a system of linear equations to find the prices of a cow (`a`), a sheep (`b`), and a pig (`c`). Here's the Python code:


"""


from fractions import Fraction

# Equations derived from the problem:
# 2a + 5b - 13c = 1000
# 3a - 9b + 3c = 0
# -5a + 6b + 8c = -600

# Solve the system of equations using substitution and elimination.

# Step 1: Solve for `a` in terms of `b` and `c` from the first equation
# 2a = 1000 - 5b + 13c
# a = (1000 - 5b + 13c) / 2
def solve():
    # Step 2: Substitute `a` into the second and third equations
    # Second equation: 3a - 9b + 3c = 0
    # Third equation: -5a + 6b + 8c = -600

    # Substitute `a` into the second equation:
    # 3((1000 - 5b + 13c) / 2) - 9b + 3c = 0
    # Multiply through by 2 to eliminate the fraction:
    # 3(1000 - 5b + 13c) - 18b + 6c = 0
    # 3000 - 15b + 39c - 18b + 6c = 0
    # -33b + 45c = -3000
    # Simplify:
    eq2 = (-33, 45, -3000)  # Coefficients of b, c, and constant term

    # Substitute `a` into the third equation:
    # -5((1000 - 5b + 13c) / 2) + 6b + 8c = -600
    # Multiply through by 2 to eliminate the fraction:
    # -5(1000 - 5b + 13c) + 12b + 16c = -1200
    # -5000 + 25b - 65c + 12b + 16c = -1200
    # 37b - 49c = 3800
    # Simplify:
    eq3 = (37, -49, 3800)  # Coefficients of b, c, and constant term

    # Step 3: Solve the system of two equations (eq2 and eq3) for `b` and `c`
    # Use elimination to solve for `b` and `c`:
    # eq2: -33b + 45c = -3000
    # eq3:  37b - 49c = 3800

    # Multiply eq2 by 37 and eq3 by 33 to align coefficients of `b`:
    # 37 * eq2: -1221b + 1665c = -111000
    # 33 * eq3:  1221b - 1617c = 125400

    # Add the two equations to eliminate `b`:
    # (1665c - 1617c) = (125400 - 111000)
    # 48c = 14400
    # c = 14400 / 48
    c = Fraction(14400, 48)

    # Substitute `c` back into eq2 to solve for `b`:
    # -33b + 45c = -3000
    # -33b + 45(300) = -3000
    # -33b + 13500 = -3000
    # -33b = -3000 - 13500
    # -33b = -16500
    # b = -16500 / -33
    b = Fraction(-16500, -33)

    # Substitute `b` and `c` back into the first equation to solve for `a`:
    # 2a + 5b - 13c = 1000
    # 2a + 5(500) - 13(300) = 1000
    # 2a + 2500 - 3900 = 1000
    # 2a - 1400 = 1000
    # 2a = 1000 + 1400
    # 2a = 2400
    # a = 2400 / 2
    a = Fraction(2400, 2)

    return a, b, c


a, b, c = solve()

# Output the results
a, b, c


"""


### Explanation of the Code:
1. The problem is translated into three linear equations:
   - \( 2a + 5b - 13c = 1000 \)
   - \( 3a - 9b + 3c = 0 \)
   - \( -5a + 6b + 8c = -600 \)

2. Using substitution and elimination, we solve for \( a \), \( b \), and \( c \) step by step.

3. The `Fraction` class is used to ensure that all calculations are exact and to handle non-integer results.

### Final Answer:
The values of \( a \), \( b \), and \( c \) (prices of a cow, a sheep, and a pig) are stored in the variables `a`, `b`, and `c`.
"""


"""
"""
