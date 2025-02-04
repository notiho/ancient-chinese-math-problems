"""
今有麻九斗麥七斗菽三斗答二斗黍五斗直錢一百四十麻七斗麥六斗菽四斗答五斗黍三斗直錢一百二十八麻三斗麥五斗菽七斗答六斗黍四斗直錢一百一十六麻二斗麥五斗菽三斗答九斗黍四斗直錢一百一十二麻一斗麥三斗菽二斗答八斗黍五斗直錢九十五問一斗直幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰麻一斗 a錢 麥一斗 b錢 菽一斗 c錢 答一斗 d錢 黍一斗 e錢 
"""

"""
This problem involves a system of linear equations to determine the price of one dou of each type of grain (麻, 麥, 菽, 答, 黍). The procedure described is essentially solving the system using elimination and substitution, akin to Gaussian elimination. Let's translate the procedure into Python code.

### Problem Setup
We are given the following equations based on the problem statement:

1. \( 9麻 + 7麥 + 3菽 + 2答 + 5黍 = 140 \)
2. \( 7麻 + 6麥 + 4菽 + 5答 + 3黍 = 128 \)
3. \( 3麻 + 5麥 + 7菽 + 6答 + 4黍 = 116 \)
4. \( 2麻 + 5麥 + 3菽 + 9答 + 4黍 = 112 \)
5. \( 1麻 + 3麥 + 2菽 + 8答 + 5黍 = 95 \)

We need to solve for the price of one dou of 麻 (\(a\)), 麥 (\(b\)), 菽 (\(c\)), 答 (\(d\)), and 黍 (\(e\)).

### Procedure
The procedure described in the problem uses elimination to reduce the system of equations step by step. Here's the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
equations = [
    [9, 7, 3, 2, 5, 140],  # 9麻 + 7麥 + 3菽 + 2答 + 5黍 = 140
    [7, 6, 4, 5, 3, 128],  # 7麻 + 6麥 + 4菽 + 5答 + 3黍 = 128
    [3, 5, 7, 6, 4, 116],  # 3麻 + 5麥 + 7菽 + 6答 + 4黍 = 116
    [2, 5, 3, 9, 4, 112],  # 2麻 + 5麥 + 3菽 + 9答 + 4黍 = 112
    [1, 3, 2, 8, 5, 95],   # 1麻 + 3麥 + 2菽 + 8答 + 5黍 = 95
]

# Convert all coefficients to fractions for exact arithmetic
equations = [[Fraction(x) for x in row] for row in equations]

# Elimination process
num_equations = len(equations)
num_variables = len(equations[0]) - 1

for i in range(num_variables):
    # Make the diagonal element 1 by dividing the row
    factor = equations[i][i]
    equations[i] = [x / factor for x in equations[i]]
    
    # Eliminate the current variable from all other rows
    for j in range(num_equations):
        if i != j:
            factor = equations[j][i]
            equations[j] = [equations[j][k] - factor * equations[i][k] for k in range(len(equations[j]))]

# Extract the solutions
a = equations[0][-1]  # 麻
b = equations[1][-1]  # 麥
c = equations[2][-1]  # 菽
d = equations[3][-1]  # 答
e = equations[4][-1]  # 黍

# Output the results
a, b, c, d, e
#----- content ends here -----


"""


### Explanation of the Code
1. **Input Representation**: Each equation is represented as a list of coefficients, with the last element being the constant term (e.g., \(140\), \(128\), etc.).
2. **Fraction Arithmetic**: All coefficients are converted to `Fraction` to ensure exact arithmetic throughout the process.
3. **Gaussian Elimination**:
   - For each variable, the corresponding row is normalized so that the diagonal element becomes 1.
   - The variable is then eliminated from all other rows by subtracting an appropriate multiple of the normalized row.
4. **Solution Extraction**: After elimination, the last column of each row contains the solution for the corresponding variable.

### Answer
The solution will give the price of one dou of 麻 (\(a\)), 麥 (\(b\)), 菽 (\(c\)), 答 (\(d\)), and 黍 (\(e\)) in terms of exact fractions.
"""


"""
"""
