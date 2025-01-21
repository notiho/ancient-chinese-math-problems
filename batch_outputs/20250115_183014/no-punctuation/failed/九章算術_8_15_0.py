"""
今有令一人吏五人從者一十人食雞一十令一十人吏一人從者五人食雞八令五人吏一十人從者一人食雞六問令吏從者食雞各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰令 a人 食 b雞 吏 c人 食 d雞 從者 e人 食 f雞 
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese "fangcheng" (方程) method, which is equivalent to solving simultaneous equations. The problem describes three scenarios involving different groups of people (ling, li, and cong) consuming chickens, and the goal is to determine how many chickens each group consumes per person.

Let's translate the problem and solve it step by step using Python:

### Problem Setup
1. **Scenario 1**: 1 ling, 5 li, and 10 cong eat 10 chickens.
2. **Scenario 2**: 10 ling, 1 li, and 5 cong eat 8 chickens.
3. **Scenario 3**: 5 ling, 10 li, and 1 cong eat 6 chickens.

We need to find:
- How many chickens each ling eats (`a`).
- How many chickens each li eats (`c`).
- How many chickens each cong eats (`e`).

### Fangcheng Method
The procedure involves setting up a system of equations and solving it using elimination and substitution. Here's the Python implementation:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 1 ling + 5 li + 10 cong = 10 chickens
eq1 = [1, 5, 10, 10]

# Equation 2: 10 ling + 1 li + 5 cong = 8 chickens
eq2 = [10, 1, 5, 8]

# Equation 3: 5 ling + 10 li + 1 cong = 6 chickens
eq3 = [5, 10, 1, 6]

# Step 1: Eliminate the first variable (ling) from eq2 and eq3 using eq1
factor2 = Fraction(eq2[0], eq1[0])
factor3 = Fraction(eq3[0], eq1[0])

for i in range(4):
    eq2[i] -= factor2 * eq1[i]
    eq3[i] -= factor3 * eq1[i]

# Step 2: Eliminate the second variable (li) from eq3 using the modified eq2
factor3_2 = Fraction(eq3[1], eq2[1])

for i in range(4):
    eq3[i] -= factor3_2 * eq2[i]

# Step 3: Solve for the third variable (cong) from eq3
cong = Fraction(eq3[3], eq3[2])

# Step 4: Solve for the second variable (li) from eq2
li = Fraction(eq2[3] - eq2[2] * cong, eq2[1])

# Step 5: Solve for the first variable (ling) from eq1
ling = Fraction(eq1[3] - eq1[2] * cong - eq1[1] * li, eq1[0])

# Results
a = ling
c = li
e = cong

# Output the results
print(f"Each ling eats {a} chickens.")
print(f"Each li eats {c} chickens.")
print(f"Each cong eats {e} chickens.")


"""


### Explanation of the Code
1. **Step 1**: Eliminate the `ling` variable from the second and third equations by subtracting a multiple of the first equation.
2. **Step 2**: Eliminate the `li` variable from the third equation using the modified second equation.
3. **Step 3**: Solve for the `cong` variable from the simplified third equation.
4. **Step 4**: Substitute the value of `cong` into the second equation to solve for `li`.
5. **Step 5**: Substitute the values of `cong` and `li` into the first equation to solve for `ling`.

### Answer
The output will give the number of chickens each ling, li, and cong eats.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 45/122
Missing variable in output: 'b'
Variable 'c' has wrong value. Expected: 1, Actual: 41/122
Missing variable in output: 'd'
Variable 'e' has wrong value. Expected: 1, Actual: 97/122
Missing variable in output: 'f'"""
