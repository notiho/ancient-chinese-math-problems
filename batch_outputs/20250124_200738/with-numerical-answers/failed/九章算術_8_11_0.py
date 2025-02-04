"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：武馬一匹力引 a(=160/7)石 ，中馬一匹力引 b(=120/7)石 ，下馬一匹力引 c(=40/7)石 。
"""

#----- content starts here -----
"""
Suppose there is one Wu horse, two Zhong horses, and three Xia horses. Each is tasked with carrying 40 shi up a slope, but none can do so alone.
The Wu horse borrows one Zhong horse, the Zhong horse borrows one Xia horse, and the Xia horse borrows one Wu horse. With this arrangement, all are able to ascend the slope.
Question: How much pulling force does each Wu, Zhong, and Xia horse exert individually?

The procedure says: Treat this as a system of equations, where the borrowing is represented by positive and negative values, and solve using the method of elimination.

The method of elimination says: Assign coefficients to each type of horse based on the borrowing relationships. Use elimination to solve for the unknowns, starting with the lowest-ranked horse and working upwards. The results are the pulling forces of each type of horse.

Answer: The pulling force of one Wu horse is *a*(=160/7) shi, one Zhong horse is *b*(=120/7) shi, and one Xia horse is *c*(=40/7) shi.
"""

from fractions import Fraction

# Define the system of equations based on the problem:
# Let x = pulling force of one Wu horse
# Let y = pulling force of one Zhong horse
# Let z = pulling force of one Xia horse

# Equation 1: Wu horse + 1 Zhong horse = 40 shi
# x + y = 40

# Equation 2: Zhong horse + 1 Xia horse = 40 shi
# y + z = 40

# Equation 3: Xia horse + 1 Wu horse = 40 shi
# z + x = 40

# Step 1: Eliminate one variable (e.g., z) by combining equations.
# From Equation 1: x + y = 40  => z = 40 - y
# From Equation 2: y + z = 40  => z = 40 - y
# From Equation 3: z + x = 40  =>

#----- content ends here -----

"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'"""
