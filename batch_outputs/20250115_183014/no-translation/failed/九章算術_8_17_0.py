"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：麻 a斗 b錢 ，麥 c斗 d錢 ，菽 e斗 f錢 ，答 g斗 h錢 ，黍 i斗 j錢 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese mathematical techniques, which are equivalent to Gaussian elimination in modern terms. Here's how we can translate the problem into Python code:


"""


from fractions import Fraction

# Coefficients of the equations
# Each row represents the coefficients of 麻, 麥, 菽, 答, 黍, and the total value (錢)
equations = [
    [9, 7, 3, 2, 5, 140],
    [7, 6, 4, 5, 3, 128],
    [3, 5, 7, 6, 4, 116],
    [2, 5, 3, 9, 4, 112],
    [1, 3, 2, 8, 5, 95]
]

# Perform Gaussian elimination
# Step 1: Forward elimination
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

# Step 2: Back substitution
results = [0] * len(equations)
for i in range(len(equations) - 1, -1, -1):
    results[i] = equations[i][-1]
    for j in range(i + 1, len(equations)):
        results[i] -= equations[i][j] * results[j]

# Extract results
a, c, e, g, i = results
b = a.denominator
d = c.denominator
f = e.denominator
h = g.denominator
j = i.denominator

# Output results
print(f"麻 {a}斗 {b}錢")
print(f"麥 {c}斗 {d}錢")
print(f"菽 {e}斗 {f}錢")
print(f"答 {g}斗 {h}錢")
print(f"黍 {i}斗 {j}錢")


"""


### Explanation:
1. **Input Representation**: The coefficients of the equations are represented as a list of lists. Each sublist corresponds to an equation, with the last element being the total value (錢).
2. **Gaussian Elimination**:
   - **Forward Elimination**: Normalize each row by dividing by the pivot element, then eliminate the variable from subsequent rows.
   - **Back Substitution**: Solve for each variable starting from the last row and working upwards.
3. **Fraction Handling**: The `Fraction` class is used to ensure exact arithmetic with fractions.
4. **Output**: The results are displayed in terms of "斗" and "錢" for each commodity.

This code will compute the price per "斗" for 麻, 麥, 菽, 答, and 黍 as fractions, ensuring accuracy in the calculations.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 7
Variable 'b' has wrong value. Expected: 7, Actual: 1
Variable 'c' has wrong value. Expected: 1, Actual: 4
Variable 'd' has wrong value. Expected: 4, Actual: 1
Variable 'e' has wrong value. Expected: 1, Actual: 3
Variable 'f' has wrong value. Expected: 3, Actual: 1
Variable 'g' has wrong value. Expected: 1, Actual: 5
Variable 'h' has wrong value. Expected: 5, Actual: 1
Variable 'i' has wrong value. Expected: 1, Actual: 6
Variable 'j' has wrong value. Expected: 6, Actual: 1"""
