"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：麻 a斗 b錢 ，麥 c斗 d錢 ，菽 e斗 f錢 ，答 g斗 h錢 ，黍 i斗 j錢 。
"""

"""
This problem is a system of linear equations, and solving it involves applying the ancient Chinese method of elimination, which is similar to Gaussian elimination. Below is the Python implementation of the procedure described in the problem:


"""


from fractions import Fraction

# Coefficients of the equations
# Each row represents the coefficients of 麻, 麥, 菽, 答, 黍, and the total price
equations = [
    [9, 7, 3, 2, 5, 140],
    [7, 6, 4, 5, 3, 128],
    [3, 5, 7, 6, 4, 116],
    [2, 5, 3, 9, 4, 112],
    [1, 3, 2, 8, 5, 95],
]

# Step 1: Forward elimination
for i in range(len(equations)):
    # Normalize the current row
    divisor = equations[i][i]
    for j in range(len(equations[i])):
        equations[i][j] = Fraction(equations[i][j], divisor)
    
    # Eliminate the current variable from the rows below
    for k in range(i + 1, len(equations)):
        multiplier = equations[k][i]
        for j in range(len(equations[k])):
            equations[k][j] -= multiplier * equations[i][j]

# Step 2: Back substitution
results = [0] * len(equations)
for i in range(len(equations) - 1, -1, -1):
    results[i] = equations[i][-1]
    for j in range(i + 1, len(equations)):
        results[i] -= equations[i][j] * results[j]

# Assign results to variables
a, c, e, g, i = results

# Convert to 鬥 and 錢
def convert_to_dou_and_qian(value):
    dou = int(value)
    qian = (value - dou) * 10
    return dou, qian

a_dou, a_qian = convert_to_dou_and_qian(a)
c_dou, c_qian = convert_to_dou_and_qian(c)
e_dou, e_qian = convert_to_dou_and_qian(e)
g_dou, g_qian = convert_to_dou_and_qian(g)
i_dou, i_qian = convert_to_dou_and_qian(i)

# Final answer
print(f"麻 {a_dou}斗 {a_qian}錢 ，麥 {c_dou}斗 {c_qian}錢 ，菽 {e_dou}斗 {e_qian}錢 ，答 {g_dou}斗 {g_qian}錢 ，黍 {i_dou}斗 {i_qian}錢 。")


"""


### Explanation of the Code:
1. **Input Representation**: The coefficients of the equations are represented as a list of lists, where each inner list corresponds to one equation.
2. **Forward Elimination**: The system of equations is transformed into an upper triangular matrix by normalizing each row and eliminating the variable from the rows below.
3. **Back Substitution**: Starting from the last row, the values of the variables are calculated by substituting the known values into the equations.
4. **Conversion to 鬥 and 錢**: Each result is converted into 鬥 (integer part) and 錢 (fractional part multiplied by 10).

### Output:
The output will display the price of one 鬥 of each grain in terms of 鬥 and 錢.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 7
Missing variable in output: 'b'
Variable 'c' has wrong value. Expected: 1, Actual: 4
Missing variable in output: 'd'
Variable 'e' has wrong value. Expected: 1, Actual: 3
Missing variable in output: 'f'
Variable 'g' has wrong value. Expected: 1, Actual: 5
Missing variable in output: 'h'
Variable 'i' has wrong value. Expected: 1, Actual: 6
Variable 'j' has wrong value. Expected: 6, Actual: 4"""
