"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：令一人食 a雞 ，吏一人食 b雞 ，從者一人食 c雞 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into a system of linear equations and solve for the unknowns \( a \), \( b \), and \( c \), which represent the number of chickens eaten by one "令" (a leader), one "吏" (an official), and one "從者" (an attendant), respectively.

The problem gives us the following equations based on the total number of chickens eaten:

1. \( 1a + 5b + 10c = 10 \)
2. \( 10a + 1b + 5c = 8 \)
3. \( 5a + 10b + 1c = 6 \)

We will solve this system of equations using Python code. Here's the implementation:


"""


from fractions import Fraction

# Define the equations
# 1a + 5b + 10c = 10
# 10a + 1b + 5c = 8
# 5a + 10b + 1c = 6

# Solve for a, b, and c using substitution and elimination
# Step 1: Eliminate one variable (e.g., c) from two equations
# Multiply the first equation by 5 and the second equation by 10 to align the coefficients of c
eq1 = [1, 5, 10, 10]  # Coefficients of a, b, c, and the constant term
eq2 = [10, 1, 5, 8]
eq3 = [5, 10, 1, 6]

# Eliminate c
eq1_scaled = [x * 5 for x in eq1]  # Scale eq1 by 5
eq2_scaled = [x * 10 for x in eq2]  # Scale eq2 by 10

# Subtract eq2_scaled from eq1_scaled
eq4 = [eq1_scaled[i] - eq2_scaled[i] for i in range(4)]  # New equation without c
# eq4: [-95a, 45b, 25c, 50]

# Eliminate c from eq2 and eq3
eq2_scaled = [x * 1 for x in eq2]  # Scale eq2 by 1
eq3_scaled = [x * 5 for x in eq3]  # Scale eq3 by 5

eq5 = [eq2_scaled[i] - eq3_scaled[i] for i in range(4)]  # New equation without c
# eq5: [

"""

"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'"""
