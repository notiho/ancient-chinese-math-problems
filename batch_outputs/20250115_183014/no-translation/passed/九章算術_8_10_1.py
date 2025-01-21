"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
This problem involves solving a system of linear equations using an ancient Chinese method similar to Gaussian elimination. Let's translate the procedure into Python code step by step.

The problem can be expressed as the following system of equations:
1. \( 2M + B = 10000 + \frac{1}{2}M \)
2. \( M + 2B = 10000 - \frac{1}{2}B \)

Where \( M \) is the price of a horse (馬價), and \( B \) is the price of a cow (牛價).

We will solve this using the described "方程術" (method of solving equations).


"""


from fractions import Fraction

# Define the equations based on the problem
# Equation 1: 2M + B = 10000 + 1/2M
# Rearrange to standard form: (2 - 1/2)M + B = 10000
# Equation 2: M + 2B = 10000 - 1/2B
# Rearrange to standard form: M + (2 + 1/2)B = 10000

# Coefficients of the equations
a1, b1, c1 = Fraction(3, 2), 1, 10000  # From equation 1
a2, b2, c2 = 1, Fraction(5, 2), 10000  # From equation 2

# Step 1: Eliminate one variable (use 方程術 to solve)
# Multiply the first equation by b2 and the second equation by b1 to align coefficients of B
factor1 = b2
factor2 = b1

new_a1 = a1 * factor1
new_b1 = b1 * factor1
new_c1 = c1 * factor1

new_a2 = a2 * factor2
new_b2 = b2 * factor2
new_c2 = c2 * factor2

# Subtract the second equation from the first to eliminate B
final_a = new_a1 - new_a2
final_c = new_c1 - new_c2

# Solve for M (馬價)
M = final_c / final_a

# Step 2: Substitute M back into one of the original equations to solve for B (牛價)
B = (c1 - a1 * M) / b1

# Results
a = M  # 馬價
b = B  # 牛價

# Output the results
a, b


"""


### Explanation:
1. The equations are rearranged into standard linear form.
2. The coefficients are aligned to eliminate one variable using the described method.
3. The remaining variable is solved, and the result is substituted back to find the other variable.

### Answer:
- \( a \): 馬價 (price of a horse)
- \( b \): 牛價 (price of a cow)
"""


"""
"""
