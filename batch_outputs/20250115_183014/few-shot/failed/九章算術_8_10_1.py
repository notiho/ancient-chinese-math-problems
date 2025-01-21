"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
This is a classic simultaneous equations problem, solved using ancient Chinese "fangcheng" (method of solving linear equations). Let's translate the problem and procedure into Python code step by step.

### Problem Description:
We are given:
1. The price of 2 horses and 1 cow exceeds 10,000 by the price of half a horse.
2. The price of 1 horse and 2 cows is less than 10,000 by the price of half a cow.

We need to find the price of one horse (*a*) and one cow (*b*).

### Procedure:
The "fangcheng" method involves setting up equations and solving them systematically. Here's the Python implementation:


"""


from fractions import Fraction

# Define the equations based on the problem:
# Let 馬價 = a (price of one horse), 牛價 = b (price of one cow)

# Equation 1: 2a + b = 10000 + (1/2)a
# Rearrange: (2 - 1/2)a + b = 10000
# Simplify: (3/2)a + b = 10000

# Equation 2: a + 2b = 10000 - (1/2)b
# Rearrange: a + (2 + 1/2)b = 10000
# Simplify: a + (5/2)b = 10000

# Coefficients for the equations:
# Equation 1: (3/2)a + b = 10000
coeff1_a = Fraction(3, 2)
coeff1_b = 1
const1 = 10000

# Equation 2: a + (5/2)b = 10000
coeff2_a = 1
coeff2_b = Fraction(5, 2)
const2 = 10000

# Solve using the fangcheng method:
# Step 1: Eliminate one variable (e.g., a) by aligning coefficients and subtracting equations.

# Multiply Equation 1 by 2 to eliminate fractions:
# 3a + 2b = 20000
coeff1_a *= 2
coeff1_b *= 2
const1 *= 2

# Equation 2 remains as is:
# a + (5/2)b = 10000

# Multiply Equation 2 by 3 to align coefficients of a:
# 3a + (15/2)b = 30000
coeff2_a *= 3
coeff2_b *= 3
const2 *= 3

# Subtract the two equations:
# (3a + 2b) - (3a + (15/2)b) = 20000 - 30000
# 2b - (15/2)b = -10000
# Simplify: (4/2)b - (15/2)b = -10000
# (-11/2)b = -10000
b = Fraction(-10000, Fraction(-11, 2))

# Simplify b:
b = b * Fraction(2, 1)  # Multiply by 2 to simplify
b = Fraction(20000, 11)

# Substitute b back into one of the original equations to solve for a:
# Use Equation 1: (3/2)a + b = 10000
a = (const1 - coeff1_b * b) / coeff1_a

# Final results:
a = float(a)
b = float(b)

print(f"馬價 a = {a} 錢")
print(f"牛價 b = {b} 錢")


"""


### Explanation of the Code:
1. **Equations Setup**: The problem is translated into two linear equations based on the given conditions.
2. **Fangcheng Method**: The equations are manipulated to eliminate one variable and solve for the other.
3. **Fractions**: The `Fraction` class is used to ensure precise calculations without floating-point errors.
4. **Substitution**: Once one variable is solved, it is substituted back into one of the original equations to find the other variable.

### Answer:
The price of one horse (*a*) and one cow (*b*) is calculated and printed.
"""


"""
Variable 'a' has wrong value. Expected: 60000/11, Actual: 5454.545454545455
Variable 'b' has wrong value. Expected: 20000/11, Actual: 1818.1818181818182"""
