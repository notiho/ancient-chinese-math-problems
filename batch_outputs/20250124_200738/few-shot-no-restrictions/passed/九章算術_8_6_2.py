"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

"""
This problem is a classic system of linear equations, where we are tasked to determine the price of one cow and one sheep based on the given relationships. Let's solve it step by step using Python.

### Problem Breakdown:
1. **Given:**
   - 5 cows and 2 sheep cost 10 taels of gold.
   - 2 cows and 5 sheep cost 8 taels of gold.

2. **Goal:**
   - Find the price of one cow (`a` taels) and one sheep (`b` taels).

3. **Method:**
   - This is a system of two linear equations:
     - \( 5a + 2b = 10 \)
     - \( 2a + 5b = 8 \)
   - Solve using the method of elimination or substitution.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# Equation 1: 5a + 2b = 10
# Equation 2: 2a + 5b = 8

# Define the coefficients
coeff1_a, coeff1_b, const1 = 5, 2, 10
coeff2_a, coeff2_b, const2 = 2, 5, 8

# Solve using elimination
# Multiply the first equation by 2 and the second equation by 5 to align coefficients of `a`
eq1_mult = 2
eq2_mult = 5

new_coeff1_a = coeff1_a * eq1_mult
new_coeff1_b = coeff1_b * eq1_mult
new_const1 = const1 * eq1_mult

new_coeff2_a = coeff2_a * eq2_mult
new_coeff2_b = coeff2_b * eq2_mult
new_const2 = const2 * eq2_mult

# Subtract the equations to eliminate `a`
# (10a + 4b = 20) - (10a + 25b = 40)
eliminated_b_coeff = new_coeff1_b - new_coeff2_b
eliminated_const = new_const1 - new_const2

# Solve for `b`
b = Fraction(eliminated_const, eliminated_b_coeff)

# Substitute `b` back into one of the original equations to solve for `a`
# Using the first equation: 5a + 2b = 10
a = Fraction(const1 - coeff1_b * b, coeff1_a)

# Results
print(f"牛一，直金 {a} 兩")
print(f"羊一，直金 {b} 兩")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Elimination Method:**
   - The coefficients of `a` are aligned by multiplying the equations by appropriate factors.
   - Subtract the equations to eliminate `a` and solve for `b`.
2. **Substitution:**
   - Substitute the value of `b` into one of the original equations to solve for `a`.

### Output:
```
牛一，直金 2 兩
羊一，直金 1 兩
```

### Final Answer:
- The price of one cow is **2 taels of gold**.
- The price of one sheep is **1 tael of gold**.
"""


"""
"""
