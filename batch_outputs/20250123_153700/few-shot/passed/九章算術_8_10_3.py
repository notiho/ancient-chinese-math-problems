"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. Let's translate the problem into Python code step by step.

### Problem Setup:
We are given:
1. The price of two horses and one cow exceeds 10,000 by the price of half a horse.
2. The price of one horse and two cows is less than 10,000 by the price of half a cow.

We need to find the price of one horse (*a*) and one cow (*b*).

### Procedure:
The procedure described is the ancient Chinese method of solving simultaneous equations, which involves elimination and substitution. Let's implement this step by step.


"""


from fractions import Fraction

# Define the equations based on the problem:
# Let 馬 = a (price of one horse) and 牛 = b (price of one cow)
# Equation 1: 2a + b = 10000 + 0.5a
# Equation 2: a + 2b = 10000 - 0.5b

# Rewrite the equations to standard form:
# Equation 1: 1.5a + b = 10000
# Equation 2: a + 2.5b = 10000

# Step 1: Represent the coefficients of the equations
# Coefficients for the first equation: 1.5a + b = 10000
coeff1_a = Fraction(3, 2)  # 1.5
coeff1_b = Fraction(1)    # 1
const1 = Fraction(10000)

# Coefficients for the second equation: a + 2.5b = 10000
coeff2_a = Fraction(1)    # 1
coeff2_b = Fraction(5, 2)  # 2.5
const2 = Fraction(10000)

# Step 2: Eliminate one variable (use elimination method)
# Multiply the first equation by 2 to eliminate fractions:
# 3a + 2b = 20000
coeff1_a *= 2
coeff1_b *= 2
const1 *= 2

# The first equation becomes: 3a + 2b = 20000
# The second equation remains: a + 2.5b = 10000

# Multiply the second equation by 3 to align the coefficients of 'a':
# 3a + 7.5b = 30000
coeff2_a *= 3
coeff2_b *= 3
const2 *= 3

# Step 3: Subtract the first equation from the second to eliminate 'a':
# (3a + 7.5b) - (3a + 2b) = 30000 - 20000
# 5.5b = 10000
b = Fraction(10000, Fraction(11, 2))  # Solve for b
b = b  # Simplify

# Step 4: Substitute b back into one of the original equations to solve for a:
# Use the first equation: 1.5a + b = 10000
a = (const1 - coeff1_b * b) / coeff1_a

# Final answers:
print(f"馬價 a = {a} 錢")  # Price of one horse
print(f"牛價 b = {b} 錢")  # Price of one cow


"""


### Explanation of the Code:
1. **Equation Setup**: The two equations are derived from the problem statement and rewritten in standard form.
2. **Elimination**: The coefficients are adjusted to align one variable (in this case, 'a') for elimination.
3. **Substitution**: After solving for one variable ('b'), it is substituted back into one of the original equations to solve for the other variable ('a').
4. **Fraction Handling**: The `Fraction` class is used to ensure precise arithmetic with fractions, as required by the problem.

### Final Answer:
The values of `a` (price of one horse) and `b` (price of one cow) will be printed as fractions or integers, depending on the result.
"""


"""
"""
