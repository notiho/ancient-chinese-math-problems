"""
今有甲乙二人持錢不知其數甲得乙半而錢五十乙得甲太半而亦錢五十問甲乙持錢各幾何
術曰如方程損益之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰甲持 a錢 乙持 b錢 
"""

"""
This problem involves solving a system of equations using the ancient Chinese "fangcheng" (方程) method, which is equivalent to solving simultaneous linear equations. Let's break it down step by step and translate it into Python code.

### Problem:
Two people, A (甲) and B (乙), hold an unknown amount of money.  
- If A takes half of B's money, A will have 50 coins.  
- If B takes more than half of A's money, B will also have 50 coins.  

Question: How much money do A and B each hold?

### Procedure:
The "fangcheng" method is used to solve this system of equations. The procedure involves setting up the equations, manipulating them, and solving for the unknowns step by step.

### Equations:
Let:
- `甲 = a` (money held by A)
- `乙 = b` (money held by B)

From the problem:
1. \( a + \frac{1}{2}b = 50 \)  
2. \( b + \frac{3}{2}a = 50 \)

We will solve this system using the "fangcheng" method.

### Python Code:


"""


from fractions import Fraction

# Define the coefficients of the equations
# Equation 1: a + (1/2)b = 50
coeff_a1 = 1
coeff_b1 = Fraction(1, 2)
const1 = 50

# Equation 2: b + (3/2)a = 50
coeff_a2 = Fraction(3, 2)
coeff_b2 = 1
const2 = 50

# Step 1: Eliminate one variable (e.g., b)
# Multiply the first equation by 2 to eliminate the fraction for b
coeff_a1 *= 2
coeff_b1 *= 2
const1 *= 2

# Now the first equation becomes:
# 2a + b = 100

# The second equation remains:
# (3/2)a + b = 50

# Step 2: Subtract the second equation from the first to eliminate b
coeff_a_combined = coeff_a1 - coeff_a2
const_combined = const1 - const2

# Solve for a (money held by A)
a = Fraction(const_combined, coeff_a_combined)

# Step 3: Substitute a back into one of the original equations to solve for b
# Using the first equation: 2a + b = 100
b = Fraction(100) - 2 * a

# Final results
甲持錢 = a
乙持錢 = b

# Output the results
甲持錢, 乙持錢


"""


### Explanation:
1. The first equation is scaled to eliminate fractions, making it easier to manipulate.
2. The second equation is subtracted from the first to eliminate one variable (`b`), allowing us to solve for `a`.
3. The value of `a` is substituted back into one of the original equations to solve for `b`.

### Answer:
- \( 甲 \) (A) holds `a` coins.
- \( 乙 \) (B) holds `b` coins.
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: -100"""
