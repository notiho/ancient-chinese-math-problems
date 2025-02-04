"""
今有賣牛二羊五以買十三豕有餘錢一千賣牛三豕三以買九羊錢適足賣羊六豕八以買五牛錢不足六百問牛羊豕價各幾何
術曰如方程置牛二羊五正豕一十三負餘錢數正次牛三正羊九負豕三正次牛五負羊六正豕八正不足錢負以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰牛價 a 羊價 b 豕價 c 
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, as described in the "方程術" (method of solving simultaneous equations). Below is the Python implementation of the problem and its solution:


"""


from fractions import Fraction

# Define the coefficients of the equations
# Equation 1: 2牛 + 5羊 - 13豕 = 1000
eq1 = [2, 5, -13, 1000]

# Equation 2: 3牛 - 9羊 + 3豕 = 0
eq2 = [3, -9, 3, 0]

# Equation 3: 5牛 - 6羊 + 8豕 = -600
eq3 = [5, -6, 8, -600]

# Step 1: Eliminate the first variable (牛) from eq2 and eq3 using eq1
factor1 = Fraction(eq2[0], eq1[0])  # Coefficient of 牛 in eq2 divided by coefficient of 牛 in eq1
factor2 = Fraction(eq3[0], eq1[0])  # Coefficient of 牛 in eq3 divided by coefficient of 牛 in eq1

# Subtract (factor1 * eq1) from eq2
eq2 = [eq2[i] - factor1 * eq1[i] for i in range(4)]

# Subtract (factor2 * eq1) from eq3
eq3 = [eq3[i] - factor2 * eq1[i] for i in range(4)]

# Step 2: Eliminate the second variable (羊) from eq3 using eq2
factor3 = Fraction(eq3[1], eq2[1])  # Coefficient of 羊 in eq3 divided by coefficient of 羊 in eq2

# Subtract (factor3 * eq2) from eq3
eq3 = [eq3[i] - factor3 * eq2[i] for i in range(4)]

# Step 3: Solve for 豕 (c) from eq3
c = Fraction(eq3[3], eq3[2])

# Step 4: Solve for 羊 (b) from eq2
b = Fraction(eq2[3] - eq2[2] * c, eq2[1])

# Step 5: Solve for 牛 (a) from eq1
a = Fraction(eq1[3] - eq1[2] * c - eq1[1] * b, eq1[0])

# Output the results
a, b, c


"""


### Explanation of the Code:
1. **Define the Equations**: Each equation is represented as a list of coefficients `[牛, 羊, 豕, constant]`.
2. **Elimination**: The first variable (牛) is eliminated from the second and third equations using the first equation. Then, the second variable (羊) is eliminated from the third equation using the second equation.
3. **Back-Substitution**: After elimination, the third equation contains only one variable (豕), which is solved directly. The solution for 豕 is substituted back into the second equation to solve for 羊, and then both are substituted into the first equation to solve for 牛.
4. **Output**: The values of 牛 (a), 羊 (b), and 豕 (c) are the solutions.

### Answer:
The solution gives the prices of 牛 (a), 羊 (b), and 豕 (c) in terms of their respective values.
"""


"""
Variable 'a' has wrong value. Expected: 1200, Actual: -100/7
Variable 'b' has wrong value. Expected: 500, Actual: -250/7
Variable 'c' has wrong value. Expected: 300, Actual: -650/7"""
