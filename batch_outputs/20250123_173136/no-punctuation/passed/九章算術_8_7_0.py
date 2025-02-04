"""
今有賣牛二羊五以買十三豕有餘錢一千賣牛三豕三以買九羊錢適足賣羊六豕八以買五牛錢不足六百問牛羊豕價各幾何
術曰如方程置牛二羊五正豕一十三負餘錢數正次牛三正羊九負豕三正次牛五負羊六正豕八正不足錢負以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰牛價 a 羊價 b 豕價 c 
"""

"""
This problem involves solving a system of linear equations to determine the prices of cows, sheep, and pigs. The ancient Chinese method described here is equivalent to solving simultaneous linear equations using elimination and substitution. Let's translate this into Python code step by step.

### Problem Setup
We are given three equations based on the transactions:
1. Selling 2 cows and 5 sheep to buy 13 pigs, with 1000 money left over.
   \( 2a + 5b - 13c = 1000 \)
2. Selling 3 cows and 3 pigs to buy 9 sheep, with no money left over.
   \( 3a - 9b + 3c = 0 \)
3. Selling 6 sheep and 8 pigs to buy 5 cows, with 600 money short.
   \( -5a + 6b + 8c = -600 \)

Here, \(a\), \(b\), and \(c\) represent the prices of cows, sheep, and pigs, respectively.

### Procedure
The ancient method involves systematically eliminating variables to solve for the unknowns. Below is the Python implementation of the procedure.


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 2a + 5b - 13c = 1000
eq1 = [2, 5, -13, 1000]

# Equation 2: 3a - 9b + 3c = 0
eq2 = [3, -9, 3, 0]

# Equation 3: -5a + 6b + 8c = -600
eq3 = [-5, 6, 8, -600]

# Step 1: Eliminate the first variable (a) from eq2 and eq3 using eq1
factor1 = Fraction(eq2[0], eq1[0])  # Factor to multiply eq1 by to eliminate a in eq2
factor2 = Fraction(eq3[0], eq1[0])  # Factor to multiply eq1 by to eliminate a in eq3

# Subtract scaled eq1 from eq2 and eq3
eq2 = [eq2[i] - factor1 * eq1[i] for i in range(4)]
eq3 = [eq3[i] - factor2 * eq1[i] for i in range(4)]

# Step 2: Eliminate the second variable (b) from eq3 using the new eq2
factor3 = Fraction(eq3[1], eq2[1])  # Factor to multiply eq2 by to eliminate b in eq3
eq3 = [eq3[i] - factor3 * eq2[i] for i in range(4)]

# Step 3: Solve for c (the third variable) from eq3
c = Fraction(eq3[3], eq3[2])

# Step 4: Solve for b (the second variable) using the new eq2
b = Fraction(eq2[3] - eq2[2] * c, eq2[1])

# Step 5: Solve for a (the first variable) using eq1
a = Fraction(eq1[3] - eq1[1] * b - eq1[2] * c, eq1[0])

# Output the results
a = float(a)
b = float(b)
c = float(c)

print(f"牛價 a = {a}")
print(f"羊價 b = {b}")
print(f"豕價 c = {c}")


"""


### Explanation of the Code
1. **Step 1**: Eliminate the first variable (\(a\)) from the second and third equations by scaling and subtracting the first equation.
2. **Step 2**: Eliminate the second variable (\(b\)) from the third equation using the updated second equation.
3. **Step 3**: Solve for the third variable (\(c\)) from the simplified third equation.
4. **Step 4**: Back-substitute \(c\) into the second equation to solve for \(b\).
5. **Step 5**: Back-substitute \(b\) and \(c\) into the first equation to solve for \(a\).

### Answer
The values of \(a\), \(b\), and \(c\) represent the prices of cows, sheep, and pigs, respectively. The output will display these values.
"""


"""
"""
