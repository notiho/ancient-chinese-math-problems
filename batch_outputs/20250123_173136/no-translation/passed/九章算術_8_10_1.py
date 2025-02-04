"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
This problem involves solving a system of linear equations using an ancient Chinese method similar to Gaussian elimination. Let's translate the procedure into Python code step by step.

The problem can be expressed as two equations:
1. \( 2M + B = 10000 + \frac{1}{2}M \)
2. \( M + 2B = 10000 - \frac{1}{2}B \)

Where \( M \) is the price of a horse (馬價), and \( B \) is the price of a cow (牛價).

We will follow the ancient "方程術" (method of solving simultaneous equations) to solve this.


"""


from fractions import Fraction

# Define the equations based on the problem
# Equation 1: 2M + B = 10000 + 1/2M
# Rearrange to standard form: (2 - 1/2)M + B = 10000
# Equation 2: M + 2B = 10000 - 1/2B
# Rearrange to standard form: M + (2 + 1/2)B = 10000

# Coefficients of the equations
a1 = Fraction(2) - Fraction(1, 2)  # Coefficient of M in equation 1
b1 = Fraction(1)                  # Coefficient of B in equation 1
c1 = Fraction(10000)              # Constant term in equation 1

a2 = Fraction(1)                  # Coefficient of M in equation 2
b2 = Fraction(2) + Fraction(1, 2) # Coefficient of B in equation 2
c2 = Fraction(10000)              # Constant term in equation 2

# Step 1: Eliminate M from the second equation
# Multiply the first equation by a2 and the second equation by a1
# Then subtract the two equations

factor1 = a2
factor2 = a1

new_b = factor1 * b1 - factor2 * b2  # New coefficient of B
new_c = factor1 * c1 - factor2 * c2  # New constant term

# Solve for B
b = new_c / new_b

# Step 2: Solve for M using the first equation
m = (c1 - b1 * b) / a1

# Results
a = m  # Price of a horse
b = b  # Price of a cow

# Output the results
a, b


"""


### Explanation of the Code:
1. The equations are rearranged into standard linear form.
2. The coefficients of the variables are extracted.
3. The first equation is used to eliminate \( M \) from the second equation, leaving a single equation in terms of \( B \).
4. Solve for \( B \) (price of a cow).
5. Substitute \( B \) back into the first equation to solve for \( M \) (price of a horse).
6. The results are stored in \( a \) and \( b \).

### Final Answer:
- \( a \): Price of a horse (馬價)
- \( b \): Price of a cow (牛價)
"""


"""
"""
