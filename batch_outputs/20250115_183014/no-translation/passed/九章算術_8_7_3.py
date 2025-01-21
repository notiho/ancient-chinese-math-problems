"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
To solve this problem, we need to apply the ancient Chinese method of solving simultaneous linear equations, as described in the "方程術" (method of solving equations). The problem involves three unknowns: the price of a cow (`牛價`), the price of a sheep (`羊價`), and the price of a pig (`豕價`). Let's encode the procedure step by step in Python.


"""


from fractions import Fraction

# Define the equations based on the problem:
# 1. 2牛 + 5羊 - 13豕 = 1000
# 2. 3牛 - 9羊 + 3豕 = 0
# 3. -5牛 + 6羊 + 8豕 = -600

# Coefficients of the equations
equation1 = [2, 5, -13, 1000]  # 牛, 羊, 豕, constant
equation2 = [3, -9, 3, 0]      # 牛, 羊, 豕, constant
equation3 = [-5, 6, 8, -600]   # 牛, 羊, 豕, constant

# Step 1: Eliminate the first variable (牛) from equations 2 and 3 using equation 1
factor1 = Fraction(equation2[0], equation1[0])  # factor to eliminate 牛 from equation 2
factor2 = Fraction(equation3[0], equation1[0])  # factor to eliminate 牛 from equation 3

for i in range(4):
    equation2[i] -= factor1 * equation1[i]
    equation3[i] -= factor2 * equation1[i]

# Step 2: Eliminate the second variable (羊) from equation 3 using equation 2
factor3 = Fraction(equation3[1], equation2[1])  # factor to eliminate 羊 from equation 3

for i in range(4):
    equation3[i] -= factor3 * equation2[i]

# Step 3: Solve for 豕 (c) from equation 3
c = Fraction(equation3[3], equation3[2])

# Step 4: Solve for 羊 (b) from equation 2
b = Fraction(equation2[3] - equation2[2] * c, equation2[1])

# Step 5: Solve for 牛 (a) from equation 1
a = Fraction(equation1[3] - equation1[1] * b - equation1[2] * c, equation1[0])

# Results
牛價 = a
羊價 = b
豕價 = c

# Output the results
牛價, 羊價, 豕價


"""


### Explanation of the Code:
1. **Equation Setup**: The three equations are written in the form of coefficients for `牛`, `羊`, `豕`, and the constant term.
2. **Elimination**: The first variable (`牛`) is eliminated from the second and third equations using the first equation. Then, the second variable (`羊`) is eliminated from the third equation using the second equation.
3. **Back Substitution**: The third equation is solved for `豕` (`c`), then the second equation is solved for `羊` (`b`), and finally, the first equation is solved for `牛` (`a`).
4. **Results**: The values of `牛價`, `羊價`, and `豕價` are calculated as fractions to ensure accuracy.

This code follows the ancient Chinese method of solving simultaneous equations step by step, as described in the problem.
"""


"""
"""
