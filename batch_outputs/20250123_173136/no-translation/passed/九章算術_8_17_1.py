"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：麻一斗 a錢 ，麥一斗 b錢 ，菽一斗 c錢 ，答一斗 d錢 ，黍一斗 e錢 。
"""

"""
To solve this problem, we need to use a system of linear equations based on the given data. Each equation represents the total cost of a combination of goods (麻, 麥, 菽, 答, 黍), and we solve for the cost of one unit of each good. Here's the Python implementation:


"""


from fractions import Fraction

# Coefficients of the equations
# 麻, 麥, 菽, 答, 黍
equations = [
    [9, 7, 3, 2, 5, 140],  # 麻9斗, 麥7斗, 菽3斗, 答2斗, 黍5斗, 直錢140
    [7, 6, 4, 5, 3, 128],  # 麻7斗, 麥6斗, 菽4斗, 答5斗, 黍3斗, 直錢128
    [3, 5, 7, 6, 4, 116],  # 麻3斗, 麥5斗, 菽7斗, 答6斗, 黍4斗, 直錢116
    [2, 5, 3, 9, 4, 112],  # 麻2斗, 麥5斗, 菽3斗, 答9斗, 黍4斗, 直錢112
    [1, 3, 2, 8, 5, 95],   # 麻1斗, 麥3斗, 菽2斗, 答8斗, 黍5斗, 直錢95
]

# Step 1: Gaussian elimination
def gaussian_elimination(equations):
    n = len(equations)
    for i in range(n):
        # Make the diagonal element 1
        diag = equations[i][i]
        for j in range(i, n + 1):
            equations[i][j] = Fraction(equations[i][j], diag)
        
        # Eliminate the current variable from the rows below
        for k in range(i + 1, n):
            factor = equations[k][i]
            for j in range(i, n + 1):
                equations[k][j] -= factor * equations[i][j]
    
    # Step 2: Back substitution
    results = [0] * n
    for i in range(n - 1, -1, -1):
        results[i] = equations[i][n]
        for j in range(i + 1, n):
            results[i] -= equations[i][j] * results[j]
    
    return results

# Solve the system of equations
solution = gaussian_elimination(equations)

# Assign the results to variables
a, b, c, d, e = solution

# Output the results
a, b, c, d, e


"""


### Explanation:
1. **Input Data**: The `equations` list contains the coefficients of the variables (麻, 麥, 菽, 答, 黍) and the total cost for each equation.
2. **Gaussian Elimination**:
   - Normalize each row so that the diagonal element becomes 1.
   - Eliminate the variable in the rows below the current row.
   - Perform back substitution to solve for each variable.
3. **Output**: The solution gives the cost of one unit of each good (麻, 麥, 菽, 答, 黍).

### Final Answer:
- 麻一斗 = `a` 錢
- 麥一斗 = `b` 錢
- 菽一斗 = `c` 錢
- 答一斗 = `d` 錢
- 黍一斗 = `e` 錢
"""


"""
"""
