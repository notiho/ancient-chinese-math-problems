"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛價 a(=1200) ，羊價 b(=500) ，豕價 c(=300) 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, similar to Gaussian elimination. Here's the step-by-step solution encoded in Python:


"""


from fractions import Fraction

# Problem setup: Represent the system of equations
# Equation 1: 2牛 + 5羊 - 13豕 = 1000
# Equation 2: 3牛 - 9羊 + 3豕 = 0
# Equation 3: -5牛 + 6羊 + 8豕 = -600

# Coefficients of 牛, 羊, 豕, and the constant terms
equations = [
    [2, 5, -13, 1000],  # First equation
    [3, -9, 3, 0],      # Second equation
    [-5, 6, 8, -600]    # Third equation
]

# Step 1: Normalize the first equation (make the coefficient of 牛 in the first equation 1)
factor = equations[0][0]
equations[0] = [Fraction(term, factor) for term in equations[0]]

# Step 2: Eliminate 牛 from the second and third equations
for i in range(1, 3):
    factor = equations[i][0]
    equations[i] = [equations[i][j] - factor * equations[0][j] for j in range(4)]

# Step 3: Normalize the second equation (make the coefficient of 羊 in the second equation 1)
factor = equations[1][1]
equations[1] = [Fraction(term, factor) for term in equations[1]]

# Step 4: Eliminate 羊 from the third equation
factor = equations[2][1]
equations[2] = [equations[2][j] - factor * equations[1][j] for j in range(4)]

# Step 5: Solve for 豕 in the third equation
c = equations[2][3] / equations[2][2]

# Step 6: Back-substitute to solve for 羊 in the second equation
b = equations[1][3] - equations[1][2] * c

# Step 7: Back-substitute to solve for 牛 in the first equation
a = equations[0][3] - equations[0][1] * b - equations[0][2] * c

# Results
a = float(a) # 牛價
b = float(b) # 羊價
c = float(c) # 豕價

print(f"牛價 a = {a}, 羊價 b = {b}, 豕價 c = {c}")


"""


### Explanation of the Steps:
1. **Normalize the first equation**: Divide all terms in the first equation by the coefficient of 牛 to make it 1.
2. **Eliminate 牛 from the second and third equations**: Subtract a multiple of the first equation from the second and third equations to eliminate 牛.
3. **Normalize the second equation**: Divide all terms in the second equation by the coefficient of 羊 to make it 1.
4. **Eliminate 羊 from the third equation**: Subtract a multiple of the second equation from the third equation to eliminate 羊.
5. **Solve for 豕**: The third equation now contains only 豕, so solve for it.
6. **Back-substitute**: Use the value of 豕 to solve for 羊 in the second equation, and then use both values to solve for 牛 in the first equation.

### Final Answer:
- 牛價 \(a = 1200\)
- 羊價 \(b = 500\)
- 豕價 \(c = 300\)
"""


"""
"""
