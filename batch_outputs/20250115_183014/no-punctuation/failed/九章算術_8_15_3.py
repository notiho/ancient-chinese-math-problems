"""
今有令一人吏五人從者一十人食雞一十令一十人吏一人從者五人食雞八令五人吏一十人從者一人食雞六問令吏從者食雞各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰令 a人 食 b雞 吏 c人 食 d雞 從者 e人 食 f雞 
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of "fangcheng" (方程), which is equivalent to solving simultaneous equations. The problem involves determining how many chickens are consumed by each group (令, 吏, 從者) based on the given constraints.

### Problem Restatement:
There are three groups: 令 (leaders), 吏 (officials), and 從者 (followers). The problem provides three scenarios:
1. 1 leader, 5 officials, and 10 followers consume 10 chickens.
2. 10 leaders, 1 official, and 5 followers consume 8 chickens.
3. 5 leaders, 10 officials, and 1 follower consume 6 chickens.

The goal is to determine how many chickens each group consumes per person.

### Procedure:
The ancient Chinese "fangcheng" method involves setting up a system of equations and solving it step by step using elimination and substitution. Below is the Python implementation of the procedure.


"""


from fractions import Fraction

# Coefficients for the equations
# Equation 1: 1令 + 5吏 + 10從者 = 10
eq1 = [1, 5, 10, 10]

# Equation 2: 10令 + 1吏 + 5從者 = 8
eq2 = [10, 1, 5, 8]

# Equation 3: 5令 + 10吏 + 1從者 = 6
eq3 = [5, 10, 1, 6]

# Step 1: Eliminate the first variable (令) from eq2 and eq3 using eq1
factor2 = Fraction(eq2[0], eq1[0])  # Factor to eliminate 令 from eq2
factor3 = Fraction(eq3[0], eq1[0])  # Factor to eliminate 令 from eq3

# Subtract (factor * eq1) from eq2 and eq3
eq2 = [eq2[i] - factor2 * eq1[i] for i in range(4)]
eq3 = [eq3[i] - factor3 * eq1[i] for i in range(4)]

# Step 2: Eliminate the second variable (吏) from eq3 using the modified eq2
factor3_2 = Fraction(eq3[1], eq2[1])  # Factor to eliminate 吏 from eq3
eq3 = [eq3[i] - factor3_2 * eq2[i] for i in range(4)]

# Step 3: Solve for 從者 (followers) in eq3
從者 = Fraction(eq3[3], eq3[2])

# Step 4: Solve for 吏 (officials) in eq2 using 從者
吏 = Fraction(eq2[3] - eq2[2] * 從者, eq2[1])

# Step 5: Solve for 令 (leaders) in eq1 using 吏 and 從者
令 = Fraction(eq1[3] - eq1[1] * 吏 - eq1[2] * 從者, eq1[0])

# Step 6: Calculate the number of chickens consumed by each group
a = 令  # Number of leaders
b = 令  # Chickens consumed by leaders
c = 吏  # Number of officials
d = 吏  # Chickens consumed by officials
e = 從者  # Number of followers
f = 從者  # Chickens consumed by followers

# Output the results
a, b, c, d, e, f


"""


### Explanation of the Code:
1. **Setting up the equations**: Each equation is represented as a list of coefficients, where the last element is the constant term (number of chickens consumed).
2. **Elimination**: The first variable (令) is eliminated from the second and third equations using the first equation. Then, the second variable (吏) is eliminated from the third equation using the modified second equation.
3. **Back-substitution**: The third equation is solved for the third variable (從者). This value is substituted back into the second equation to solve for the second variable (吏), and then into the first equation to solve for the first variable (令).
4. **Results**: The values of 令, 吏, and 從者 represent the number of chickens consumed per person in each group.

### Answer:
The solution will provide the values of `a`, `b`, `c`, `d`, `e`, and `f`, which represent the number of people and chickens consumed by each group.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 45/122
Variable 'c' has wrong value. Expected: 1, Actual: 41/122
Variable 'e' has wrong value. Expected: 1, Actual: 97/122"""
