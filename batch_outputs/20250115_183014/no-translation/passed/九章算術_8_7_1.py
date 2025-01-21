"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
To solve this problem, we need to set up a system of linear equations based on the given relationships and solve it using the described method (Gaussian elimination). Here's the Python implementation:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 2牛 + 5羊 - 13豕 = 1000
# Equation 2: 3牛 - 9羊 + 3豕 = 0
# Equation 3: -5牛 + 6羊 + 8豕 = -600
equations = [
    [2, 5, -13, 1000],
    [3, -9, 3, 0],
    [-5, 6, 8, -600]
]

# Gaussian elimination
def gaussian_elimination(equations):
    n = len(equations)
    
    # Forward elimination
    for i in range(n):
        # Normalize the pivot row
        pivot = equations[i][i]
        for j in range(i, n + 1):
            equations[i][j] = Fraction(equations[i][j], pivot)
        
        # Eliminate the current variable from subsequent rows
        for k in range(i + 1, n):
            factor = equations[k][i]
            for j in range(i, n + 1):
                equations[k][j] -= factor * equations[i][j]
    
    # Back substitution
    results = [0] * n
    for i in range(n - 1, -1, -1):
        results[i] = equations[i][n]
        for j in range(i + 1, n):
            results[i] -= equations[i][j] * results[j]
    
    return results

# Solve the system of equations
solution = gaussian_elimination(equations)

# Extract the results
a = solution[0]  # 牛價
b = solution[1]  # 羊價
c = solution[2]  # 豕價

# Output the results
a, b, c


"""


### Explanation of the Code:
1. **Equations Setup**: The problem gives us three equations based on the relationships between 牛 (cattle), 羊 (sheep), and 豕 (pigs). These are represented as a matrix where each row corresponds to an equation, and the last column is the constant term.

2. **Gaussian Elimination**:
   - **Forward Elimination**: Normalize each row by dividing by the pivot element, then eliminate the current variable from all rows below.
   - **Back Substitution**: Solve for each variable starting from the last row and substituting back into the previous rows.

3. **Results**: The solution to the system gives the prices of 牛, 羊, and 豕.

### Final Answer:
- 牛價 \( a \)
- 羊價 \( b \)
- 豕價 \( c \)
"""


"""
"""
