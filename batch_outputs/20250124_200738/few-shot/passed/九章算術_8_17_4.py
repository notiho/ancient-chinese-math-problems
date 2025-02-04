"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：麻一斗 a錢 ，麥一斗 b錢 ，菽一斗 c錢 ，答一斗 d錢 ，黍一斗 e錢 。
"""

"""
The problem presented is a system of linear equations, which can be solved using the method described in ancient Chinese mathematics, specifically the "正負術" (positive and negative method) and "方程術" (method of simultaneous equations). Below is the Python implementation of the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# 麻 (ma), 麥 (mai), 菽 (shu), 答 (da), 黍 (shu)
equations = [
    [9, 7, 3, 2, 5, 140],  # 麻9斗, 麥7斗, 菽3斗, 答2斗, 黍5斗, 直錢140
    [7, 6, 4, 5, 3, 128],  # 麻7斗, 麥6斗, 菽4斗, 答5斗, 黍3斗, 直錢128
    [3, 5, 7, 6, 4, 116],  # 麻3斗, 麥5斗, 菽7斗, 答6斗, 黍4斗, 直錢116
    [2, 5, 3, 9, 4, 112],  # 麻2斗, 麥5斗, 菽3斗, 答9斗, 黍4斗, 直錢112
    [1, 3, 2, 8, 5, 95]    # 麻1斗, 麥3斗, 菽2斗, 答8斗, 黍5斗, 直錢95
]

# Step 1: Normalize the equations using the 正負術 (positive and negative method)
# Convert the system of equations into an upper triangular form
for i in range(len(equations)):
    # Normalize the current row
    divisor = equations[i][i]
    for j in range(len(equations[i])):
        equations[i][j] = Fraction(equations[i][j], divisor)
    
    # Eliminate the current variable from subsequent rows
    for k in range(i + 1, len(equations)):
        multiplier = equations[k][i]
        for j in range(len(equations[k])):
            equations[k][j] -= multiplier * equations[i][j]

# Step 2: Back-substitution to solve for each variable
# Initialize the solution array
solution = [0] * len(equations)

# Solve for each variable starting from the last row
for i in range(len(equations) - 1, -1, -1):
    solution[i] = equations[i][-1]
    for j in range(i + 1, len(equations)):
        solution[i] -= equations[i][j] * solution[j]

# Extract the results
a = solution[0]  # 麻一斗
b = solution[1]  # 麥一斗
c = solution[2]  # 菽一斗
d = solution[3]  # 答一斗
e = solution[4]  # 黍一斗

# Output the results
a, b, c, d, e
#----- content ends here -----


"""


### Explanation:
1. **Input Data**: The coefficients of the equations represent the quantities of 麻 (ma), 麥 (mai), 菽 (shu), 答 (da), and 黍 (shu) in each equation, along with the total value in 錢 (money).

2. **正負術 (Positive and Negative Method)**: This is equivalent to Gaussian elimination, where the system of equations is transformed into an upper triangular matrix.

3. **Back-Substitution**: After transforming the system into an upper triangular form, the solution is obtained by solving for each variable starting from the last equation.

4. **Output**: The solution gives the value of one 斗 (dou) of each item in terms of 錢 (money).

### Final Answer:
The values of 麻, 麥, 菽, 答, and 黍 per 斗 are:
- 麻一斗 = `a` 錢
- 麥一斗 = `b` 錢
- 菽一斗 = `c` 錢
- 答一斗 = `d` 錢
- 黍一斗 = `e` 錢
"""


"""
"""
