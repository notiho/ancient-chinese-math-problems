"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛 a ，直金 b兩 ，羊 c ，直金 d兩 。
"""

"""
To solve this problem, we need to translate the ancient Chinese math problem into Python code. The problem involves solving a system of linear equations to find the values of the unknowns.

The problem states:
1. 5 cows and 2 sheep cost 10 taels of gold.
2. 2 cows and 5 sheep cost 8 taels of gold.

We need to find the cost of one cow (`b`) and one sheep (`d`).

Here is the Python code:


"""


from fractions import Fraction

# Let b = cost of one cow (in taels of gold)
# Let d = cost of one sheep (in taels of gold)

# Equations:
# 5b + 2d = 10
# 2b + 5d = 8

# Solve for b and d using substitution or elimination
# Multiply the first equation by 2 and the second equation by 5 to eliminate b:
# 10b + 4d = 20
# 10b + 25d = 40

# Subtract the first equation from the second:
# (10b + 25d) - (10b + 4d) = 40 - 20
# 21d = 20
d = Fraction(20, 21)  # Cost of one sheep

# Substitute d back into the first equation to solve for b:
# 5b + 2d = 10
# 5b + 2 * (20/21) = 10
# 5b + 40/21 = 10
# 5b = 10 - 40/21
# 5b = (210/21) - (40/21)
# 5b = 170/21
b = Fraction(170, 105)  # Simplify: b = 34/21 (Cost of one cow)

# Assign the values to variables
a = 1  # Number of cows (not explicitly asked, but included for completeness)
c = 1  # Number of sheep (not explicitly asked, but included for completeness)

# Final answers
b  # Cost of one cow in taels of gold
d  # Cost of one sheep in taels of gold


"""


### Explanation of the solution:
1. We set up two equations based on the problem:
   - \( 5b + 2d = 10 \)
   - \( 2b + 5d = 8 \)
2. We use the elimination method to solve for \( d \) (cost of one sheep).
3. Substitute \( d \) back into one of the original equations to solve for \( b \) (cost of one cow).
4. The results are stored in variables `b` and `d`.

### Final Results:
- \( b = \frac{34}{21} \) taels of gold (cost of one cow)
- \( d = \frac{20}{21} \) taels of gold (cost of one sheep)
"""


"""
"""
