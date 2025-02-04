"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：麻一斗 a錢 ，麥一斗 b錢 ，菽一斗 c錢 ，答一斗 d錢 ，黍一斗 e錢 。
"""

"""
This problem involves solving a system of linear equations to determine the price of one dou of each type of grain. The problem is described in terms of ancient Chinese mathematical methods, specifically using the "正負術" (positive and negative method) and "方程術" (method of simultaneous equations). Below is the Python implementation of the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations (麻, 麥, 菽, 答, 黍)
equations = [
    [9, 7, 3, 2, 5, 140],  # 麻9斗, 麥7斗, 菽3斗, 答2斗, 黍5斗, 直錢140
    [7, 6, 4, 5, 3, 128],  # 麻7斗, 麥6斗, 菽4斗, 答5斗, 黍3斗, 直錢128
    [3, 5, 7, 6, 4, 116],  # 麻3斗, 麥5斗, 菽7斗, 答6斗, 黍4斗, 直錢116
    [2, 5, 3, 9, 4, 112],  # 麻2斗, 麥5斗, 菽3斗, 答9斗, 黍4斗, 直錢112
    [1, 3, 2, 8, 5, 95],   # 麻1斗, 麥3斗, 菽2斗, 答8斗, 黍5斗, 直錢95
]

# Step 1: Eliminate variables using Gaussian elimination
for i in range(len(equations)):
    # Normalize the current row
    divisor = equations[i][i]
    for j in range(len(equations[i])):
        equations[i][j] = Fraction(equations[i][j], divisor)
    
    # Eliminate the current variable from all other rows
    for k in range(len(equations)):
        if k != i:
            factor = equations[k][i]
            for j in range(len(equations[k])):
                equations[k][j] -= factor * equations[i][j]

# Step 2: Extract the solutions
a = equations[0][-1]  # 麻一斗
b = equations[1][-1]  # 麥一斗
c = equations[2][-1]  # 菽一斗
d = equations[3][-1]  # 答一斗
e = equations[4][-1]  # 黍一斗

# Output the results
a, b, c, d, e
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input the Equations**: The coefficients of the grains (麻, 麥, 菽, 答, 黍) and their total price are stored in a list of lists.
2. **Gaussian Elimination**: The system of equations is solved using Gaussian elimination, which involves normalizing each row and eliminating variables step by step.
3. **Extract the Solutions**: After elimination, the last column of each row contains the solution for the corresponding variable.
4. **Output the Results**: The prices of one dou of 麻, 麥, 菽, 答, and 黍 are stored in `a`, `b`, `c`, `d`, and `e`, respectively.

### Answer:
The prices of one dou of each grain are:
- 麻一斗: `a` 錢
- 麥一斗: `b` 錢
- 菽一斗: `c` 錢
- 答一斗: `d` 錢
- 黍一斗: `e` 錢
"""


"""
"""
