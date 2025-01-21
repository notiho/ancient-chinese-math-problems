"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. The problem can be translated into Python code as follows:

### Problem Setup:
We are given three equations based on the transactions:
1. Selling 2 cows and 5 sheep to buy 13 pigs, with 1000 money left over.
2. Selling 3 cows and 3 pigs to buy 9 sheep, with no money left over.
3. Selling 6 sheep and 8 pigs to buy 5 cows, with a deficit of 600 money.

Let the prices of a cow, a sheep, and a pig be `牛價 (a)`, `羊價 (b)`, and `豕價 (c)` respectively. We aim to solve for `a`, `b`, and `c`.

### Equations:
1. \( 2a + 5b - 13c = 1000 \)
2. \( 3a - 9b + 3c = 0 \)
3. \( -5a + 6b + 8c = -600 \)

We will solve this system of equations using the elimination method described in the "方程術".

---

### Python Code:


"""


from fractions import Fraction

# Define the coefficients of the equations
# Each equation is represented as [牛, 羊, 豕, constant]
equations = [
    [2, 5, -13, 1000],  # 2a + 5b - 13c = 1000
    [3, -9, 3, 0],      # 3a - 9b + 3c = 0
    [-5, 6, 8, -600]    # -5a + 6b + 8c = -600
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

# Step 6: Back-substitute to solve for the variables
c = equations[2][3]  # 豕價 (c)
b = equations[1][3] - equations[1][2] * c  # 羊價 (b)
a = equations[0][3] - equations[0][2] * c - equations[0][1] * b  # 牛價 (a)

# Output the results
牛價 = a
羊價 = b
豕價 = c

print(f"牛價 a = {牛價}")
print(f"羊價 b = {羊價}")
print(f"豕價 c = {豕價}")


"""


---

### Explanation of the Code:
1. **Normalization**: Each equation is normalized by dividing through by the leading coefficient of the variable being eliminated.
2. **Elimination**: Variables are eliminated from subsequent equations by subtracting a multiple of the normalized equation.
3. **Back-substitution**: Once the system is in triangular form, the variables are solved starting from the last equation and substituting upwards.

### Answer:
The values of `a`, `b`, and `c` (prices of a cow, a sheep, and a pig) will be calculated and printed as fractions.
"""


"""
"""
