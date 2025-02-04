"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲持 a(=75/2)錢 ，乙持 b(=25)錢 。
"""

#----- content starts here -----
"""
Suppose there are two people, Jia and Yi, holding unknown amounts of money.
Jia takes half of Yi's money and has 50 qian. Yi takes more than half of Jia's money and also has 50 qian.
Question: how much money does Jia and Yi each hold?

The procedure says: Solve it as a system of equations using the method of balancing (損益).

The answer says: Jia holds *a*(=75/2) qian, and Yi holds *b*(=25) qian.
"""

# Let 甲持錢 = x, 乙持錢 = y

# Equation 1: 甲得乙半而錢五十
# x + (1/2)y = 50
# Rearrange: 2x + y = 100

# Equation 2: 乙得甲太半而亦錢五十
# y + (3/2)x = 50
# Rearrange: 3x + 2y = 100

# Solve the system of equations using elimination

# Multiply Equation 1 by 2 to align coefficients of y
# 4x + 2y = 200
# 3x + 2y = 100

# Subtract the second equation from the first
# (4x + 2y) - (3x + 2y) = 200 - 100
x = Fraction(100, 2)  # x = 50

# Substitute x into Equation 1: 2x + y = 100
# 2(50) + y = 100
y = 100 - 75#----- content ends here -----

"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
