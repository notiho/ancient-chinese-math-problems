"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
To solve this problem using the ancient Chinese "方程術" (method of simultaneous equations), we will translate the problem into Python code step by step. The equations are derived from the problem statement:

1. \( 2牛 + 5羊 - 13豕 = 1000 \)  
2. \( 3牛 - 9羊 + 3豕 = 0 \)  
3. \( -5牛 + 6羊 + 8豕 = -600 \)  

We will solve this system of equations using the described "正負術" (positive-negative method), which is essentially Gaussian elimination.


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# 牛, 羊, 豕, constant
equations = [
    [2, 5, -13, 1000],  # Equation 1
    [3, -9, 3, 0],      # Equation 2
    [-5, 6, 8, -600]    # Equation 3
]

# Step 1: Normalize the first equation (make the first coefficient 1)
factor = equations[0][0]
equations[0] = [Fraction(x, factor) for x in equations[0]]

# Step 2: Eliminate the first variable (牛) from the other equations
for i in range(1, 3):
    factor = equations[i][0]
    equations[i] = [equations[i][j] - factor * equations[0][j] for j in range(4)]

# Step 3: Normalize the second equation (make the second coefficient 1)
factor = equations[1][1]
equations[1] = [Fraction(x, factor) for x in equations[1]]

# Step 4: Eliminate the second variable (羊) from the other equations
for i in [0, 2]:
    factor = equations[i][1]
    equations[i] = [equations[i][j] - factor * equations[1][j] for j in range(4)]

# Step 5: Normalize the third equation (make the third coefficient 1)
factor = equations[2][2]
equations[2] = [Fraction(x, factor) for x in equations[2]]

# Step 6: Eliminate the third variable (豕) from the other equations
for i in [0, 1]:
    factor = equations[i][2]
    equations[i] = [equations[i][j] - factor * equations[2][j] for j in range(4)]

# The results are now in the form [1, 0, 0, a], [0, 1, 0, b], [0, 0, 1, c]
a = equations[0][3]  # 牛價
b = equations[1][3]  # 羊價
c = equations[2][3]  # 豕價

# Output the results
a, b, c
#----- content ends here -----


"""


### Explanation of the Code:
1. **Normalization**: Each equation is divided by the leading coefficient to make it 1.
2. **Elimination**: Variables are eliminated from other equations by subtracting a multiple of the normalized equation.
3. **Back-substitution**: After elimination, the system is in triangular form, and the solution is directly obtained.

### Final Answer:
The values of \( a \), \( b \), and \( c \) represent the prices of 牛 (a), 羊 (b), and 豕 (c), respectively.
"""


"""
"""
